import pandas

class Portfolio:
  """Class representing an investment account portfolio"""

  def __init__(self):
    self.Cash = Portfolio.Cash
    self.Stocks = Portfolio.Stocks

  class Cash:
    free = 0     # Free funds
    invested = 0 # Total amount invested before ppl
    ppl = 0      # Unrealised gains or losses
    result = 0   # Realised ppl
    total = 0    # Total amount value

  class Stocks:
    holdings = pandas.DataFrame()

