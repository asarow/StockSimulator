from tkinter import *
import tkinter.messagebox as tmb
from Controller import Controller

class Window:
    def __init__(self):
        self.controller = Controller()
        self.controller.loadData()
        self.root = Tk()
        self.root.wm_title("Stock simulator v1.0")
        self.root.minsize(width=500, height=500)
        self.root.protocol("WM_DELETE_WINDOW", self.askQuit)
        self.stockPrice = DoubleVar()
        self.currentBal = DoubleVar()
        self.error = StringVar()
        self.currentBal.set(self.controller.getCurrentBalance())

        self.displayLabel = Label(self.root, text="Enter a ticker: ")
        self.searchBar = Entry(self.root)
        self.searchButton = Button(self.root, text="Go", command=lambda: 
                                   self.checkData())
                   
        self.buyButton = Button(self.root, text="Buy", state=DISABLED,
                                command=lambda: self.buyStock())
        self.sellButton = Button(self.root, text="Sell", state=DISABLED,
                                 command=lambda: self.sellStock())
        self.stockAmountBar = Entry(self.root)
        self.balanceLabel = Label(self.root, text="Current balance: ")
        self.balanceAmount = Label(self.root, textvariable=self.currentBal)
        self.tickerDisplay = Label(self.root, anchor=E, text="Stock price:")
        self.tickerPrice = Label(self.root, textvariable=self.stockPrice)
        self.errorLabel = Label(self.root, textvariable=self.error)
        self.viewPortfolio = Button(self.root, text="View Portfilio", 
                                    command=lambda: self.getPortfolio())

        self.displayLabel.grid(row=0, column=0, sticky=E)
        self.searchBar.grid(row=0, column=1)
        self.searchButton.grid(row=0, column=2, sticky=W)
        self.balanceLabel.grid(row=1, column=0, sticky=E)
        self.balanceAmount.grid(row=1, column=1, sticky=W)
        self.tickerDisplay.grid(row=2, column=0, sticky=E)
        self.tickerPrice.grid(row=2, column=1, sticky=W)
        self.stockAmountBar.grid(row=0, column=3)
        self.buyButton.grid(row=0, column=4)
        self.sellButton.grid(row=1, column=4, sticky=E)
        self.errorLabel.grid(row=1, columnspan=3, sticky=E)
        self.viewPortfolio.grid(row=4, column=0)
        self.root.mainloop()

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
        tickerPrice = self.controller.grabLastTradePrice(self.searchBar.get())
        if tickerPrice == 0:
            self.buyButton['state'] = 'disabled'
            self.sellButton['state'] = 'disabled'
            self.error.set("Invalid ticker!")
        else:
            self.stockPrice.set(tickerPrice)
            self.error.set("");
            self.buyButton['state'] = 'normal'
            self.sellButton['state'] = 'normal'

    def buyStock(self):
        if self.unlockButton() == False:
            return
            
        if not self.stockAmountBar.get():
            return
            
        result = self.controller.buyStock(int(self.stockAmountBar.get()),
                                          self.searchBar.get())
        if result == True:
            self.currentBal.set(self.controller.getCurrentBalance())
            self.error.set("")
        else:
            self.error.set(result)
            self.buyButton['state'] = 'disabled'

    def sellStock(self):
        if self.unlockButton() == False:
            return

        if not self.stockAmountBar.get():
            return

        result = self.controller.sellStock(int(self.stockAmountBar.get()),
                                           self.searchBar.get())
        
        if result == True:
            self.currentBal.set(self.controller.getCurrentBalance())
            self.error.set("")
        else:
            self.error.set(result)
            self.sellButton['state'] = 'disabled'
        

    def getPortfolio(self):
        self.portWindow = Toplevel()
        self.portWindow.wm_title("Portfolio")
        self.tickerBox = Listbox(self.portWindow)
        self.valBox = Listbox(self.portWindow)
        self.tickerBox.grid(row=0, column=0)
        self.valBox.grid(row=0, column=1)
        port = self.controller.getPortfolio()

        for key in sorted(port):
            self.tickerBox.insert(END, key)
            self.valBox.insert(END, port[key])

    def askQuit(self):
        if tmb.askokcancel("Quit", "Are you sure you want to exit?"):
            self.controller.saveData()
            self.root.destroy()
