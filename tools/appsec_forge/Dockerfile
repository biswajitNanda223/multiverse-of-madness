# Dockerfile for SecureForge 2026 Service
FROM python:3.11-slim

WORKDIR /app

# Copy requirements from root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy current project directory and root package definition
COPY ./tools/appsec_forge /app/tools/appsec_forge
COPY ./tools/__init__.py /app/tools/__init__.py

EXPOSE 8000

# Set Python path to ensure module imports resolve correctly
ENV PYTHONPATH=/app

CMD ["uvicorn", "tools.appsec_forge.main:app", "--host", "0.0.0.0", "--port", "8000"]
