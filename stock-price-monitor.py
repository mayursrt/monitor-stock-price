import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt

st.write('# Stock Price Monitor')

tickr = st.selectbox('Select', ['GOOGL','AAPL','AMZN','ACN'])

#Ticker symbol
tickerSymbol = tickr #You can change the ticker symbol for the name of the stock of the company you're intrested in.



#Data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#Get historical data prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-4-24')
companyName = tickerData.info['longName']
st.write(" Shown below are the stock closing price and volume of "+ "***" + companyName+"***") 


# Plot a line chart to show Closing Prices
st.write("## Closing Price")
st.line_chart(tickerDf.Close)

# Plot a line chart to show Volume Prices
st.write("## Volume")
st.line_chart(tickerDf.Volume)