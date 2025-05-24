from api import *
import datetime
from dateutil import parser
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
    if isinstance(broker_api, Trading212):
      return Trading212PortfolioFactory.build(broker_api)
    else:
      raise ValueError(f"Unknown broker api parameter: {broker_api}")

  @staticmethod
  def format_timestamp_to_utc_iso(timestamp):
    """
    Parse a timestamp string into a readable datetime string.

    Args:
      timestamp (str): A timestamp string.

    Returns:
      str: The formatted timestamp string into ISO 8601 format with Z sign.

    Raises:
      ValueError: Unrecognised timestamp format.
    """

    # FIXME: Doesn't recognise UNIX format
    try:
      timestamp_datetime = parser.parse(timestamp)
    except ValueError:
      raise ValueError(f"Unrecognised timestamp format: {timestamp}")

    if timestamp_datetime.tzinfo is None:
      # If no timezone is supplied, assume UTC
      timestamp_datetime = timestamp_datetime.replace(tzinfo=datetime.timezone.utc)
    else:
      timestamp_datetime = timestamp_datetime.astimezone(datetime.timezone.utc)

    return timestamp_datetime.isoformat().replace("+00:00", "Z")


