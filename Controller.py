from BalanceUpdater import BalanceUpdater
from DataGrabber import DataGrabber

class Controller:
    def __init__(self):
        self.updater = BalanceUpdater()
        self.grabber = DataGrabber()
        
    def getStartingBalance(self):
        return self.updater.startingBalance

    def getCurrentBalance(self):
        return self.updater.currentBalance

    def grabLastTradePrice(self, ticker):
        return self.grabber.grabPrice(ticker)

    def buyStock(self, stockPrice, amount, ticker):
        canBuy = self.updater.buyStock(stockPrice, amount, ticker)
        if canBuy == True:
            return True
        elif canBuy == False:
            return "Could not buy stock."
        
            
    def getPortfolio(self):
        return self.updater.getPortfolio()
