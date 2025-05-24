import pytest
from models.portfolio_factory import base

class DummyBroker:
  pass

def test_invalid_broker_name():
  with pytest.raises(ValueError):
    base.PortfolioFactory.build(DummyBroker())