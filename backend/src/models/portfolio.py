import pandas

class Portfolio:
  """Class representing an investment account portfolio"""

  def __init__(self):
    Cash = None
    Stocks = None

class Cash:
  """Class representing the cash assets and information of a portfolio"""

  def __init__(self):
    free = 0     # Free funds
    invested = 0 # Total amount invested before ppl
    ppl = 0      # Unrealised gains or losses
    result = 0   # Realised ppl
    total = 0    # Total amount value

class Stocks:
  """Class representing all holdings in a portfolio"""

  def __init__(self):
    holdings = pandas.DataFrame()

