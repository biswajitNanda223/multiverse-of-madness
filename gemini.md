# 🌌 Gemini & Agent Guidelines - Multiverse of Madness

Welcome! This repository is the **Multiverse of Madness**, a zero-to-advanced, production-grade Low-Level Design (LLD) and High-Level Design (HLD) Python monorepo. It serves as an educational encyclopedia and reference for software design across multiple architectural dimensions. 

As an AI agent or contributor, please follow these cosmic guidelines when adding features, design patterns, projects, or documents to ensure perfect order and prevent architectural collapse.

---

## 1. Directory Structure & Dimensions

All code and documents must be located in their respective dimensional planes:
- **docs/**: High-level or OOP-level concepts (Agile, SOLID, OOP basic elements, Concurrency, Design Principles).
- **system_design/**: High-Level Design (HLD) concepts, distributed systems building blocks (caching, sharding, CDN, reliability), and interactive Mermaid diagrams.
- **patterns/<type>/<pattern_name>/**: Concrete design pattern.
  - Must contain `README.md` explaining the pattern with a Mermaid UML diagram.
  - Must contain `pattern.py` with fully typed code.
  - Must contain `test_pattern.py` with `pytest` unit tests.
- **projects/<project_name>/**: Real-world, multi-pattern projects using FastAPI.
  - Must have a clean architecture separation (Domain, Application, Infrastructure).

> [!IMPORTANT]
> This repository is **strictly Python-only** for all implementation code, patterns, tests, and web projects. Do not introduce other languages for backend or service components.

---

## 2. Python Coding Style (Runes of Clarity)

This repository enforces strict, modern Python coding standards:
- **Type Hinting**: All functions, methods, and classes MUST use type annotations (`typing` module or modern union types).
- **Formatting**: Strictly format code using `black` (100 char line limit) and `isort`.
- **Linting**: No unresolved warnings in `flake8`.
- **Docstrings**: Document all classes and public methods using Google style or Sphinx style docstrings.
- **Thread Safety**: For designs containing state (e.g., Singleton, Parking Lot allocation, Vending Machine), ensure thread-safety using Python's `threading.Lock` or `threading.RLock`. Refer to [concurrency.md](file:///c:/personal%20Projects/lld/docs/concurrency.md) for detailed locking and synchronization rules.

---

## 3. Documentation Style (ByteByteGo standard)

To keep documentation clean, visual, and highly readable:
1. **Mermaid Diagrams**: Include structural or interaction diagrams using Mermaid syntax in Markdown. Always wrap Mermaid labels in double quotes if they contain special characters (like `()`).
2. **Tabular Comparisons**: Use Markdown tables for comparisons (e.g., Strategy vs State pattern, Monolith vs Microservices).
3. **Analogy-First**: Begin every pattern or project document with a relatable, real-world, non-software analogy (e.g., an Adapter is like a travel plug adapter; the Observer is like subscribing to a newspaper).
4. **Pros & Cons**: Provide objective pros, cons, and performance/concurrency trade-offs for each pattern.

---

## 4. How to Verify & Validate (Activating the Runes)

Always verify your changes before proposing or committing:
1. **Install requirements**: `pip install -r requirements.txt`
2. **Run pre-commit script**: `./pre-commit.sh` (or manually run `pytest`, `mypy .`, `flake8 .`, `black --check .`).
3. **Start FastAPI services**:
   ```bash
   uvicorn projects.parking_lot.main:app --reload
   ```
   Verify that Swagger UI is accessible at `http://127.0.0.1:8000/docs`.

