!pip install -q yfinance
!pip install -q yahoofinancials
!pip install -q pandas-datareader
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import numpy as np
import pandas_datareader as pdr
import datetime as dt

%load_ext autoreload
%autoreload 2

def normalize_data(df):
    return df/df.iloc[0, :]