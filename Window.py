from tkinter import *
from ModelViewController import ModelViewController

class Window:
    def __init__(self):
        self.mvc = ModelViewController()
        root = Tk()
        root.minsize(width=500, height=500)
        self.stockPrice = IntVar()
        self.currentBal = IntVar()
        self.currentBal.set(self.mvc.getCurrentBalance())

        self.displayLabel = Label(root, text="Enter a ticker: ")
        self.searchBar = Entry(root)
        self.searchButton = Button(root, text="Go", command=lambda:
                    self.stockPrice.set(self.mvc.grabLastTradePrice
                                   (self.searchBar.get())))
        self.buyButton = Button(root, text="Buy", command=lambda:
                                self.buyStock())
        self.stockAmountBar = Entry(root)
        self.balanceLabel = Label(root, text="Current balance: ")
        self.balanceAmount = Label(root, textvariable=self.currentBal)
        self.tickerDisplay = Label(root, text="Ticker price ")
        self.tickerPrice = Label(root, textvariable=self.stockPrice)

        self.displayLabel.grid(row=0, column=0)
        self.searchBar.grid(row=0, column=1)
        self.searchButton.grid(row=0, column=2)
        self.balanceLabel.grid(row=1, column=0)
        self.balanceAmount.grid(row=1, column=1)
        self.tickerDisplay.grid(row=2, column=0)
        self.tickerPrice.grid(row=2, column=1)
        self.stockAmountBar.grid(row=2, column=2)
        self.buyButton.grid(row=2, column=3)

        root.mainloop()
        
    def buyStock(self):
        print("Price is %6.2f " % (self.stockPrice.get() 
                                   * int(self.stockAmountBar.get())))
        self.mvc.buyStock(self.stockPrice.get(), int(self.stockAmountBar.get()))
        self.currentBal.set(self.mvc.getCurrentBalance())
        
    def sellStock(self, int):
        pass
