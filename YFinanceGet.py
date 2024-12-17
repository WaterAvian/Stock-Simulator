import yfinance as yf

class GetYfData:
    def __init__(self, ticker):
        priceData = yf.Ticker(ticker).history("max")
        dividendData = priceData.dividends()
