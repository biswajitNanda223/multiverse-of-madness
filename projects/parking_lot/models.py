from abc import ABC
from datetime import datetime
from enum import Enum
from typing import Optional


class VehicleType(str, Enum):
    MOTORCYCLE = "MOTORCYCLE"
    CAR = "CAR"
    TRUCK = "TRUCK"


class SpotType(str, Enum):
    MOTORCYCLE = "MOTORCYCLE"
    COMPACT = "COMPACT"
    LARGE = "LARGE"


class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    REFUNDED = "REFUNDED"


class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate: str = license_plate
        self.vehicle_type: VehicleType = vehicle_type


class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)


class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.CAR)


class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.TRUCK)


class ParkingSpot(ABC):
    def __init__(self, spot_id: str, floor_number: int, spot_type: SpotType):
        self.spot_id: str = spot_id
        self.floor_number: int = floor_number
        self.spot_type: SpotType = spot_type
        self.is_occupied: bool = False
        self.parked_vehicle: Optional[Vehicle] = None

    def park(self, vehicle: Vehicle) -> bool:
        if self.is_occupied:
            return False
        self.is_occupied = True
        self.parked_vehicle = vehicle
        return True

    def unpark(self) -> None:
        self.is_occupied = False
        self.parked_vehicle = None


class MotorcycleSpot(ParkingSpot):
    def __init__(self, spot_id: str, floor_number: int):
        super().__init__(spot_id, floor_number, SpotType.MOTORCYCLE)


class CompactSpot(ParkingSpot):
    def __init__(self, spot_id: str, floor_number: int):
        super().__init__(spot_id, floor_number, SpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, spot_id: str, floor_number: int):
        super().__init__(spot_id, floor_number, SpotType.LARGE)


class Ticket:
    def __init__(
        self,
        ticket_id: str,
        license_plate: str,
        vehicle_type: VehicleType,
        floor_number: int,
        spot_id: str,
    ):
        self.ticket_id: str = ticket_id
        self.license_plate: str = license_plate
        self.vehicle_type: VehicleType = vehicle_type
        self.floor_number: int = floor_number
        self.spot_id: str = spot_id
        self.entry_time: datetime = datetime.now()


class Payment:
    def __init__(self, payment_id: str, ticket_id: str, amount: float):
        self.payment_id: str = payment_id
        self.ticket_id: str = ticket_id
        self.amount: float = amount
        self.payment_time: datetime = datetime.now()
        self.status: PaymentStatus = PaymentStatus.COMPLETED
