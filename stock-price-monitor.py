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


# User Inputs

input_container = st.beta_container()
col1, col2 = st.beta_columns([5, 5])
with input_container:
    with col1:
        exch = st.selectbox('Exchange', ['NASDAQ', 'NYSE', 'AMEX']) # Input Exchange
    with col2:
        tickerSymbol = st.selectbox('Stock Symbol', get_tickers(exch)) # Input Stock Symbol

#Data on the selected ticker
tickerData = yf.Ticker(tickerSymbol)

#Get historical data prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31')
companyName = tickerData.info['longName']
st.markdown(f"Shown below are the stock closing price and volume of **{companyName}**.")

my_expander = st.beta_expander('Company Details')
with my_expander:
	st.markdown(f"""
Name : {companyName} \n
Sector : {tickerData.info['sector']}\n
City : {tickerData.info['city']}\n
Country : {tickerData.info['country']}\n
Full Time Employees : {tickerData.info['fullTimeEmployees']}\n
Website : {tickerData.info['website']}\n
Previous Close : {tickerData.info['previousClose']}\n
	""")

# Plot a line chart to show Closing Prices
st.write("## Closing Price")
st.line_chart(tickerDf.Close)

# Plot a line chart to show Volume Prices
st.write("## Volume")
st.line_chart(tickerDf.Volume)