# 🚗 LLD Project: Thread-Safe Parking Lot System

A production-grade, interview-ready **Low-Level Design (LLD)** of a multi-floor, thread-safe **Parking Lot System** in Python, exposed via a clean **FastAPI** web service.

---

## 🧭 System Requirements

1. **Multiple Vehicle Types**: Support for `Motorcycles`, `Cars`, and `Trucks`.
2. **Multiple Spot Types**: `Motorcycle Spots`, `Compact Spots` (for cars), and `Large Spots` (for trucks).
3. **Multi-Floor Support**: The parking lot contains multiple floors, each managing its own allocation map.
4. **Dynamic Spot Allocation**: Automatically allocates the nearest available spot of the correct type (Nearest-First strategy).
5. **Dynamic Pricing Strategy**: Calculates fees dynamically based on duration and vehicle type (e.g., flat rate first hour, then hourly rate).
6. **Thread-Safety & Concurrency**: Mutual exclusion control when multiple entry/exit gates attempt to book or vacate spots concurrently.
7. **FastAPI Web API**: Web endpoints representing real-world services, domain entities, and occupancy statuses.

---

## 📊 Class Diagram (UML)

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

## 🔒 Concurrency & Thread-Safety Design

When multiple vehicles enter through different gates simultaneously, race conditions can occur (e.g., assigning the same parking spot to two different vehicles).
- **Thread-Safety Guard**: Implemented using Python's `threading.Lock` inside the `ParkingLotService` singleton. All spot allocation and checkout transactions are executed within atomic critical sections, preventing race conditions.
- For a deeper dive into Python locking and synchronization paradigms, see the [concurrency.md](file:///c:/personal%20Projects/lld/docs/concurrency.md) wiki page.

---

## 🔌 REST API Endpoints (FastAPI)

| Method | Endpoint | Description | Payloads / Parameters |
| :---: | :--- | :--- | :--- |
| `POST` | `/parking-lot/init` | Initialize parking lot with custom floors and spot maps | `num_floors`, `spots_config` |
| `POST` | `/park` | Park a vehicle and receive an entry ticket | `license_plate`, `vehicle_type` |
| `POST` | `/unpark` | Vacate a spot, calculate duration, and return invoice | `ticket_id` |
| `GET` | `/status` | Retrieve real-time occupancy maps per floor | None |
