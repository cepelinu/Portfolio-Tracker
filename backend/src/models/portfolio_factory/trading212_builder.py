from backend.src.models import portfolio
from backend.src.api.Trading212 import Trading212

class Trading212PortfolioFactory:

  @staticmethod
  def build(trading212_api):
    """
        Build a Portfolio instance using the Trading212 API

        Args:
          trading212_api (Trading212): The Trading212 API instance

        Returns:
          object: The Portfolio instance
        """

    def build_cash():
      cash_instance = portfolio.Cash()

      account_cash = trading212_api.fetch_account_cash()
      cash_instance.free = account_cash["blocked"]
      cash_instance.invested = account_cash["invested"]
      cash_instance.ppl = account_cash["ppl"]
      cash_instance.result = account_cash["result"]
      cash_instance.total = account_cash["total"]

      return cash_instance

    def build_stocks():
      stocks_instance = portfolio.Stocks()

      # TODO: Retrieve and generalise stock data

      return stocks_instance

    trading212_portfolio = portfolio.Portfolio()

    trading212_portfolio.Cash = build_cash()
    trading212_portfolio.Stocks = build_stocks()

    return trading212_portfolio