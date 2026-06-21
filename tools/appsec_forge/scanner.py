import os
import re
from typing import Dict, List


class SecurityScanner:
    def __init__(self) -> None:
        # Regex patterns for static code analysis
        self.rules = {
            "hardcoded_secret": re.compile(
                r"(?:key|password|secret|token|passwd|api_key)\s*=\s*['\"][a-zA-Z0-9_\-+=/]{8,}['\"]",
                re.IGNORECASE,
            ),
            "weak_hash": re.compile(r"hashlib\.(?:md5|sha1)\(", re.IGNORECASE),
            "sql_injection": re.compile(
                r"\.execute\(\s*f?['\"].*?\{\w+\}.*?['\"]\s*\)", re.IGNORECASE
            ),
            "insecure_cors": re.compile(
                r"allow_origins\s*=\s*\[\s*['\"]\*['\"]\s*\]", re.IGNORECASE
            ),
            "weak_random": re.compile(
                r"\brandom\.(?:randint|random|choice|randrange)\b", re.IGNORECASE
            ),
        }

        self.explanations = {
            "hardcoded_secret": "CRITICAL: Hardcoded credentials detected. Use environment variables (dotenv) instead.",
            "weak_hash": "WARNING: Insecure hashing algorithm (MD5 or SHA-1) detected. Use hashlib.sha256 or bcrypt/argon2 instead.",
            "sql_injection": "CRITICAL: Potential SQL injection detected via string interpolation in database execution. Use parameterized queries.",
            "insecure_cors": "WARNING: Insecure CORS wildcard configuration ('*') detected. Specify explicit origins to avoid cross-origin exploitation.",
            "weak_random": "INFO: Standard pseudo-random generator detected. For cryptographic uses (e.g., token generation), use the 'secrets' module.",
        }

    def scan_file(self, file_path: str) -> List[Dict[str, any]]:
        vulnerabilities = []
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line_idx, line in enumerate(f, 1):
                    for rule_name, pattern in self.rules.items():
                        if pattern.search(line):
                            vulnerabilities.append(
                                {
                                    "file": os.path.basename(file_path),
                                    "line_number": line_idx,
                                    "line_content": line.strip(),
                                    "rule": rule_name,
                                    "description": self.explanations[rule_name],
                                }
                            )
        except Exception as e:
            vulnerabilities.append(
                {
                    "file": os.path.basename(file_path),
                    "line_number": 0,
                    "line_content": "",
                    "rule": "read_error",
                    "description": f"Failed to read file: {str(e)}",
                }
            )
        return vulnerabilities

    def scan_directory(self, dir_path: str) -> List[Dict[str, any]]:
        all_vulnerabilities = []
        for root, _, files in os.walk(dir_path):
            # Ignore hidden files, virtual environments and build directories
            if any(
                part in root
                for part in [
                    ".venv",
                    "venv",
                    "__pycache__",
                    ".git",
                    ".mypy_cache",
                    "build",
                ]
            ):
                continue
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    all_vulnerabilities.extend(self.scan_file(full_path))
        return all_vulnerabilities
