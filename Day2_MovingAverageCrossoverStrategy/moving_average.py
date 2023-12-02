import pandas as pd
import numpy as np
from Day1_HistoricalStockPriceDownloader.stock_price import DataScraper


class TickerPrice:
    def __init__(self, ticker, criteria='Close'):
        self.ticker = ticker
        self.apikey = 'TGQVZHVO92AP5GWD'
        self.criteria = criteria

    def get_prices(self):
        data_scraper = DataScraper(api_key=self.apikey, ticker=self.ticker)
        dict_prices = data_scraper.get_prices()
        df = pd.DataFrame()
        for key, value in dict_prices.items():
            df = pd.concat([df, pd.DataFrame([value], index=[key])])
        df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        return df


class MovingAverageStrategy():
    def __init__(self, ticker, period_low, period_high, criteria='Close'):
        self.ticker = ticker
        self.period_low = period_low
        self.period_high = period_high
        self.criteria = criteria

    def build_prices(self):
        ticker_prices = TickerPrice(self.ticker, self.criteria)
        df = ticker_prices.get_prices()
        return df

    def buy_signal(self):
        prices = self.build_prices()
        ma_low = prices.iloc[:self.period_low][self.criteria].values.astype('float').mean()
        ma_high = prices.iloc[:self.period_high][self.criteria].values.astype('float').mean()
        return ma_low > ma_high


if __name__ == "__main__":
    mas = MovingAverageStrategy('AAPL', 50, 200)
    print(mas.buy_signal())




