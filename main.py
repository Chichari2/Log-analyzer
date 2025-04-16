import argparse
import sys
import os
from typing import List
from log_parser.factory import get_report


def validate_files(file_paths: List[str]) -> List[str]:
  """Validate that all files exist."""
  valid_files = []
  for path in file_paths:
    if not os.path.isfile(path):
      print(f"Error: File not found - {path}", file=sys.stderr)
      sys.exit(1)
    valid_files.append(path)
  return valid_files


def main() -> None:
  """Main entry point for the log analyzer CLI."""
  parser = argparse.ArgumentParser(
    description="Django Log Analyzer - Generate reports from Django request logs"
  )
  parser.add_argument(
    "log_files",
    nargs="+",
    help="Paths to log files to analyze"
  )
  parser.add_argument(
    "--report",
    required=True,
    choices=["handlers"],
    help="Type of report to generate"
  )

  args = parser.parse_args()

  try:
    files = validate_files(args.log_files)
    report = get_report(args.report)
    report.process(files)
    report.print()
  except Exception as e:
    print(f"Error: {str(e)}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
  main()