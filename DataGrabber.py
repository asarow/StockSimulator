
class DataGrabber:
    dataURL = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from" \
              "%20yahoo.finance.quote%20where%20symbol%20in%20(%22"
    secondURL = "YHOO%22)&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2" \
                "Falltableswithkeys"

    def __init__(self):
        print(self.dataURL)
