import datetime
from datetime import timezone

import requests

class Trading212:
  """
  Class representing unabstracted api endpoints available from Trading212.

  Only the live version is supported.

  Attributes:
    BASE_URL (str): The base url.
    api_key (str): The api key.
  """
  BASE_URL = "https://live.trading212.com"

  EPOCH_ISO8601 = "1970-01-01T00:00:00Z"

  def __init__(self, api_key = ""):
    self.api_key = api_key

  @staticmethod
  def get_current_iso8601_utc():
    return datetime.datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

  # Instruments Metadata
  def exchange_list(self):
    return self.requests("GET", "/api/v0/equity/metadata/exchanges")

  def instruments_list(self):
    return self.requests("GET", "/api/v0/equity/metadata/instruments")

  # Pies
  def fetch_all_pies(self):
    return self.requests("GET", "/api/v0/equity/pies")

  # Equity Orders
  def fetch_all(self):
    return self.requests("GET", "/api/v0/equity/orders")

  def fetch_by_id(self, id):
    return self.requests("GET", "/api/v0/equity/orders/{id}")

  # Account Data
  def fetch_account_cash(self):
    return self.requests("GET", "/api/v0/equity/account/cash")

  def fetch_account_metadata(self):
    return self.requests("GET", "/api/v0/equity/account/info")

  # Personal Portfolio
  def fetch_all_open_positions(self):
    return self.requests("GET", "/api/v0/equity/portfolio")

  def search_for_a_specific_position_by_ticker(self, ticker):
    return self.requests("POST", f"/api/v0/equity/portfolio/{ticker}")

  def fetch_a_specific_position(self, ticker):
    return self.requests("GET", f"/api/v0/equity/portfolio/{ticker}")

  # Historical Items
  def historical_order_data(self, cursor = 0, ticker = "", limit = 50):
    if not (0 >= limit >= 50): raise ValueError("Limit must be between 0 and 50 inclusive")

    query = {
      "cursor": cursor,
      "ticker": ticker,
      "limit": limit
    }

    return self.requests("GET", "/api/v0/equity/history/orders", query)

  def paid_out_dividends(self, cursor = 0, ticker = "", limit = 50):
    if not (0 >= limit >= 50): raise ValueError("Limit must be between 0 and 50 inclusive")

    query = {
      "cursor": cursor,
      "ticker": ticker,
      "limit": limit
    }

    return self.requests("GET", "/api/v0/history/dividends", query)

  def exports_list(self):
    return self.requests("GET", "/api/v0/history/exports")

  def export_csv(
      self,
      include_dividends = True,
      include_interest = True,
      include_orders = True,
      include_transactions = True,
      time_from = 0,
      time_to = 0
  ):
    if time_from is None:
      time_from = self.EPOCH_ISO8601

    if time_to is None:
      time_to = Trading212.get_current_iso8601_utc()

    payload = {
      "dataIncluded": {
        "includeDividends": include_dividends,
        "includeInterest": include_interest,
        "includeOrders": include_orders,
        "includeTransactions": include_transactions,
      },
      "timeFrom": time_from,
      "timeTo": time_to
    }

    return self.requests("POST", "/api/v0/history/exports", payload)

  def transaction_list(self, cursor = 0, time = None, limit = 50):
    if not (0 <= limit <= 50): raise ValueError("Limit must be between 0 and 50 inclusive")

    if time is None:
      time = self.EPOCH_ISO8601

    query = {
      "cursor": cursor,
      "time": time,
      "limit": limit
    }

    return self.requests("GET", "/api/v0/history/transactions", query)

  def requests(self, method, path, params = None):
    """

    Args:
      method (str): The HTTP request method.
      path (str): The API
      params (any): Optional parameters to be passed alongside the request, default is None.

    Returns:
      dict: The json response.

    Raises:
      HTTPException: If the request fails.
    """

    url = self.BASE_URL + path

    headers = {
      "Content-Type": "application/json",
      "Authorization": self.api_key
    }

    if method == "GET":
      response = requests.get(url, headers=headers, params=params)
    elif method == "POST":
      response = requests.post(url, headers=headers, json=params)
    else:
      raise ValueError(f"Invalid HTTP method: {method}")

    response.raise_for_status()
    return response.json()