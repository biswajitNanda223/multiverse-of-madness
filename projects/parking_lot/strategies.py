from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

from .models import ParkingSpot, SpotType, VehicleType


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(
        self, entry_time: datetime, exit_time: datetime, vehicle_type: VehicleType
    ) -> float:
        """Calculate the total fee owed for parking."""
        pass


class HourlyPricingStrategy(PricingStrategy):
    def __init__(self) -> None:
        # Base hourly rates for each vehicle type
        self.hourly_rates = {
            VehicleType.MOTORCYCLE: 1.5,
            VehicleType.CAR: 3.0,
            VehicleType.TRUCK: 6.0,
        }

    def calculate_fee(
        self, entry_time: datetime, exit_time: datetime, vehicle_type: VehicleType
    ) -> float:
        duration = exit_time - entry_time
        duration_hours = max(
            1.0, duration.total_seconds() / 3600.0
        )  # Charge at least 1 hour
        rate = self.hourly_rates.get(vehicle_type, 2.0)
        return round(duration_hours * rate, 2)


class FlatPricingStrategy(PricingStrategy):
    def __init__(self, flat_rate: float = 5.0) -> None:
        self.flat_rate = flat_rate

    def calculate_fee(
        self, entry_time: datetime, exit_time: datetime, vehicle_type: VehicleType
    ) -> float:
        return self.flat_rate


class SpotAssignmentStrategy(ABC):
    @abstractmethod
    def assign_spot(
        self, floors: List[List[ParkingSpot]], vehicle_type: VehicleType
    ) -> Optional[ParkingSpot]:
        """Find and return the optimal parking spot according to the strategy."""
        pass


class NearestFirstStrategy(SpotAssignmentStrategy):
    def _get_matching_spot_type(self, vehicle_type: VehicleType) -> SpotType:
        if vehicle_type == VehicleType.MOTORCYCLE:
            return SpotType.MOTORCYCLE
        elif vehicle_type == VehicleType.CAR:
            return SpotType.COMPACT
        else:
            return SpotType.LARGE

    def assign_spot(
        self, floors: List[List[ParkingSpot]], vehicle_type: VehicleType
    ) -> Optional[ParkingSpot]:
        target_type = self._get_matching_spot_type(vehicle_type)
        # Search floor-by-floor (nearest floor first), spot-by-spot
        for floor_spots in floors:
            for spot in floor_spots:
                if not spot.is_occupied and spot.spot_type == target_type:
                    return spot
        return None
