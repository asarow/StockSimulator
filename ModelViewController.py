from BalanceUpdater import BalanceUpdater
from DataGrabber import DataGrabber

class ModelViewController:
    def __init__(self):
        self.updater = BalanceUpdater()
        self.grabber = DataGrabber()
        
    def getStartingBalance(self):
        return self.updater.startingBalance

    def getCurrentBalance(self):
        return self.updater.currentBalance

    def grabLastTradePrice(self, ticker):
        return self.grabber.grabPrice(ticker)

    def buyStock(self, stockPrice, amount):
        self.updater.buyStock(stockPrice, amount)
        
