from BalanceUpdater import BalanceUpdater
from DataGrabber import DataGrabber
import pickle

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

    def buyStock(self, amount, ticker):
        currentPrice = float(self.grabLastTradePrice(ticker))
        canBuy = self.updater.buyStock(currentPrice, amount, ticker)
        if canBuy == True:
            return True
        elif canBuy == False:
            return "Could not buy stock."
        
    def sellStock(self, amount, ticker):
        currentPrice = float(self.grabLastTradePrice(ticker))
        canSell = self.updater.sellStock(currentPrice, amount, ticker)
        if canSell == True:
            return True
        elif canSell == False:
            return "Could not sell stock."
            
    def getPortfolio(self):
        return self.updater.getPortfolio()
        
    def saveData(self):
        self.updater.getPortfolio().update(
            {"Balance":self.updater.currentBalance})

        pickle.dump(self.updater.getPortfolio(),
                    open("PortfolioData.txt", "wb"))
        
    def loadData(self):
        try:
            portfolio = pickle.load(open("PortfolioData.txt", "rb"))
            if not portfolio:
                return
            else:
                self.updater.loadPortfolio(portfolio)
        except (OSError, IOError):
            pass

    def getPortfolioValue(self):
        totalValue = 0
        currentPortfolio = self.updater.getPortfolio()
        if not currentPortfolio:
            return totalValue

        for key in currentPortfolio:
            totalValue += self.grabLastTradePrice(key) * currentPortfolio[key]

        return "{:.2f}".format(totalValue)
