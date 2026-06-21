# Dockerfile for Splitwise LLD Service
FROM python:3.11-slim

WORKDIR /app

# Copy requirements from root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy current project directory and root package definition
COPY ./projects/splitwise /app/projects/splitwise
COPY ./projects/__init__.py /app/projects/__init__.py

EXPOSE 8000

# Set Python path to ensure module imports resolve correctly
ENV PYTHONPATH=/app

CMD ["uvicorn", "projects.splitwise.main:app", "--host", "0.0.0.0", "--port", "8000"]
