
class BalanceUpdater:
    def __init__(self):
        self.startingBalance = 100000.00
        self.currentBalance = 100000.00
        self.portfolio = {}

    def buyStock(self, stockPrice, amount, ticker):
        calcPrice = stockPrice * amount
        if self.currentBalance >= calcPrice:
            if ticker in self.portfolio:
                updatedPrice = self.portfolio.get(ticker) + calcPrice
                self.portfolio.update({ticker:updatedPrice})
            else:
                self.portfolio.update({ticker:calcPrice})
            self.currentBalance -= calcPrice
            return True
        else:
            return False
        
    def sellStock(self, stockPrice, amount, ticker):
        calcPrice = stockPrice * amount
        if ticker in self.portfolio:
            currentVal = self.portfolio.get(ticker)
            if currentVal > calcPrice:
                newPrice = currentVal - calcPrice
                self.portfolio.update({ticker:newPrice})
            elif currentVal <= calcPrice:
                del self.portfolio[ticker]
            self.currentBalance += calcPrice
            return True
        else:
            return False

    def getPortfolio(self):
        return self.portfolio
        
