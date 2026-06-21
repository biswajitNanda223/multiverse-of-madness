# LLD Project: Parking Lot System

A Low-Level Design of an interview-grade, thread-safe **Parking Lot System** in Python, wrapped with a FastAPI web interface.

---

## 1. System Requirements

1. **Multiple Vehicle Types**: Support for Motorcycles, Cars, and Trucks.
2. **Multiple Spot Types**: Motorcycle spots, Compact spots (for cars), and Large spots (for trucks).
3. **Multiple Floors**: The parking lot contains multiple floors, each with its own set of spots.
4. **Spot Allocation Strategy**: Automatically allocate the nearest available spot of the correct type to the vehicle (Nearest-to-Entrance Strategy).
5. **Pricing Strategy**: Dynamic calculation of fees based on duration and vehicle type (e.g., flat rate first hour, then hourly rate).
6. **Thread-Safety**: Concurrency control when multiple entry/exit gates attempt to book spots simultaneously.
7. **FastAPI Web API**: Web interface showing real-world application of domain entities, services, and endpoints.

---

## 2. Class Diagram (UML)

```mermaid
classDiagram
    direction TB

    class Vehicle {
        <<abstract>>
        +license_plate: str
        +type: VehicleType
    }
    class Motorcycle {
        +type: VehicleType.MOTORCYCLE
    }
    class Car {
        +type: VehicleType.CAR
    }
    class Truck {
        +type: VehicleType.TRUCK
    }

    Vehicle <|-- Motorcycle
    Vehicle <|-- Car
    Vehicle <|-- Truck

    class ParkingSpot {
        <<abstract>>
        +spot_id: str
        +floor_number: int
        +type: SpotType
        +is_occupied: bool
        +park(vehicle: Vehicle) bool
        +unpark() void
    }
    class MotorcycleSpot {
        +type: SpotType.MOTORCYCLE
    }
    class CompactSpot {
        +type: SpotType.COMPACT
    }
    class LargeSpot {
        +type: SpotType.LARGE
    }

    ParkingSpot <|-- MotorcycleSpot
    ParkingSpot <|-- CompactSpot
    ParkingSpot <|-- LargeSpot

    class ParkingFloor {
        +floor_number: int
        +spots: List[ParkingSpot]
        +get_available_spot(vehicle_type: VehicleType) ParkingSpot
    }

    class ParkingLot {
        -instance: ParkingLot
        +name: str
        +floors: List[ParkingFloor]
        +park_vehicle(vehicle: Vehicle) Ticket
        +unpark_vehicle(ticket: Ticket) Payment
    }

    ParkingFloor "1" *-- "many" ParkingSpot
    ParkingLot "1" *-- "many" ParkingFloor

    class Ticket {
        +ticket_id: str
        +vehicle: Vehicle
        +spot: ParkingSpot
        +entry_time: datetime
    }

    class Payment {
        +payment_id: str
        +ticket: Ticket
        +amount: float
        +payment_time: datetime
        +status: PaymentStatus
    }

    ParkingLot ..> Ticket : Creates
    ParkingLot ..> Payment : Creates
```

---

## 3. Concurrency Design

When multiple cars try to enter different gates simultaneously, there is a risk of a race condition: two gates might see the same spot as vacant and assign it to different vehicles.
- **Solution**: We implement **Thread-Safety** in Python using `threading.Lock`. The `ParkingLotService` wraps all spot assignment operations inside a thread-safe context, protecting the shared state of `ParkingFloor` spots.

---

## 4. API Endpoints (FastAPI)

- `POST /parking-lot/init`: Initialize a parking lot with customized floors and spots.
- `POST /park`: Park a vehicle and receive a ticket.
- `POST /unpark`: Unpark a vehicle by providing a ticket ID, calculating the payment fee.
- `GET /status`: View current occupancy rates per floor and spot type.
