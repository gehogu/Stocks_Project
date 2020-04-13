from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import requests
from typing import Dict, List, Tuple, Any
import pandas as pd
import json


# prompt for user to pick symbol
def stock_picker():
    valid = True
    while valid:
        try:
            stockprice = str(input("Enter a symbol: "))
            stockp = stockprice.upper()
            valid = False
        except ValueError:
            print("enter a stock symbol")
    return stockp


# Setting up pandas dataframe
def stock_retrieve(sym) -> List[Dict]:
    key = 'OMUTW5LN5BPYR0YN'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={sym}&apikey={key}'
    r = requests.get(url)
    request = r.text
    tt = json.loads(request)
    return tt


# Sets up matplot graph with given symbol by user
def stock_tracker(sym):
    key = 'OMUTW5LN5BPYR0YN'
    ts = TimeSeries(key=f'{key}', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=f'{sym}', interval='1min', outputsize='full')
    data['4. close'].plot()
    plt.title(f'Intraday Times Series for the {sym} stock (1 min)')
    plt.show()


def main():
    stock = stock_picker()
    p = stock_retrieve(stock)
    o = pd.DataFrame(p)
    print(o.to_string())
    stock_tracker(stock)


if __name__ == '__main__':
    main()
