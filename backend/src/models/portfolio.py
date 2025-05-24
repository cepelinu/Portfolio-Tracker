import pandas

class Portfolio:
  """Class representing an investment account portfolio"""

  def __init__(self):
    self.Cash = None
    self.Stocks = None

class Cash:
  """Class representing the cash assets and information of a portfolio"""

  def __init__(self):
    self.free = 0     # Free funds
    self.invested = 0 # Total amount invested before ppl
    self.ppl = 0      # Unrealised gains or losses
    self.result = 0   # Realised ppl
    self.total = 0    # Total amount value

  def to_json(self):
    return {
      "free": self.free,
      "invested": self.invested,
      "ppl": self.ppl,
      "result": self.result,
      "total": self.total
    }

class Stocks:
  """Class representing all holdings in a portfolio"""

  def __init__(self):
    self.holdings = pandas.DataFrame()

  def to_json(self):
    return self.holdings.to_json()

