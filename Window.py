from tkinter import *
from ModelViewController import ModelViewController

class Window:
    def __init__(self):
        self.mvc = ModelViewController()
        root = Tk()
        root.wm_title("Stock simulator v1.0")
        root.minsize(width=500, height=500)
        self.stockPrice = IntVar()
        self.currentBal = IntVar()
        self.error = StringVar()
        self.currentBal.set(self.mvc.getCurrentBalance())
        self.portfolio = StringVar()

        self.displayLabel = Label(root, text="Enter a ticker: ")
        self.searchBar = Entry(root)
        self.searchButton = Button(root, text="Go", command=lambda: 
                                   self.checkData())
                   
        self.buyButton = Button(root, text="Buy", state=DISABLED,
                                command=lambda: self.buyStock())
        self.stockAmountBar = Entry(root)
        self.balanceLabel = Label(root, text="Current balance: ")
        self.balanceAmount = Label(root, textvariable=self.currentBal)
        self.tickerDisplay = Label(root, text="Ticker price ")
        self.tickerPrice = Label(root, textvariable=self.stockPrice)
        self.errorLabel = Label(root, textvariable=self.error)
        self.viewPortfolio = Button(root, text="View Portfilio", 
                                    command=lambda: self.getPortfolio())
        self.viewPortfolioLabel = Label(root, textvariable=self.portfolio)
        self.displayLabel.grid(row=0, column=0)
        self.searchBar.grid(row=0, column=1)
        self.searchButton.grid(row=0, column=2)
        self.balanceLabel.grid(row=1, column=0)
        self.balanceAmount.grid(row=1, column=1)
        self.tickerDisplay.grid(row=2, column=0)
        self.tickerPrice.grid(row=2, column=1)
        self.stockAmountBar.grid(row=2, column=2)
        self.buyButton.grid(row=2, column=3)
        self.errorLabel.grid(row=3, column=0)
        self.viewPortfolio.grid(row=4, column=3)
        self.viewPortfolioLabel.grid(row=4, column=2)
        root.mainloop()

    def checkData(self):
        if self.unlockButton() == True:
            self.pullData()
            
        
    def unlockButton(self):
        ticker = self.searchBar.get()
        if not ticker:
            self.error.set("Enter a valid ticker.")
            self.buyButton['state'] = 'disabled'
            return False
        else:
            self.error.set("")
            self.buyButton['state'] = 'normal'
            return True

    def pullData(self):
        tickerPrice = self.mvc.grabLastTradePrice(self.searchBar.get())
        if tickerPrice == 0:
            self.buyButton['state'] = 'disabled'
            self.error.set("Invalid ticker!")
        else:
            self.stockPrice.set(tickerPrice)
            self.error.set("");
            self.buyButton['state'] = 'normal'
         
    def buyStock(self):
        if self.unlockButton() == False:
            return
            
        if not self.stockAmountBar.get():
            return

        result = self.mvc.buyStock(self.stockPrice.get(), 
                                   int(self.stockAmountBar.get()),
                                   self.searchBar.get())
        if result == True:
            self.currentBal.set(self.mvc.getCurrentBalance())
            self.error.set("")
        else:
            self.error.set(result)
            self.buyButton['state'] = 'disabled'

    def sellStock(self, int):
        pass

    def getPortfolio(self):
        port = self.mvc.getPortfolio()
        self.portfolio.set(port)
