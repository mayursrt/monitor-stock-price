import pandas as pd
import yfinance as yf
import streamlit as stl

stl.write("""
# Stock Price Monitor

Shown below are the stock closing price and volume of Google.

""")

#Ticker symbol
tickerSymbol = 'GOOGL' #You can change the ticker symbol for the name of the stock of the company you're intrested in.


#Data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#Get historical data prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

stl.line_chart(tickerDf.Close)
stl.line_chart(tickerDf.Volume)