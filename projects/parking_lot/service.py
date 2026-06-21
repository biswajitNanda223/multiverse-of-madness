import uuid
from datetime import datetime
from threading import Lock
from typing import Dict, List, Optional

from .models import (
    Car,
    CompactSpot,
    LargeSpot,
    Motorcycle,
    MotorcycleSpot,
    ParkingSpot,
    Payment,
    Ticket,
    Truck,
    Vehicle,
    VehicleType,
)
from .strategies import (
    HourlyPricingStrategy,
    NearestFirstStrategy,
    PricingStrategy,
    SpotAssignmentStrategy,
)


class ParkingLotService:
    _instance: Optional["ParkingLotService"] = None
    _lock: Lock = Lock()

    def __new__(cls) -> "ParkingLotService":
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        self.floors: List[List[ParkingSpot]] = []
        self.tickets: Dict[str, Ticket] = {}
        self.pricing_strategy: PricingStrategy = HourlyPricingStrategy()
        self.spot_assignment_strategy: SpotAssignmentStrategy = NearestFirstStrategy()
        self.lock: Lock = Lock()
        self._initialized = True

    def initialize_parking_lot(
        self, num_floors: int, spots_config: Dict[str, int]
    ) -> None:
        """
        Initializes the parking lot with the specified number of floors and spots.
        Example configuration:
        spots_config = {
            "motorcycle": 5,
            "compact": 10,
            "large": 3
        }
        """
        with self.lock:
            self.floors = []
            self.tickets = {}
            for floor_idx in range(1, num_floors + 1):
                floor_spots: List[ParkingSpot] = []
                # Add motorcycle spots
                for i in range(1, spots_config.get("motorcycle", 0) + 1):
                    floor_spots.append(MotorcycleSpot(f"F{floor_idx}-M{i}", floor_idx))
                # Add compact spots
                for i in range(1, spots_config.get("compact", 0) + 1):
                    floor_spots.append(CompactSpot(f"F{floor_idx}-C{i}", floor_idx))
                # Add large spots
                for i in range(1, spots_config.get("large", 0) + 1):
                    floor_spots.append(LargeSpot(f"F{floor_idx}-L{i}", floor_idx))

                self.floors.append(floor_spots)

    def _create_vehicle(self, license_plate: str, vehicle_type: VehicleType) -> Vehicle:
        if vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle(license_plate)
        elif vehicle_type == VehicleType.CAR:
            return Car(license_plate)
        elif vehicle_type == VehicleType.TRUCK:
            return Truck(license_plate)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

    def park_vehicle(self, license_plate: str, vehicle_type: VehicleType) -> Ticket:
        with self.lock:
            # Check if parking lot is initialized
            if not self.floors:
                raise ValueError("Parking Lot is not initialized.")

            # Use assignment strategy to find a spot
            spot = self.spot_assignment_strategy.assign_spot(self.floors, vehicle_type)
            if not spot:
                raise ValueError(f"No available spots for vehicle type: {vehicle_type}")

            vehicle = self._create_vehicle(license_plate, vehicle_type)
            success = spot.park(vehicle)
            if not success:
                raise ValueError("Failed to park vehicle: spot already occupied.")

            # Generate Ticket
            ticket_id = str(uuid.uuid4())[:8]
            ticket = Ticket(
                ticket_id=ticket_id,
                license_plate=license_plate,
                vehicle_type=vehicle_type,
                floor_number=spot.floor_number,
                spot_id=spot.spot_id,
            )
            self.tickets[ticket_id] = ticket
            return ticket

    def unpark_vehicle(self, ticket_id: str) -> Payment:
        with self.lock:
            if ticket_id not in self.tickets:
                raise KeyError(f"Invalid ticket ID: {ticket_id}")

            ticket = self.tickets[ticket_id]

            # Find the spot and unpark the vehicle
            target_spot: Optional[ParkingSpot] = None
            for floor_spots in self.floors:
                for spot in floor_spots:
                    if spot.spot_id == ticket.spot_id:
                        target_spot = spot
                        break
                if target_spot:
                    break

            if not target_spot or not target_spot.is_occupied:
                raise ValueError("Spot associated with this ticket is already vacant.")

            target_spot.unpark()

            # Calculate fee
            exit_time = datetime.now()
            amount = self.pricing_strategy.calculate_fee(
                ticket.entry_time, exit_time, ticket.vehicle_type
            )

            # Create payment receipt
            payment_id = str(uuid.uuid4())[:8]
            payment = Payment(payment_id=payment_id, ticket_id=ticket_id, amount=amount)

            # Remove ticket
            del self.tickets[ticket_id]
            return payment

    def get_status(self) -> Dict[str, Dict[str, int]]:
        with self.lock:
            status = {}
            for floor_idx, floor_spots in enumerate(self.floors, 1):
                floor_stats = {
                    "total_spots": len(floor_spots),
                    "occupied_spots": sum(1 for s in floor_spots if s.is_occupied),
                    "available_spots": sum(1 for s in floor_spots if not s.is_occupied),
                    "motorcycle_available": sum(
                        1
                        for s in floor_spots
                        if not s.is_occupied and s.spot_type == "MOTORCYCLE"
                    ),
                    "compact_available": sum(
                        1
                        for s in floor_spots
                        if not s.is_occupied and s.spot_type == "COMPACT"
                    ),
                    "large_available": sum(
                        1
                        for s in floor_spots
                        if not s.is_occupied and s.spot_type == "LARGE"
                    ),
                }
                status[f"Floor {floor_idx}"] = floor_stats
            return status
