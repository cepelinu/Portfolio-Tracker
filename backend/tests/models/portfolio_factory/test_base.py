import pytest
from models.portfolio_factory import base

class DummyBroker:
  pass

def test_invalid_broker_name():
  with pytest.raises(ValueError):
    base.PortfolioFactory.build(DummyBroker())

def test_format_timestamp_to_utc_iso():
  test_cases = {
    "2025-05-24T12:30:00Z": "2025-05-24T12:30:00Z",       # ISO format with Z
    "2025-05-24T12:30:00+00:00": "2025-05-24T12:30:00Z",  # ISO format with +00:00
    "2025-05-24T12:30:00": "2025-05-24T12:30:00Z",        # ISO format without timezone
    "2025-05-24T12:30:00+02:00": "2025-05-24T10:30:00Z",  # ISO format with timezone offset
    #"1598323200": "2020-08-26T00:00:00Z",                 # UNIX timestamp since epoch
    "24-05-2025 12:30:00": "2025-05-24T12:30:00Z",        # Custom format DD-MM-YYYY HH:MM:SS
    "May 24, 2025 12:30:00 PM": "2025-05-24T12:30:00Z",   # Month Day, Year, HH:MM:SS AM/PM
    "24 May 2025 12:30:00": "2025-05-24T12:30:00Z"        # DD Month YYYY HH:MM:SS
  }

  for original, expected in test_cases.items():
    convert = base.PortfolioFactory.format_timestamp_to_utc_iso(original)
    assert convert == expected
