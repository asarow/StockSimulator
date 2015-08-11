import urllib
from urllib import request

class DataGrabber:
    dataURL = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from" \
              "%20yahoo.finance.quote%20where%20symbol%20in%20(%22"
    secondURL = "%22)&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2" \
                "Falltableswithkeys"

    def __init__(self):
        pass
        
    def grabPrice(self, ticker):
        page = urllib.request.urlopen(self.dataURL + ticker + self.secondURL)
        for line in page:
            data = str(line, encoding='utf8')
            if "<LastTradePriceOnly" in data:
                firstIndex = data.find("<LastTradePriceOnly>")
                secondIndex = data.find("</LastTradePriceOnly>")
                price = data[firstIndex+20:secondIndex]
                if len(price) > 6:
                    return 0.0
                else:
                    return float(price)
        return 0.0
                
