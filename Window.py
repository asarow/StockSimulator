from tkinter import *
from ModelViewController import ModelViewController

class Window:
    def __init__(self):
        self.mvc = ModelViewController()
        root = Tk()
        root.minsize(width=500, height=500)
        self.stockPrice = IntVar()
        self.currentBal = IntVar()
        self.error = StringVar()
        self.currentBal.set(self.mvc.getCurrentBalance())

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
         self.stockPrice.set(self.mvc.grabLastTradePrice(self.searchBar.get()))
    
    def buyStock(self):
        if self.unlockButton() == False:
            return

        result = self.mvc.buyStock(self.stockPrice.get(), 
                                   int(self.stockAmountBar.get()),
                                   self.searchBar.get())
        if result == True:
            self.currentBal.set(self.mvc.getCurrentBalance())
            self.error.set("")
        else:
            self.error.set(result)

    def sellStock(self, int):
        pass
