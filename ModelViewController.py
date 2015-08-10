from BalanceUpdater import BalanceUpdater
from DataGrabber import DataGrabber

class ModelViewController:
    def __init__(self):
        self.updater = BalanceUpdater()
        self.grabber = DataGrabber()
        
    def getStartingBalance(self):
        return self.updater.startingBalance
