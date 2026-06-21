# Dockerfile for Parking Lot LLD Service
FROM python:3.11-slim

WORKDIR /app

# Copy requirements from root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy current project directory and root package definition
COPY ./projects/parking_lot /app/projects/parking_lot
COPY ./projects/__init__.py /app/projects/__init__.py

EXPOSE 8000

# Set Python path to ensure module imports resolve correctly
ENV PYTHONPATH=/app

CMD ["uvicorn", "projects.parking_lot.main:app", "--host", "0.0.0.0", "--port", "8000"]
