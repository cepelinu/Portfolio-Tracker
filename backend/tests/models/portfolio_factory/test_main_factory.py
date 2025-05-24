import pytest
from models.portfolio_factory import main_factory

class DummyBroker:
  pass

def test_invalid_broker_name():
  with pytest.raises(ValueError):
    main_factory.PortfolioFactory.build(DummyBroker())