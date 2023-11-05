import pandas as pd
import numpy as np
from Day1_HistoricalStockPriceDownloader.stock_price import DataScraper


class MovingAverageStrategy:
    def __init__(self, ticker, period, criteria='Close'):
        self.ticker = ticker
        self.period = period
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

    def get_average(self):
        df = self.get_prices()
        return np.mean(df.iloc[:self.period][self.criteria])




if __name__ == "__main__":
    mas = MovingAverageStrategy('AAPL', 50)
    print(mas.get_prices())
    print(mas.get_average())




