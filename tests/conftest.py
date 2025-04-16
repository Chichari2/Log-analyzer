import pytest
from typing import Generator
from pathlib import Path

@pytest.fixture
def sample_log(tmp_path: Path) -> str:
    log = tmp_path / "sample.log"
    log.write_text("""DEBUG 2024-04-16 10:00:00,000 django.request "GET /api/v1/products/" 200
INFO 2024-04-16 10:01:00,000 django.request "GET /api/v1/products/" 200
ERROR 2024-04-16 10:02:00,000 django.request "GET /api/v1/products/" 500
""")
    return str(log)

@pytest.fixture
def empty_log(tmp_path: Path) -> str:
    log = tmp_path / "empty.log"
    log.write_text("")
    return str(log)