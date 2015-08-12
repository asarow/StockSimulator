from BalanceUpdater import BalanceUpdater
from DataGrabber import DataGrabber
import pickle

class Controller:
    def __init__(self):
        """Responsible for communication between the GUI and data classes.

        The BalanceUpdater and DataGrabber objects are initialized for use
        between their respective classes and the Controller class which is
        initialized as an object within the Window (GUI) class.
        """

        self.updater = BalanceUpdater()
        self.grabber = DataGrabber()

    def getCurrentBalance(self):
        return self.updater.currentBalance

    def grabLastTradePrice(self, ticker):
        return self.grabber.grabPrice(ticker)

    def buyStock(self, amount, ticker):
        """Purchases stock and updates the current balance and portfolio.

        The grabber object returns the current price of the stock to be
        purchased and passes it to the updater object to reflect the change
        in the current balance and the portfolio which holds the stock
        purchases.

        Args:
            amount: The amount of stock to be purchased.
            ticker: The stock ticker for the company.

        Return:
            Return true if the stock purchase and update was successful. False
            otherwise indicating not enough funds were available or the stock
            did not exist.
        """

        currentPrice = float(self.grabLastTradePrice(ticker))
        canBuy = self.updater.buyStock(currentPrice, amount, ticker)
        if canBuy == True:
            return True
        elif canBuy == False:
            return "Could not buy stock."
        
    def sellStock(self, amount, ticker):
        """Sells currently held stock of a given company and updates portfolio.

        The grabber object gets the current price of the stock and passes
        that information to the updater object to sell the stock at the
        most recent price. The updater object adjusts the current balance
        and portfolio to reflect the sale of the stock.

        Args:
            amount: The amount of stock to sell.
            ticker: The ticker symbol of the company.
        
        Return:
            Return true if the stock sale was successful, False otherwise
            indicating the stock did not exist in the portfolio or the amount
            requested to sell was more than what existed in the portfolio.
        """

        currentPrice = float(self.grabLastTradePrice(ticker))
        canSell = self.updater.sellStock(currentPrice, amount, ticker)
        if canSell == True:
            return True
        elif canSell == False:
            return "Could not sell stock."
            
    def saveData(self):
        """Saves the existing stock portfolio locally.

        When the user exits the program, the user will be prompted with a
        final exit screen. If the user exits, before termination, any existing
        stock within the portfolio is saved for the next run of the program.
        The portfolio is saved within the same directory as the program and
        can be deleted at any time.
        """
        self.updater.portfolio.update({"Balance":self.updater.currentBalance})
        pickle.dump(self.updater.portfolio, open("PortfolioData.txt", "wb"))
        
    def loadData(self):
        """Loads an existing stock portfolio.

        When the program is first opened, any pre-existing portfolio is loaded
        to allow the user to continue selling and buying stock. If an existing
        portfolio is not found, a new portfolio is created.
        
        Raises:
            IOError: An error occurred trying to access the portfolio data file.
            OSError: An error occured within the operating system when trying
                     to access the file.
        """
        
        try:
            portfolio = pickle.load(open("PortfolioData.txt", "rb"))
            if not portfolio:
                return
            else:
                self.updater.loadPortfolio(portfolio)
        except (OSError, IOError):
            pass

    def getPortfolioValue(self):
        """Returns the current value of the portfolio.

        The current portfolio is returned from the BalanceUpdater class. 
        If the portfolio is empty, a value of 0.00 is returned. Else if
        it is not empty, the DataGrabber class updates the current values
        of the portfolio by accessing the current stock prices, calculates
        the total value of the portfolio and returns it.

        Returns:
            The total value of the portfolio is returned.
        """
        totalValue = 0
        currentPortfolio = self.updater.portfolio
        if not currentPortfolio:
            return totalValue

        for key in currentPortfolio:
            totalValue += self.grabLastTradePrice(key) * currentPortfolio[key]

        return "{:.2f}".format(totalValue)
