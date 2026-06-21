from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .models import VehicleType
from .service import ParkingLotService

app = FastAPI(
    title="Parking Lot LLD API",
    description="Low-Level Design interface for a thread-safe multi-floor Parking Lot System.",
    version="1.0.0",
)

# Instantiate the Singleton Service
parking_lot_service = ParkingLotService()


# Request/Response Schemas
class InitRequest(BaseModel):
    num_floors: int = Field(..., ge=1, description="Number of floors in the parking lot")
    spots_config: Dict[str, int] = Field(
        default={"motorcycle": 5, "compact": 10, "large": 3},
        description="Configuration of spot counts by type on each floor",
    )


class ParkRequest(BaseModel):
    license_plate: str = Field(..., description="Vehicle's license plate number")
    vehicle_type: VehicleType = Field(..., description="Type of vehicle: MOTORCYCLE, CAR, or TRUCK")


class TicketResponse(BaseModel):
    ticket_id: str
    license_plate: str
    vehicle_type: str
    floor_number: int
    spot_id: str
    entry_time: str


class UnparkRequest(BaseModel):
    ticket_id: str = Field(..., description="ID of the ticket issued during parking")


class PaymentResponse(BaseModel):
    payment_id: str
    ticket_id: str
    amount: float
    payment_time: str
    status: str


# Endpoints
@app.post("/parking-lot/init", tags=["Initialization"])
def init_parking_lot(request: InitRequest) -> Dict[str, str]:
    try:
        parking_lot_service.initialize_parking_lot(request.num_floors, request.spots_config)
        return {
            "status": "success",
            "message": f"Initialized parking lot with {request.num_floors} floors.",
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/park", response_model=TicketResponse, tags=["Parking Operations"])
def park_vehicle(request: ParkRequest) -> TicketResponse:
    try:
        ticket = parking_lot_service.park_vehicle(request.license_plate, request.vehicle_type)
        return TicketResponse(
            ticket_id=ticket.ticket_id,
            license_plate=ticket.license_plate,
            vehicle_type=ticket.vehicle_type,
            floor_number=ticket.floor_number,
            spot_id=ticket.spot_id,
            entry_time=ticket.entry_time.isoformat(),
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/unpark", response_model=PaymentResponse, tags=["Parking Operations"])
def unpark_vehicle(request: UnparkRequest) -> PaymentResponse:
    try:
        payment = parking_lot_service.unpark_vehicle(request.ticket_id)
        return PaymentResponse(
            payment_id=payment.payment_id,
            ticket_id=payment.ticket_id,
            amount=payment.amount,
            payment_time=payment.payment_time.isoformat(),
            status=payment.status,
        )
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/status", tags=["Monitoring"])
def get_occupancy_status() -> Dict[str, Dict[str, int]]:
    return parking_lot_service.get_status()
