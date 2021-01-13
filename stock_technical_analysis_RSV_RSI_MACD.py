'''
firstly
pip install stockstats
pip install yfinance
'''

import pandas as pd
from stockstats import StockDataFrame
from pandas_datareader import data as web
from datetime import datetime
import yfinance as yf


class Stock_analytics_index():  # 建立股票類別
    def __init__(self, stock):
        self.__stock = str(stock)
        self.__start_date = datetime(2000, 1, 2)
        self.__end_date = datetime.now()
        self.__get_stock_data()

    def __get_stock_data(self):  # 從 yfinance 拿取股價資料
        df = web.get_data_yahoo(self.__stock, self.__start_date, self.__end_date)
        analysis = f'./{self.__stock}data.csv'  # 在當前資料夾產生該股票的股價資料
        df.to_csv(analysis)
        data = pd.read_csv(analysis, parse_dates=True, index_col='Date')
        price = data["Close"]
        stock = StockDataFrame.retype(pd.read_csv('./stockdata.csv'))

    def get_rsv_9(self):  # 取得該股票的RSV
        return stock.get('rsv_9')

    def get_rsi_6(self):  # 取得該股票的RSI, RSI(6)
        return stock.get('rsi_6')

    def get_rsi_9(self):  # 取得該股票的RSI, RSI(9)
        return stock.get('rsi_9')

    def get_macd(self):  # 取得該股票的MACD
        return stock['macd']

    def get_macd_12(self):  # 取得該股票的MACD, n=12
        return stock['close_12_ema']

    def get_macd_26(self):  # 取得該股票的MACD, m=26
        return stock['close_26_ema']

    def get_macd_9(self):  # 取得該股票的MACD, x=9
        return stock['close_9_ema']


