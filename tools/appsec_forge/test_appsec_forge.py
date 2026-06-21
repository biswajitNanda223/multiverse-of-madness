import os
import tempfile

import pytest

from .generator import SecurityTemplateGenerator
from .scanner import SecurityScanner
from .threat_model import STRIDEThreatModeler


def test_scanner_detects_vulnerabilities() -> None:
    scanner = SecurityScanner()

    # Create a temp file containing insecure code patterns
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".py") as f:
        f.write('api_key = "ab12cd34ef56gh78"\n')
        f.write("hashlib.md5(data)\n")
        f.write("db.execute('SELECT * FROM users WHERE name = ' + user_input)\n")
        f.write("allow_origins = ['*']\n")
        temp_file_name = f.name

    try:
        alerts = scanner.scan_file(temp_file_name)
        rules = [alert["rule"] for alert in alerts]

        assert "hardcoded_secret" in rules
        assert "weak_hash" in rules
        assert "insecure_cors" in rules
    finally:
        os.remove(temp_file_name)


def test_boilerplate_generation() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        msg = SecurityTemplateGenerator.generate_boilerplate(temp_dir)

        assert "Successfully generated" in msg
        assert os.path.exists(os.path.join(temp_dir, "main.py"))
        assert os.path.exists(os.path.join(temp_dir, "README.md"))
        assert os.path.exists(os.path.join(temp_dir, "requirements.txt"))


def test_threat_modeler() -> None:
    model = STRIDEThreatModeler.generate_stride_model("microservice")
    assert "# STRIDE Threat Model" in model
    assert "Spoofing" in model
    assert "Information Disclosure" in model
