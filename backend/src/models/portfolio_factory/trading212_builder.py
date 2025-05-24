from models import portfolio
from models.portfolio_factory.base import *

class Trading212PortfolioFactory(Base):

  @staticmethod
  def build(trading212_api):
    """
        Build a Portfolio instance using the Trading212 API

        Args:
          trading212_api (Trading212): The Trading212 API instance

        Returns:
          object: The Portfolio instance
        """
    trading212_portfolio = portfolio.Portfolio()

    trading212_portfolio.Cash = Trading212PortfolioFactory.build_cash(trading212_api)
    trading212_portfolio.Stocks = Trading212PortfolioFactory.build_stocks(trading212_api)

    return trading212_portfolio

  @staticmethod
  def build_cash(trading212_api):
    cash_instance = portfolio.Cash()

    account_cash = trading212_api.fetch_account_cash()
    cash_instance.free = account_cash["free"]
    cash_instance.invested = account_cash["invested"]
    cash_instance.ppl = account_cash["ppl"]
    cash_instance.result = account_cash["result"]
    cash_instance.total = account_cash["total"]

    return cash_instance

  @staticmethod
  def build_stocks(trading212_api):
    stocks_instance = portfolio.Stocks()
    total_holdings = trading212_api.fetch_all_open_positions()

    for holding in total_holdings:
      # [
      #       "average_price",
      #       "forex_ppl",
      #       "initial_buy_date",
      #       "ppl",
      #       "quantity",
      #       "ticker"
      #     ]
      timestamp = holding["initialFillDate"]
      initial_fill_date = Base.format_timestamp_to_utc_iso(timestamp)

      row = [
        holding["averagePrice"],
        holding["fxPpl"],
        holding["initialFillDate"],
        initial_fill_date,
        holding["ppl"],
        holding["quantity"],
        holding["ticker"]
      ]

      stocks_instance.holdings.loc[len(stocks_instance.holdings)] = row

    return stocks_instance