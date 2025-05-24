from api.Trading212 import Trading212
from models.portfolio_factory.trading212_builder import Trading212PortfolioFactory


class PortfolioFactory:
  """Factory pattern to return a Portfolio instance depending on the Broker API as input"""

  @staticmethod
  def build(broker_api):
    """
    Build a Portfolio instance using the Broker API

    Args:
      broker_api (object): The Broker API instance

    Returns:
      object: The Portfolio instance

    Raises:
      ValueError: If the Broker API is not valid
    """
    if isinstance(broker_api, Trading212.__class__):
      return Trading212PortfolioFactory.build(broker_api)
    else:
      raise ValueError(f"Unknown broker api parameter: {broker_api}")


