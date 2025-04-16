from typing import List, Dict, DefaultDict
import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import os
from .reader import read_log_lines
from .report_base import BaseReport

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
LOG_PATTERN = re.compile(
    r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+"
    r"\d{4}-\d{2}-\d{2} [\d:,]+\s+"
    r".*?django\.request.*?\"[A-Z]+\s+"
    r"(?P<path>/[^\s\"]+)"
)


class HandlerReport(BaseReport):
    """Report handler for API endpoint statistics by log level."""

    def __init__(self) -> None:
        self.data: DefaultDict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self.total = 0

    def _process_file(self, file_path: str) -> Dict[str, Dict[str, int]]:
        """Process single log file and return statistics."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        file_data: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))

        for line in read_log_lines(file_path):
            match = LOG_PATTERN.search(line)
            if match:
                level = match.group("level")
                path = match.group("path")
                file_data[path][level] += 1

        return file_data

    def process(self, file_paths: List[str]) -> None:
        """Process multiple log files in parallel."""
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(self._process_file, file_paths))

        # Merge results
        for result in results:
            for path, levels in result.items():
                for level, count in levels.items():
                    self.data[path][level] += count
                    self.total += count

    def print(self) -> None:
        """Print formatted report to stdout."""
        if not self.data:
            print("No data to display")
            return

        # Prepare data
        handlers = sorted(self.data.keys())
        total_levels = {level: 0 for level in LOG_LEVELS}

        # Calculate column widths
        handler_width = max(len(h) for h in handlers) if handlers else 8
        handler_width = max(handler_width, len("HANDLER"))

        level_widths = [max(len(l), 7) for l in LOG_LEVELS]

        # Print header
        header = f"{'HANDLER':<{handler_width}}"
        for i, level in enumerate(LOG_LEVELS):
            header += f"  {level:<{level_widths[i]}}"
        print(f"\nTotal requests: {self.total}\n")
        print(header)

        # Print rows
        for handler in handlers:
            row = f"{handler:<{handler_width}}"
            for i, level in enumerate(LOG_LEVELS):
                count = self.data[handler].get(level, 0)
                row += f"  {count:<{level_widths[i]}}"
                total_levels[level] += count
            print(row)

        # Print totals
        totals_row = f"{'':<{handler_width}}"
        for i, level in enumerate(LOG_LEVELS):
            totals_row += f"  {total_levels[level]:<{level_widths[i]}}"
        print(totals_row)

