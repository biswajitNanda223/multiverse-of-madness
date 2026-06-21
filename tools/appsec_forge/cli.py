import argparse
import os
import sys

from .generator import SecurityTemplateGenerator
from .scanner import SecurityScanner
from .threat_model import STRIDEThreatModeler


def main() -> None:
    parser = argparse.ArgumentParser(
        description="SecureForge 2026: Tool to build and audit cyber secure applications."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available actions")

    # Scan command
    scan_parser = subparsers.add_parser("scan", help="Scan code for security vulnerabilities")
    scan_parser.add_argument(
        "--path", required=True, help="Path to Python file or directory to scan"
    )

    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate secure boilerplate template")
    gen_parser.add_argument(
        "--output", required=True, help="Directory to save the secure boilerplate"
    )

    # Threat command
    threat_parser = subparsers.add_parser("threat", help="Generate STRIDE Threat Model")
    threat_parser.add_argument(
        "--type", default="web", help="Application type (web, microservice, mobile)"
    )
    threat_parser.add_argument(
        "--output",
        default="threat_model.md",
        help="Filename to save the markdown model",
    )

    args = parser.parse_args()

    if args.command == "scan":
        scanner = SecurityScanner()
        target = args.path
        if os.path.isdir(target):
            results = scanner.scan_directory(target)
        else:
            results = scanner.scan_file(target)

        if not results:
            print(f"✅ No vulnerabilities detected in: {target}")
            sys.exit(0)

        print(f"⚠️ Detected {len(results)} vulnerabilities/alerts:")
        for idx, alert in enumerate(results, 1):
            print(f"--- Alert #{idx} ---")
            print(f"File: {alert['file']}:{alert['line_number']}")
            print(f"Type: {alert['rule']}")
            print(f"Details: {alert['description']}")
            if alert["line_content"]:
                print(f"Code: {alert['line_content']}")
        sys.exit(1)

    elif args.command == "generate":
        res = SecurityTemplateGenerator.generate_boilerplate(args.output)
        print(res)

    elif args.command == "threat":
        model_md = STRIDEThreatModeler.generate_stride_model(args.type)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(model_md)
        print(f"✅ Generated STRIDE threat model saved to: {args.output}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
