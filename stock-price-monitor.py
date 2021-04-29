import pandas as pd
import yfinance as yf
import streamlit as st
from PIL import Image
from get_tickers import *

title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 5])
image = Image.open('assets/stock.jpg')
with title_container:
    with col1:
        st.image(image)
    with col2:
        st.write('# Stock Price Monitor\n' + 'by Mayur Machhi')

# image = Image.open('assets/stock.jpg')
# st.image(image, width=150)

# st.write('# Stock Price Monitor\n' + 'by Mayur Machhi')

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