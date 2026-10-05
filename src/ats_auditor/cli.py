from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

from .core import save_report, scan_resume


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Audit a resume locally for ATS parseability and job-specific keyword coverage.")
    result.add_argument("--resume", required=True, type=Path)
    job_source = result.add_mutually_exclusive_group()
    job_source.add_argument("--job-description", type=Path)
    job_source.add_argument("--job-id", type=int, help="Load a job description from the local application ledger.")
    result.add_argument("--ledger", type=Path, help="SQLite ledger used with --job-id.")
    result.add_argument("--json", dest="json_path", type=Path)
    result.add_argument("--markdown", dest="markdown_path", type=Path)
    result.add_argument("--strict", action="store_true", help="Return a nonzero exit code when high-severity findings exist.")
    return result


def main() -> int:
    args = parser().parse_args()
    if args.job_id is not None and args.ledger is None:
        raise SystemExit("--ledger is required when --job-id is used")

    if args.job_description:
        job_text = args.job_description.read_text(encoding="utf-8")
    elif args.job_id is not None:
        with sqlite3.connect(args.ledger) as connection:
            row = connection.execute(
                "SELECT description FROM jobs WHERE job_id = ?", (args.job_id,)
            ).fetchone()
        if row is None:
            raise SystemExit(f"job ID {args.job_id} was not found in {args.ledger}")
        job_text = row[0]
    else:
        job_text = None
    report = scan_resume(args.resume, job_text=job_text)
    save_report(report, args.json_path, args.markdown_path)
    print(f"Structural readiness: {report.structural_readiness_score}/{report.structural_readiness_max}")
    if report.job_match_score is not None:
        print(f"Job match: {report.job_match_score}/20")
        print(f"Combined diagnostic: {report.overall_score}/100")
    for finding in report.findings:
        print(f"[{finding.severity.upper()}] {finding.message}")
    if args.strict and any(item.severity == "high" for item in report.findings):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
