import datetime
from dateutil import parser

class AbstractBase:
  """
  Abstract base class for portfolio factory builders.
  """

  # TODO: Make abstract builder classes for future brokers

class Base:
  """Inheritable methods"""
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