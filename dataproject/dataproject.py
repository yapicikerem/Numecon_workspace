import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import numpy as np
import pandas_datareader as pdr
import datetime as datetime

def normalize_data(df):
    return df/df.iloc[0, :]