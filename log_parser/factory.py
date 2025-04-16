from typing import Type
from .report_base import BaseReport
from .report_handlers import HandlerReport

def get_report(name: str) -> BaseReport:
    """Factory function to get report instance by name."""
    if name == "handlers":
        return HandlerReport()
    raise ValueError(f"Unknown report type: {name}")

def create_report_handler(report_type: str) -> BaseReport:
    """Alias for get_report for backward compatibility."""
    return get_report(report_type)
