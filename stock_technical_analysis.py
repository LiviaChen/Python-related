import pandas as pd
from stockstats import StockDataFrame
from pandas_datareader import data as web
from datetime import datetime


# thanks to : https://github.com/jealous/stockstats

class Stock_analytics_index():  # 建立股票類別

    def __init__(self, stock):  # 初始化函數
        self.__stock = str(stock)  # 接輸入的美股代碼
        self.__start_date = datetime(2010, 1, 1)  # 股價起始日
        self.__end_date = datetime.now()  # 股價結束日
        self.__get_stock_data()  # 呼叫私有方法__get_stock_data (private method)

    def __get_stock_data(self):  # 從 pandas_datareader 拿取股價資料
        df = web.get_data_yahoo(self.__stock, self.__start_date, self.__end_date)
        analysis = f'./{self.__stock}data.csv'  # 先建立csv檔案路徑
        df.to_csv(analysis)  # 在當前資料夾產生該股票的股價資料
        data = pd.read_csv(analysis, parse_dates=True, index_col='Date')  # 前三行的部份可以使用本機股價檔案來取代
        price = data["Close"]
        self.__stock = StockDataFrame.retype(pd.read_csv(analysis))  # stockstats需求的dataframe

    def get_rsv_9(self):  # 取得該股票的RSV
        return self.__stock.get('rsv_9')

    def get_rsi_6(self):  # 取得該股票的RSI, RSI(6), 6天的RSI
        return self.__stock.get('rsi_6')

    def get_rsi_12(self):  # 取得該股票的RSI, RSI(12), 12天的RSI
        return self.__stock.get('rsi_12')

    def get_macd(self):  # 取得該股票的MACD
        return self.__stock['macd']

    def get_macd_12(self):  # 取得該股票的MACD, n=12
        return self.__stock['close_12_ema']

    def get_macd_26(self):  # 取得該股票的MACD, m=26
        return self.__stock['close_26_ema']

    def get_macd_9(self):  # 取得該股票的MACD, x=9
        return self.__stock['close_9_ema']

    def get_ma_5(self):  # 取得該股票的 5MA
        return self.__stock['cr-ma1']

    def get_ma_10(self):  # 取得該股票的 10MA
        return self.__stock['cr-ma2']

    def get_ma_20(self):  # 取得該股票的 20MA
        return self.__stock['cr-ma3']

    def get_bolling(self):  # 布林通道中線：20MA
        return self.__stock['boll']

    def get_bolling_upper(self):  # 布林通道上線
        return self.__stock['boll_ub']

    def get_bolling_lower(self):  # 布林通道下線
        return self.__stock['boll_lb']

    def get_pdm(self):  # +DM, window defult 1
        return self.__stock['pdm_1']

    def get_mdm(self):  # -DM, window default 1
        return self.__stock['mdm_1']

    def get_pdi(self):  # +DI, 預設14天
        return self.__stock['pdi']

    def get_mdi(self):  # -DI, 預設14天
        return self.__stock['mdi']

    def get_dx(self):  # DX, 預設14天的+DI & -DI
        return self.__stock['dx']

    def get_adx(self):  # ADM, 預設6天的DX SMA
        return self.__stock['adx']

    def get_tr(self):  # TR
        return self.__stock['tr']

    def get_atr(self):  # ATR, 平均TR, 預設14天
        return self.__stock['atr']
