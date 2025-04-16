from log_parser.factory import create_report_handler, get_report
from log_parser.report_handlers import HandlerReport

def test_create_report_handler():
    handler = create_report_handler("handlers")
    assert isinstance(handler, HandlerReport)

def test_get_report():
    handler = get_report("handlers")
    assert isinstance(handler, HandlerReport)

def test_invalid_report_type():
    import pytest
    with pytest.raises(ValueError):
        get_report("invalid_type")


