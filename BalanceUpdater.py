
class BalanceUpdater:
    def __init__(self):
        """Initializes the current balance and portfolio.

        The current balance by default is set to $100,000.00 and is
        modified if there is an existing portfolio. The portfolio
        represents the current stock purchases by ticker and amount.
        """
        self.currentBalance = 100000.00
        self.portfolio = {} 

    def buyStock(self, stockPrice, amount, ticker):
        """Purchases the stock of a given public company.

        Total price of the stock purchase is caclulated and then compared
        to the current balance to ensure enough funds are available. If
        so, the stock ticker and stock amount purchased is stored into
        a dictionary which represents the stock portfolio. The current
        balance is then updated to reflect the purchase.

        Args:
            stockPrice: The current stock price of the given ticker.
            amount: The amount of stock to be purchased.
            ticker: The ticker symbol of the public company.

        Returns:
            If the stock purchase is successful, True is returned. Else
            False to indicate the stock purchase was not successful.
        """
        calcPrice = stockPrice * amount
        if self.currentBalance >= calcPrice:
            if ticker in self.portfolio:
                newAmount = self.portfolio.get(ticker) + amount
                self.portfolio.update({ticker:newAmount})
            else:
                self.portfolio.update({ticker:amount})
            self.currentBalance -= calcPrice
            return True
        else:
            return False
        
    def sellStock(self, stockPrice, amount, ticker):
        """Sells the stock of a given public company from the portfolio.

        The total sale-price is calculated from the current stock price
        and amount requested to sell. If the stock exists in the portfolio,
        and the amount requested for sale is less than the current amount
        in the portfolio, the sale goes through, the portfolio is updated,
        and the current balance is changed to reflect the sale. If the
        amount requested to sell is equal to the amount in the portfolio,
        the stock is completely removed from the portfolio. Else if the 
        amount requested for sale is greater than the amount existing in
        the portfolio, the sale does not go through.

        Args:
            stockPrice: The current stock price of the ticker.
            amount: The amount of stock requested to sell.
            ticker: The ticker symbol of the public company.
        
        Return:
            If the stock sale is succesful, True is returned. Else, False
            is returned to indicate the sale was not successful.
        """
        
        calcPrice = stockPrice * amount
        if ticker in self.portfolio:
            currentAmount = self.portfolio.get(ticker)
            if currentAmount > amount:
                newAmount = currentAmount - amount
                self.portfolio.update({ticker:newAmount})
            elif currentAmount == amount:
                del self.portfolio[ticker]
            else:
                return False
            self.currentBalance += calcPrice
            return True
        else:
            return False

    def loadPortfolio(self, portFromFile):
        """Loads the portfolio from the controller

        The Controller class loads a file containing an existing stock
        portfolio and requests this portfolio to be updated inside the
        BalanceUpdater class. The current balance is updated and the
        stock portfolio is loaded into the current portfolio.

        Args:
            portFromFile: An existing stock portfolio.
        """

        if "Balance" in portFromFile:
            self.currentBalance = portFromFile.get("Balance")
            del portFromFile["Balance"]

        self.portfolio = portFromFile

        
