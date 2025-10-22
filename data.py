import yfinance as yf
import pandas as pd
from datetime import datetime

def get_ticker_history(ticker: str, start: str, end: str, interval: str = '1d'):
    for date_str in (start, end):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print(f"Error: Date '{date_str}' is not in the correct format 'YYYY-MM-DD'.")
            return None
    valid_intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    if interval not in valid_intervals:
        print(f"Error: Interval '{interval}' is not valid. Choose from {valid_intervals}.")
        return None
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(start=start, end=end, interval=interval)
        if history.empty:
            print(f"No data found for ticker '{ticker}' between {start} and {end}.")
            return None
        return history
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def get_ticker_price(ticker: str, start: str, end: str, price_type: str = 'Close', interval: str = '1d'):
    valid_price_types = ['Open', 'High', 'Low', 'Close']
    if price_type not in valid_price_types:
        print(f"Error: price_type '{price_type}' is not valid. Choose from {valid_price_types}.")
        return None
    for date_str in (start, end):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print(f"Error: Date '{date_str}' is not in the correct format 'YYYY-MM-DD'.")
            return None
    valid_intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    if interval not in valid_intervals:
        print(f"Error: Interval '{interval}' is not valid. Choose from {valid_intervals}.")
        return None
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(start=start, end=end, interval=interval)
        if history.empty:
            print(f"No data found for ticker '{ticker}' between {start} and {end}.")
            return None
        return history[price_type]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def get_dividends(ticker: str, start: str, end: str):
    for date_str in (start, end):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print(f"Error: Date '{date_str}' is not in the correct format 'YYYY-MM-DD'.")
            return None
    try:
        stock = yf.Ticker(ticker)
        dividends = stock.dividends

        if dividends.empty:
            print(f"No dividend data found for ticker '{ticker}'.")
            return None
        dividends_in_range = dividends[(dividends.index >= start) & (dividends.index <= end)]
        if dividends_in_range.empty:
            print(f"No dividends found for ticker '{ticker}' between {start} and {end}.")
            return None
        return dividends_in_range
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def get_volume(ticker: str, start: str, end: str, interval: str = '1d'):
    for date_str in (start, end):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print(f"Error: Date '{date_str}' is not in the correct format 'YYYY-MM-DD'.")
            return None
    valid_intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    if interval not in valid_intervals:
        print(f"Error: Interval '{interval}' is not valid. Choose from {valid_intervals}.")
        return None
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(start=start, end=end, interval=interval)
        if history.empty:
            print(f"No data found for ticker '{ticker}' between {start} and {end}.")
            return None
        return history['Volume']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
print(get_ticker_history('AAPL', '2023-01-01', '2023-10-01', interval='1wk'))
print(get_dividends('CME','2023-01-01', '2023-10-01'))