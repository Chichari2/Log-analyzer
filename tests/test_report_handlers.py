import pytest
from log_parser.report_handlers import HandlerReport, LOG_LEVELS


def test_handlers_report(sample_log):
    report = HandlerReport()
    report.process([sample_log])

    assert "/api/v1/products/" in report.data
    assert report.data["/api/v1/products/"]["DEBUG"] == 1
    assert report.data["/api/v1/products/"]["INFO"] == 1
    assert report.data["/api/v1/products/"]["ERROR"] == 1
    assert report.total == 3


def test_empty_log_file(empty_log):
    report = HandlerReport()
    report.process([empty_log])
    assert report.total == 0


def test_multiple_log_files(sample_log, empty_log):
    report = HandlerReport()
    report.process([sample_log, empty_log])
    assert report.total == 3


def test_file_not_found():
    report = HandlerReport()
    with pytest.raises(FileNotFoundError):
        report.process(["nonexistent.log"])


def test_print_report(capsys, sample_log):
    report = HandlerReport()
    report.process([sample_log])
    report.print()

    captured = capsys.readouterr()
    assert "Total requests: 3" in captured.out
    assert "/api/v1/products/" in captured.out
    for level in LOG_LEVELS:
        assert level in captured.out
