import pytest
from unittest.mock import patch
from api import *
from models import portfolio
from models.portfolio_factory.trading212_builder import Trading212PortfolioFactory


# Mock responses
# These do not need to be mathematically correct
# as we are not calculating any additional data
def mock_fetch_account_cash():
  return {
      "blocked": 2000,
      "free": 1500,
      "invested": 1250,
      "pieCash": 0,
      "ppl": 260,
      "result": 100,
      "total": 5000
  }

def mock_fetch_all_open_positions():
  return [
  {
    "averagePrice": 0,
    "currentPrice": 0,
    "frontend": "API",
    "fxPpl": 0,
    "initialFillDate": "2019-08-24T14:15:22Z",
    "maxBuy": 0,
    "maxSell": 0,
    "pieQuantity": 0,
    "ppl": 0,
    "quantity": 0,
    "ticker": "AAPL_US_EQ"
  }
]

@pytest.fixture
def mock_trading212_api():
  trading212 = Trading212("dummy")
  return trading212

@patch.object(Trading212, "fetch_account_cash", return_value=mock_fetch_account_cash())
def test_trading212_cash_instance(mock_get, mock_trading212_api):
  trading212_cash_portfolio = Trading212PortfolioFactory.build_cash(mock_trading212_api)

  assert isinstance(trading212_cash_portfolio, portfolio.Cash)

  for key, value in trading212_cash_portfolio.to_json().items():
    assert mock_fetch_account_cash()[key] == getattr(trading212_cash_portfolio, key)

@patch.object(Trading212, "fetch_all_open_positions", return_value=mock_fetch_all_open_positions())
def test_trading212_stock_instance(mock_get, mock_trading212_api):
  trading212_stock_instance = Trading212PortfolioFactory.build_stocks(mock_trading212_api)


