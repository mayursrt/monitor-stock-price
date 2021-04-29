import pandas as pd


tickersdf = pd.read_csv('assets/tickers.csv')

def get_tickers(exchange='NASDAQ'):
	
	tickers = list(tickersdf[exchange])
	return tickers