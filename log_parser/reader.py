from typing import List, Generator
import os


def read_log_lines(file_path: str) -> Generator[str, None, None]:
    """Read log file line by line."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip('\n')


def read_log_file(file_path: str) -> List[str]:
    """Read entire log file into list of lines."""
    return list(read_log_lines(file_path))
