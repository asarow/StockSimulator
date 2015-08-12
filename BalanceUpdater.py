
class BalanceUpdater:
    def __init__(self):
        self.currentBalance = 100000.00
        self.portfolio = {} 

    def buyStock(self, stockPrice, amount, ticker):
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

    def getPortfolio(self):
        return self.portfolio

    def loadPortfolio(self, portFromFile):
        if "Balance" in portFromFile:
            self.currentBalance = portFromFile.get("Balance")
            del portFromFile["Balance"]

        self.portfolio = portFromFile

        
