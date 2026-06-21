import time
from datetime import datetime, timedelta

import pytest

from .models import VehicleType
from .service import ParkingLotService


@pytest.fixture(autouse=True)
def setup_service() -> None:
    # Reset singleton status for tests
    service = ParkingLotService()
    service.initialize_parking_lot(
        num_floors=2, spots_config={"motorcycle": 2, "compact": 2, "large": 1}
    )


def test_parking_lot_initialization() -> None:
    service = ParkingLotService()
    status = service.get_status()

    assert "Floor 1" in status
    assert "Floor 2" in status
    assert status["Floor 1"]["total_spots"] == 5
    assert status["Floor 1"]["motorcycle_available"] == 2
    assert status["Floor 1"]["compact_available"] == 2
    assert status["Floor 1"]["large_available"] == 1


def test_park_vehicle_success() -> None:
    service = ParkingLotService()
    ticket = service.park_vehicle("CAR-1234", VehicleType.CAR)

    assert ticket.license_plate == "CAR-1234"
    assert ticket.vehicle_type == VehicleType.CAR
    assert ticket.floor_number == 1
    assert ticket.spot_id == "F1-C1"  # Nearest compact spot

    # Status should show 1 less compact spot on Floor 1
    status = service.get_status()
    assert status["Floor 1"]["compact_available"] == 1
    assert status["Floor 1"]["occupied_spots"] == 1


def test_park_vehicle_no_spots() -> None:
    service = ParkingLotService()
    # Fill both compact spots on floor 1, and both compact spots on floor 2
    service.park_vehicle("CAR-1", VehicleType.CAR)
    service.park_vehicle("CAR-2", VehicleType.CAR)
    service.park_vehicle("CAR-3", VehicleType.CAR)
    service.park_vehicle("CAR-4", VehicleType.CAR)

    # 5th car should fail
    with pytest.raises(ValueError, match="No available spots"):
        service.park_vehicle("CAR-5", VehicleType.CAR)


def test_unpark_vehicle_success() -> None:
    service = ParkingLotService()
    ticket = service.park_vehicle("CAR-U", VehicleType.CAR)

    # Artificially alter entry time to test pricing
    ticket.entry_time = datetime.now() - timedelta(hours=2)

    payment = service.unpark_vehicle(ticket.ticket_id)

    assert payment.ticket_id == ticket.ticket_id
    assert payment.amount == 6.0  # 2 hours * $3.0/hr

    # Verify spot is freed
    status = service.get_status()
    assert status["Floor 1"]["compact_available"] == 2


def test_unpark_invalid_ticket() -> None:
    service = ParkingLotService()
    with pytest.raises(KeyError):
        service.unpark_vehicle("INVALID-TICKET")
