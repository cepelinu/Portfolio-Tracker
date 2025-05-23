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
      pass
    else:
      raise ValueError(f"Unknown broker api parameter: {broker}")