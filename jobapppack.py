#!/usr/bin/env python3
"""
jobapppack.py - Create a job application package folder with templated files.

Usage:
    jobapppack.py <company_name>

Example:
    jobapppack.py Google
    → creates folder "Google" with:
        creelhenry_resume_Google.md
        creelhenry_coverletter_Google.md
        creelhenry_summaryreport_Google.md
"""

import sys
import os
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: jobapppack.py <company_name>", file=sys.stderr)
        sys.exit(1)

    company = sys.argv[1].strip()
    if not company:
        print("Error: company name cannot be empty", file=sys.stderr)
        sys.exit(1)

    # Create the folder
    folder = Path(company)
    folder.mkdir(exist_ok=True)
    print(f"Created folder: {folder}")

    # Common base name (updated to match project theme)
    base = "creelhenry"

    # File definitions: (filename_suffix, initial_content) - updated to use project templates
    files = [
        (f"resume_{company}.md",         "# Resume for " + company + "\n\n[Content based on resume_template_CreelHenry.md]"),
        (f"coverletter_{company}.md",    "# Cover Letter for " + company + "\n\n[Content based on coverletter_template_CreelHenry.md]"),
        (f"summaryreport_{company}.md", "# Summary Report - " + company + "\n\n[Content based on prompts/Review_Actions_in_FULLAUDITMODE.md]"),
    ]

    for suffix, content in files:
        filepath = folder / f"{base}_{suffix}"
        if not filepath.exists():
            filepath.write_text(content + "\n", encoding="utf-8")
            print(f"  Created {filepath.name}")
        else:
            print(f"  Already exists: {filepath.name}")

if __name__ == "__main__":
    main()