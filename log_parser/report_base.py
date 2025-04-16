from abc import ABC, abstractmethod
from typing import List


class BaseReport(ABC):
  """Abstract base class for all report types."""

  @abstractmethod
  def process(self, file_paths: List[str]) -> None:
    """Process log files and collect data for report."""
    pass

  @abstractmethod
  def print(self) -> None:
    """Print the report to stdout."""
    pass