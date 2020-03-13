'''Programming Assignment 10: Add Custom Functionality of Your Own Choice

Use matplotlib finance API to improve upon the graphs you created (https://matplotlib.org/api/finance_api.html)
matplotlib.finance has been depreciated so I used the new version (https://github.com/matplotlib/mplfinance)

This program will plot that last month of open, closing, high, and low prices for each stock in seperate candlestick charts.

This program will open a JSON file, read the data, and convert it to a pandas Dataframe.
It will convert date to datetype for the mplfinance application and convert string number to floats. 
Then it will segement each stock into sepeate groups and each stock will be added to a list.
The script will iterate through the list to plot each stock to a candlestick chart.
The candlestick charts will contain moving averages for 5 and 10 days and volume for each day. 

Developed by Kyle DuBois. Version 1. Written 3/9/2020'''

import json
from datetime import datetime
from datetime import date
import pandas as pd
import mplfinance as mpf


try:
    df = pd.read_json(r'AllStocks.json',orient="records",convert_dates=True)  #  Read the JSON stream into a pandas Dataframe
except FileNotFoundError:
    print('JSON file not found in directory.')
else:
    df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')  # Convert date in date column to datetype.
    df = df.sort_values(by="Date") # Sort data by date.
    df.set_index('Date', inplace=True, drop=True)  # Change the dataframe index to the date.


    # Update date range to only show the last month.
    df = df.loc['2017-07-04':'2017-08-04',:]

    # Convert string values for Open, High, and Low to float. Replace with NaN if error.
    df['Open'] = pd.to_numeric(df['Open'], errors='coerce')  
    df['High'] = pd.to_numeric(df['High'], errors='coerce')
    df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

    # Filter each stock into a sperate groups.
    stock1 = df.loc[df['Symbol'] == 'AIG' ]
    stock2 = df.loc[df['Symbol'] == 'F']
    stock3 = df.loc[df['Symbol'] == 'FB']
    stock4 = df.loc[df['Symbol'] == 'GOOG']
    stock5 = df.loc[df['Symbol'] == 'M']
    stock6 = df.loc[df['Symbol'] == 'MSFT']
    stock7 = df.loc[df['Symbol'] == 'RDS-A']

    # Create a list to place each stock
    stock_list = []

    # Append each stock to the list
    stock_list.append(stock1)
    stock_list.append(stock2)
    stock_list.append(stock3)
    stock_list.append(stock4)
    stock_list.append(stock5)
    stock_list.append(stock6)
    stock_list.append(stock7)

    #  Iterate through stock list to plot date in candlestick graph
    for stock in stock_list:
        mpf.plot(stock, type='candle', mav =(5,10), volume=True) # Plot each stock in a candle graph, include moving averages for 5 and 10 days, and volume for day.
