import argparse
from pathlib import Path
from git_utils import get_changed_files, get_file_diff
from openai_client import review_code
from prompt_builder import build_prompt
import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_review(repo_path):
    print("Scanning repository:", repo_path)

    changed_files = get_changed_files(repo_path)
    if not changed_files:
        print("No changed files found")
        return

    report_lines = ["# AI Code Review Report\n"]

    for file_path in changed_files:
        print("Reviewing:", file_path)
        diff = get_file_diff(repo_path, file_path)
        if not diff.strip():
            continue

        prompt = build_prompt(file_path, diff)

        try:
            review = review_code(prompt)
        except Exception as e:
            review = f"ERROR: {str(e)}"

        report_lines.append(f"\n---\n## {file_path}\n")
        report_lines.append(review)

        Path("review_report.md").write_text("\n".join(report_lines), encoding="utf-8")

    print("Review report generated: review_report.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo_path", required=True)
    args = parser.parse_args()
    run_review(args.repo_path)
