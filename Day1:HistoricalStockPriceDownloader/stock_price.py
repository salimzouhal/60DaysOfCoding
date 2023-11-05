import csv
import json
import random

import requests


class DataScraper:
    def __init__(self, api_key, ticker):
        self.api_key = api_key
        self.ticker = ticker

    def get_quote(self):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={self.ticker}&apikey={self.api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data['Global Quote']

    def get_financials(self):
        url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={self.ticker}&apikey={self.api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    def get_prices(self):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.ticker}&apikey={self.api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data['Time Series (Daily)']


class FinancialDatabase:
    def __init__(self, api_key, tickers):
        self.api_key = api_key
        self.tickers = tickers

    def get_data(self):
        data = [DataScraper(self.api_key, ticker).get_quote() for ticker in self.tickers]
        return data


api_key = 'TGQVZHVO92AP5GWD'
csv_url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}"

with requests.Session() as s:
    download = s.get(csv_url)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    tickers = [element[0] for element in my_list]

random_index = random.sample(range(0, len(tickers) - 1), 2)
tickers = [tickers[i] for i in random_index]

if __name__ == "__main__":
    #financial_db = FinancialDatabase(api_key, tickers)
    #data = financial_db.get_data()
    #print(data)
    ds = DataScraper(api_key, 'AAPL')
    print(ds.get_prices())