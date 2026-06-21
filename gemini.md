# Gemini & Agent Guidelines - LLD Monorepo

Welcome! This repository is a zero-to-advanced, production-grade Low-Level Design (LLD) monorepo. It serves as an educational encyclopedia and reference for Low-Level Design in Python. 

As an AI agent or contributor, please follow these guidelines when adding features, code patterns, projects, or documents.

---

## 1. Directory Structure Rules

All code and documents must be located in their respective directories:
- **docs/**: High-level or OOP-level concepts (Agile, SOLID, OOP basic elements).
- **patterns/<type>/<pattern_name>/**: Concrete design pattern.
  - Must contain `README.md` explaining the pattern with a Mermaid UML diagram.
  - Must contain `pattern.py` with fully typed code.
  - Must contain `test_pattern.py` with `pytest` unit tests.
- **projects/<project_name>/**: Real-world, multi-pattern projects using FastAPI.
  - Must have a clean architecture separation (Domain, Application, Infrastructure).

---

## 2. Python Coding Style

This repository enforces strict, modern Python coding standards:
- **Type Hinting**: All functions, methods, and classes MUST use type annotations (`typing` module or modern union types).
- **Formatting**: Strictly format code using `black` (100 char line limit) and `isort`.
- **Linting**: No unresolved warnings in `flake8`.
- **Docstrings**: Document all classes and public methods using Google style or Sphinx style docstrings.
- **Thread Safety**: For designs containing state (e.g., Singleton, Parking Lot allocation, Vending Machine), ensure thread-safety using Python's `threading.Lock`.

---

## 3. Documentation Style (ByteByteGo standard)

To keep documentation clean, visual, and highly readable:
1. **Mermaid Diagrams**: Include structural or interaction diagrams using Mermaid syntax in Markdown. Always wrap Mermaid labels in double quotes if they contain special characters (like `()`).
2. **Tabular Comparisons**: Use Markdown tables for comparisons (e.g., Strategy vs State pattern, Monolith vs Microservices).
3. **Analogy-First**: Begin every pattern or project document with a relatable, real-world, non-software analogy (e.g., an Adapter is like a travel plug adapter; the Observer is like subscribing to a newspaper).
4. **Pros & Cons**: Provide objective pros, cons, and performance/concurrency trade-offs for each pattern.

---

## 4. How to Verify & Validate

Always verify your changes before proposing or committing:
1. **Install requirements**: `pip install -r requirements.txt`
2. **Run pre-commit script**: `./pre-commit.sh` (or manually run `pytest`, `mypy .`, `flake8 .`, `black --check .`).
3. **Start FastAPI services**:
   ```bash
   uvicorn projects.parking_lot.main:app --reload
   ```
   Verify that Swagger UI is accessible at `http://127.0.0.1:8000/docs`.
