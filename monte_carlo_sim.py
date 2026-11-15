import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

def get_data(stocks, start, end):
    stockData = yf.download(stocks, start=start, end=end, auto_adjust=True)['Close']
    returns = stockData.pct_change().dropna()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

stockList = ['NVDA', 'AAPL', 'MSFT', 'AMZN', 'GOOGL']
end_date = dt.datetime.now()
start_date = dt.datetime(2020, 1, 1)

meanReturns, covMatrix = get_data(stockList, start_date, end_date)