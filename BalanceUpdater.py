
class BalanceUpdater:
    def __init__(self):
        self.startingBalance = 100000.00
        self.currentBalance = 100000.00
        self.portfolio = []

    def buyStock(self, stockPrice, amount, ticker):
        calcPrice = stockPrice * amount
        if self.currentBalance >= calcPrice:
            self.portfolio.append(ticker)
            self.currentBalance -= calcPrice
            return True
        else:
            return False
        
    def sellStock(self, stockPrice, amount):
        pass

        
