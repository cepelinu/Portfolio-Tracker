from backend.src.api import *
import portfolio

class PortfolioFactory:
  """Factory pattern to return a Portfolio instance depending on the Broker API as input"""

  @staticmethod
  def build(broker):
    """
    Build a Portfolio instance using the Broker API

    Args:
      broker (object): The Broker API instance

    Returns:
      object: The Portfolio instance
    """
    name = broker.__class__.__name__

    if broker == "Trading212":
      return PortfolioFactory.build_trading212(broker)
    else:
      raise ValueError(f"Unknown broker api parameter: {broker}")

  @staticmethod
  def build_trading212(api_class : Trading212):
    """
    Build a Portfolio instance using the Trading212 API

    Args:
      api_class (object): The Trading212 API instance

    Returns:
      object: The Portfolio instance
    """
    def build_cash():
      cash_instance = portfolio.Cash()

      account_cash = api_class.fetch_account_cash()
      cash_instance.free = account_cash["blocked"]
      cash_instance.invested = account_cash["invested"]
      cash_instance.ppl = account_cash["ppl"]
      cash_instance.result = account_cash["result"]
      cash_instance.total = account_cash["total"]

      return cash_instance


    trading212_portfolio = portfolio.Portfolio()

    trading212_portfolio.Cash = build_cash()

    return trading212_portfolio