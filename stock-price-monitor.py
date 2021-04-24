import pandas as pd
import yfinance as yf
import streamlit as st

st.write("""
# Stock Price Monitor

Shown below are the stock closing price and volume of Google.

""")

tickr = st.selectbox('Select', ['GOOGL','AAPL','AMZN','ACN'])

#Ticker symbol
tickerSymbol = tickr #You can change the ticker symbol for the name of the stock of the company you're intrested in.


#Data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#Get historical data prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-4-24')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)