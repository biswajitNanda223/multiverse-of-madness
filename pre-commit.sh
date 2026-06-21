#!/bin/bash
# Pre-Commit Execution Script for LLD Monorepo
# Checks formatting, code style, types, and runs tests.

echo "=== [1/5] Running Isort (Imports Sorting) ==="
isort --check-only .
if [ $? -ne 0 ]; then
    echo "❌ Isort checks failed! Run 'isort .' to auto-fix."
    exit 1
fi

echo "=== [2/5] Running Black (Formatting Check) ==="
black --check .
if [ $? -ne 0 ]; then
    echo "❌ Black formatting checks failed! Run 'black .' to auto-format."
    exit 1
fi

echo "=== [3/5] Running Flake8 (Linting Check) ==="
flake8 .
if [ $? -ne 0 ]; then
    echo "❌ Flake8 checks failed! Please fix style violations."
    exit 1
fi

echo "=== [4/5] Running Mypy (Type Verification) ==="
mypy --explicit-package-bases .
if [ $? -ne 0 ]; then
    echo "❌ Mypy static type check failed! Check type annotations."
    exit 1
fi

echo "=== [5/5] Running Pytest (Unit Tests) ==="
pytest
if [ $? -ne 0 ]; then
    echo "❌ Pytest validation failed! Some tests are broken."
    exit 1
fi

echo "✅ All pre-commit checks passed successfully!"
exit 0
