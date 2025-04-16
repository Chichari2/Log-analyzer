from log_parser.reader import read_log_lines, read_log_file
import pytest

def test_read_log_lines_parses_correctly(sample_log):
    log_data = list(read_log_lines(sample_log))
    assert isinstance(log_data, list)
    assert len(log_data) == 3
    assert "django.request" in log_data[0]

def test_read_log_file(sample_log):
    log_data = read_log_file(sample_log)
    assert isinstance(log_data, list)
    assert len(log_data) == 3

def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        list(read_log_lines("nonexistent.log"))
