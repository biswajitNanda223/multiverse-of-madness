# 🌌 Multiverse of Madness: Python Low-Level Design (LLD) Monorepo 🌌

<p align="center">
  <img src="assets/multiverse_banner.png" alt="Multiverse of Madness Cosmic Portal Banner" width="100%">
</p>

[![CI Pipeline](https://github.com/biswajitNanda223/multiverse-of-madness/actions/workflows/ci.yml/badge.svg)](https://github.com/biswajitNanda223/multiverse-of-madness/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-green.svg)](https://fastapi.tiangolo.com)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Static Types](https://img.shields.io/badge/mypy-strict-blue.svg)](http://mypy-lang.org/)

> 🌌 **Tagline**
> *Taming the architectural chaos in the Low-Level Design multiverse. A comprehensive Python monorepo covering 23 GoF design patterns, OOP & SOLID wiki, FastAPI microservices, and Secure-by-Design hardening tools.*

Welcome, dimensional traveler, to the **Multiverse of Madness**—the ultimate, production-grade repository for mastering Python Low-Level Design (LLD) and High-Level System Design (HLD). In this cosmic workspace, we tame the chaotic entropic forces of software architecture. This monorepo serves as a comprehensive educational wiki, spanning 13 days of celestial HLD building blocks, fundamental OOP/SOLID principles, interactive Mermaid UML schemas, the 23 classical Gang of Four (GoF) design patterns, and container-orchestrated FastAPI microservices hardened against multiversal threats.

---

## 🗺️ Map of the Multiverse

```text
multiverse-of-madness/
├── .github/workflows/ci.yml    # Continuous Integration pipeline (linting & pytest)
├── docs/                       # 🔮 The Mystic Archives (LLD Conceptual Wiki)
│   ├── index.md                # Wiki home index page
│   ├── sdlc.md                 # SDLC lifecycles & design pipelines
│   ├── oop_fundamentals.md     # Encapsulation, Abstraction, & SOLID in Python
│   ├── design_principles.md    # Code health runes: DRY, KISS, YAGNI
│   ├── concurrency.md          # Multithreading, locks, & GIL synchronization
│   └── uml_guide.md            # UML Class, Sequence, & State diagrams via Mermaid
├── system_design/              # 🌌 The Celestial Roadmap (13-Day System Design Guide)
│   ├── README.md               # Guide index & roadmaps
│   └── Day-01-to-13.md         # Daily HLD concepts & interactive flowcharts
├── patterns/                   # 🌀 The 23 Dimensions of GoF Design Patterns
│   ├── creational/             # Singleton, Factory Method, Builder, Prototype, etc.
│   ├── structural/             # Adapter, Bridge, Composite, Decorator, Facade, etc.
│   └── behavioral/             # Chain of Responsibility, Command, Observer, State, etc.
├── projects/                   # 🧪 Alchemy Labs (FastAPI Microservices)
│   ├── parking_lot/            # Thread-safe multi-floor parking lot system
│   ├── splitwise/              # Greedy debt simplification app
│   └── vending_machine/        # State Pattern vending machine simulation
├── tools/                      # 🛡️ Aegis Hardening (Secure-by-Design Tools)
│   └── appsec_forge/           # OWASP vulnerability scanner & STRIDE threat modeler
├── docker-compose.yml          # Container configuration for local portal deployment
├── requirements.txt            # Package dependencies
├── pre-commit.sh               # Local pre-commit verification script
└── gemini.md                   # AI Agent & developer guidelines
```

---

## 📖 Grimoire of Architectural Dimensions

### 1. 🔮 The Mystic Archives (`docs/`)
Deep conceptual write-ups establishing foundational design patterns and principles:
- **[OOP & SOLID in Python](file:///c:/personal%20Projects/lld/docs/oop_fundamentals.md)**: Zero-to-advanced overview of abstract base classes (ABCs), pythonic access modifiers, getters/setters, properties, and magic methods, combined with clean "Before" and "After" SOLID examples.
- **[SDLC Frameworks](file:///c:/personal%20Projects/lld/docs/sdlc.md)**: Deep dive into systems development lifecycles, showing how requirements convert into High-Level Design (HLD) and Low-Level Design (LLD) blueprints.
- **[UML Guide](file:///c:/personal%20Projects/lld/docs/uml_guide.md)**: Structural associations (aggregation vs composition) and behavioral sequence/state patterns detailed via Mermaid diagrams.
- **[Software Design Principles](file:///c:/personal%20Projects/lld/docs/design_principles.md)**: Practical Python guides to clean code principles: DRY (Don't Repeat Yourself), KISS (Keep It Simple, Stupid), and YAGNI (You Aren't Gonna Need It).
- **[Concurrency & Thread-Safety](file:///c:/personal%20Projects/lld/docs/concurrency.md)**: Master multithreading, multiprocessing, the GIL (Global Interpreter Lock), critical sections, mutual exclusion locks, semaphores, and async queue patterns.

### 2. 🌀 The 23 Dimensions of GoF Patterns (`patterns/`)
Each of the 23 Gang of Four (GoF) design patterns has its own dimensional folder containing:
- `README.md`: Analogy, ByteByteGo-style Mermaid UML diagram, pros/cons, and performance notes.
- `pattern.py`: Strict, type-annotated, thread-safe implementation.
- `test_pattern.py`: Standard unit tests checking bounds and edge cases.

### 3. 🧪 Alchemy Labs (`projects/`)
Real-world, multi-pattern FastAPI microservices operating in parallel:
- **[Parking Lot](file:///c:/personal%20Projects/lld/projects/parking_lot/) (Port 8001)**: Multi-floor parking lot utilizing Strategy Pattern (for pricing and spot assignment), and `threading.Lock` for race-condition prevention.
- **[Splitwise](file:///c:/personal%20Projects/lld/projects/splitwise/) (Port 8002)**: Expense management utilizing Strategy Pattern (split calculations) and a greedy Min-Flow Cash Flow algorithm to minimize settlement routes.
- **[Vending Machine](file:///c:/personal%20Projects/lld/projects/vending_machine/) (Port 8003)**: Dynamic coin validation and inventory management utilizing the State Design Pattern.

### 4. 🛡️ Aegis Hardening (`tools/`)
Defending your applications against multiversal exploits:
- **[SecureForge 2026](file:///c:/personal%20Projects/lld/tools/appsec_forge/) (Port 8004)**: Security scanning tool and API checking for SQL Injections, weak cryptography (MD5/SHA1), hardcoded secrets, and wildcard CORS policies. It automatically outputs STRIDE threat models and hardened FastAPI boilerplates.

### 5. 🌌 The Celestial Roadmap (`system_design/`)
High-Level Design (HLD) bootcamps:
- **[System Design 13-Day Bootcamp](file:///c:/personal%20Projects/lld/system_design/README.md)**: A complete, structured journey through HLD building blocks—client-server models, OSI/TCP-IP networking, SQL vs NoSQL, caching strategies, monoliths vs microservices, load balancing, sharding, replication quorums, messaging systems, CDNs, and reliability engineering. Enhanced with interactive **Mermaid.js** diagrams.

---

## 🚀 Activating the Portal (Quick Start)

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

## 🧪 Verification & Runes Validation

We enforce strict validation pipelines to ensure architectural consistency:
- **Imports**: Sorted via `isort`.
- **Styling**: Formatted via `black` (100 char limit).
- **Linting**: Verified via `flake8`.
- **Types**: Confirmed via `mypy`.
- **Tests**: Automated via `pytest` run locally and inside GitHub Actions.

