
class BalanceUpdater:
    def __init__(self):
        self.startingBalance = 100000.00
        self.currentBalance = 100000.00
    
    def buyStock(self, stockPrice, amount):
        calcPrice = stockPrice * amount
        self.currentBalance -= calcPrice
        
        
    def sellStock(self, stockPrice, amount):
        pass

        
