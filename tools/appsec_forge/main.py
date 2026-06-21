from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .generator import SecurityTemplateGenerator
from .scanner import SecurityScanner
from .threat_model import STRIDEThreatModeler

app = FastAPI(
    title="SecureForge 2026 API",
    description=(
        "Microservice API for static application vulnerability "
        "analysis and STRIDE threat modeling."
    ),
    version="1.0.0",
)

scanner = SecurityScanner()


class CodeScanRequest(BaseModel):
    file_path: str = Field(
        ..., description="Target file path or directory on disk to run static analysis"
    )


class GenerateRequest(BaseModel):
    output_path: str = Field(
        ..., description="Disk directory path where secure template will be written"
    )


class ThreatRequest(BaseModel):
    app_type: str = Field(
        "web", description="Target application type (e.g. web, microservice, mobile)"
    )


@app.post("/sec/scan", tags=["Security Scan"])
def scan_codebase(request: CodeScanRequest) -> Dict[str, Any]:
    import os

    if not os.path.exists(request.file_path):
        raise HTTPException(status_code=404, detail="Target path not found.")

    if os.path.isdir(request.file_path):
        results = scanner.scan_directory(request.file_path)
    else:
        results = scanner.scan_file(request.file_path)

    return {
        "status": "scan_completed",
        "alerts_count": len(results),
        "vulnerabilities": results,
    }


@app.post("/sec/generate", tags=["Hardening Template"])
def generate_secured_boilerplate(request: GenerateRequest) -> Dict[str, str]:
    try:
        msg = SecurityTemplateGenerator.generate_boilerplate(request.output_path)
        return {"status": "success", "message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/sec/threat-model", tags=["Threat Modeling"])
def create_threat_model(request: ThreatRequest) -> Dict[str, str]:
    model_md = STRIDEThreatModeler.generate_stride_model(request.app_type)
    return {"app_type": request.app_type, "threat_model_markdown": model_md}
