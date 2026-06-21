# Advanced Python Low-Level Design (LLD) Monorepo (2026 Edition)

[![CI Pipeline](https://github.com/biswajitNanda223/multiverse-of-madness/actions/workflows/ci.yml/badge.svg)](https://github.com/biswajitNanda223/multiverse-of-madness/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-green.svg)](https://fastapi.tiangolo.com)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Static Types](https://img.shields.io/badge/mypy-strict-blue.svg)](http://mypy-lang.org/)

Welcome to the ultimate, production-grade **Python Low-Level Design (LLD) Monorepo**. This project is designed as an educational encyclopedia and modern reference for OOP, SOLID design principles, structural UML diagrams, Gang of Four (GoF) design patterns, and container-orchestrated microservice architectures in Python.

---

## 🗺️ Monorepo Roadmap & Structure

```text
lld/
├── .github/workflows/ci.yml    # GitHub Actions Continuous Integration (tests & linting)
├── docs/                       # LLD conceptual wiki
│   ├── index.md                # Wiki home page index
│   ├── sdlc.md                 # SDLC methodologies (Agile vs Waterfall, HLD vs LLD)
│   ├── oop_fundamentals.md     # Encapsulation, Abstraction, SOLID principles in Python
│   └── uml_guide.md            # UML Class, Sequence, and State diagrams via Mermaid
├── patterns/                   # 23 Gang of Four (GoF) design patterns in Python
│   ├── creational/             # Singleton, Factory Method, Abstract Factory, Builder, Prototype
│   ├── structural/             # Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
│   └── behavioral/             # Chain of Responsibility, Command, Interpreter, Iterator, Mediator,
│                               # Memento, Observer, State, Strategy, Template Method, Visitor
├── projects/                   # Multi-pattern real-world FastAPI projects
│   ├── parking_lot/            # Thread-safe multi-floor parking lot system
│   ├── splitwise/              # Expense sharing app with greedy debt simplification algorithm
│   └── vending_machine/        # State Pattern Vending Machine simulation
├── tools/                      # Security & hardening helper tools
│   └── appsec_forge/           # OWASP 2026 App Security vulnerability scanner & template generator
├── docker-compose.yml          # Container configuration for local deployment
├── requirements.txt            # Package dependencies
├── pre-commit.sh               # Local pre-commit verification script
└── gemini.md                   # AI Agent & developer guidelines file
```

---

## 📖 Features Overview

### 1. Conceptual Wiki (`docs/`)
- **[OOP & SOLID in Python](file:///c:/personal%20Projects/lld/docs/oop_fundamentals.md)**: Zero-to-advanced overview of abstract base classes (ABCs), pythonic access modifiers, getters/setters, properties, and magic methods, combined with clean "Before" and "After" SOLID examples.
- **[SDLC Frameworks](file:///c:/personal%20Projects/lld/docs/sdlc.md)**: Deep dive into systems development lifecycles, showing how requirements convert into High-Level Design (HLD) and Low-Level Design (LLD) blueprints.
- **[UML Guide](file:///c:/personal%20Projects/lld/docs/uml_guide.md)**: Structural associations (aggregation vs composition) and behavioral sequence/state patterns detailed via Mermaid diagrams.

### 2. Concrete Design Patterns (`patterns/`)
Each of the 23 Gang of Four (GoF) design patterns has its own folder containing:
- `README.md`: Analogy, ByteByteGo-style Mermaid UML diagram, pros/cons, and performance notes.
- `pattern.py`: Strict, type-annotated, thread-safe implementation.
- `test_pattern.py`: Standard unit tests checking bounds and edge cases.

### 3. FastAPI LLD Projects (`projects/`)
Multi-pattern real-world services:
- **[Parking Lot](file:///c:/personal%20Projects/lld/projects/parking_lot/) (Port 8001)**: Multi-floor parking lot utilizing Strategy Pattern (for pricing and spot assignment), and `threading.Lock` for race-condition prevention.
- **[Splitwise](file:///c:/personal%20Projects/lld/projects/splitwise/) (Port 8002)**: Expense management utilizing Strategy Pattern (split calculations) and a greedy Min-Flow Cash Flow algorithm to minimize settlement routes.
- **[Vending Machine](file:///c:/personal%20Projects/lld/projects/vending_machine/) (Port 8003)**: Dynamic coin validation and inventory management utilizing the State Design Pattern.

### 4. Cyber Security Hardening Tools (`tools/`)
- **[SecureForge 2026](file:///c:/personal%20Projects/lld/tools/appsec_forge/) (Port 8004)**: Security scanning tool and API checking for SQL Injections, weak cryptography (MD5/SHA1), hardcoded secrets, and wildcard CORS policies. It automatically outputs STRIDE threat models and hardened FastAPI boilerplates.

---

## 🚀 Quick Start Guide

### 1. Local Setup
Ensure Python 3.11+ is installed. Clone the repository and run:
```bash
# Install dependencies
pip install -r requirements.txt

# Run all unit tests (67 test specs across patterns, projects, and tools)
python -m pytest --import-mode=importlib patterns/ projects/ tools/

# Run the local pre-commit checks
./pre-commit.sh
```

### 2. Multi-Container Orchestration (Docker Compose)
To spin up all FastAPI applications (Parking Lot, Splitwise, Vending Machine, and SecureForge) simultaneously:
```bash
docker-compose up --build
```
Once healthy, access Swagger UI APIs at:
- **Parking Lot API**: [http://localhost:8001/docs](http://localhost:8001/docs)
- **Splitwise API**: [http://localhost:8002/docs](http://localhost:8002/docs)
- **Vending Machine API**: [http://localhost:8003/docs](http://localhost:8003/docs)
- **SecureForge API**: [http://localhost:8004/docs](http://localhost:8004/docs)

---

## 🧪 Testing Coverage Validation

We enforce strict validation pipelines:
- **Imports**: Sorted via `isort`.
- **Styling**: Formatted via `black` (100 char limit).
- **Linting**: Verified via `flake8`.
- **Types**: Confirmed via `mypy`.
- **Tests**: Automated via `pytest` run locally and inside GitHub Actions.
