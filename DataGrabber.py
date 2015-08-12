import urllib
from decimal import Decimal
from urllib import request

class DataGrabber:
    """Grabs financial data from the Yahoo Query Language console."""
    dataURL = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from" \
              "%20yahoo.finance.quote%20where%20symbol%20in%20(%22"
    secondURL = "%22)&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2" \
                "Falltableswithkeys"

    def __init__(self):
        pass
        
    def grabPrice(self, ticker):
        """Retrieves the stock price for a given stock ticker.

        The given stock ticker is passed to the YQL database which returns
        a page containing various stock data. Each line is read until the
        last trade price is found, and the last trade price is returned.
        
        Args:
            ticker: The stock ticker of the company.

        Returns:
            The stock price of the company is returned. If no stock ticker
            is found, 0.00 is returned.
        """

        page = urllib.request.urlopen(self.dataURL + ticker + self.secondURL)
        for line in page:
            data = str(line, encoding='utf8')
            if "<LastTradePriceOnly" in data:
                firstIndex = data.find("<LastTradePriceOnly>")
                secondIndex = data.find("</LastTradePriceOnly>")
                price = float(data[firstIndex+20:secondIndex])
                if len(data[firstIndex+20:secondIndex]) > 6:
                    return 0.00
                else:
                    return Decimal(price).quantize(Decimal('.01'))
        return 0.0
    

    
