import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt
from get_tickers import *


st.set_page_config(layout="centered") 
st.write('# Stock Price Monitor\n' + 'by Mayur Machhi')

exch = st.selectbox('Exchange', ['NASDAQ', 'NYSE', 'AMEX'])
#Ticker symbol
tickerSymbol = st.selectbox('Stock Symbol', get_tickers(exch)) # You can change the ticker symbol for the name of the stock of the company you're intrested in.

#Data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#Get historical data prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31')
companyName = tickerData.info['longName']
st.write(" Shown below are the stock closing price and volume of "+ "***" + companyName+"***") 


# Plot a line chart to show Closing Prices
st.write("## Closing Price")
st.line_chart(tickerDf.Close)

# Plot a line chart to show Volume Prices
st.write("## Volume")
st.line_chart(tickerDf.Volume)