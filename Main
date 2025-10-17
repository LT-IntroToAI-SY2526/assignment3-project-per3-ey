import yfinance as yf
import pandas as pd

# Create a Ticker object for a stock (e.g., AAPL)
aapl = yf.Ticker("AAPL")

# Download historical market data for the last 12 months
# The data is returned as a pandas DataFrame
stock_data = aapl.history(period="1y")

# Print the downloaded data
print(stock_data.head()) # Print the first 5 rows
print("\n")
print(stock_data.tail()) # Print the last 5 rows

# You can also access other information using the Ticker object
# Get company information
info = aapl.info
print("\nCompany Name:", info['longName'])
print("Sector:", info['sector'])
print("Industry:", info['industry'])

# Get dividends and splits
print("\nDividends:\n", aapl.dividends)
print("\nSplits:\n", aapl.splits)

# You can also download data for multiple tickers at once
data = yf.download("MSFT AAPL GOOG", start="2024-01-01", end="2024-10-17")
print("\nMulti-ticker data:\n", data.head())