import requests
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Function to scrape financial data from a webpage
def scrape_yahoo_finance(stock_symbol):
    url = f"https://finance.yahoo.com/quote/{stock_symbol}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve data")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the current stock price
    price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
    print(f"Current Price of {stock_symbol}: {price}")
    
    return price

# Function to download stock data using Yahoo Finance API (yfinance)
def get_stock_data(stock_symbol, start_date='2020-01-01', end_date='2025-01-01'):
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    print(f"Data for {stock_symbol} from {start_date} to {end_date}:")
    print(stock_data.head())
    
    # Save stock data to CSV
    csv_filename = f"{stock_symbol}_data.csv"
    stock_data.to_csv(csv_filename)
    print(f"Data saved to {csv_filename}")
    
    return stock_data

# Function to perform basic analysis on stock data
def analyze_stock_data(stock_data):
    # Calculate moving averages
    stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()
    
    # Plotting the stock data with moving averages
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Stock Price', color='blue')
    plt.plot(stock_data['SMA_50'], label='50-Day SMA', color='red')
    plt.plot(stock_data['SMA_200'], label='200-Day SMA', color='green')
    plt.title('Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

# Main function to run the scraper and analyzer
def main():
    # User input for stock symbol
    stock_symbol = input("Enter the stock symbol (e.g., AAPL, MSFT, TSLA): ").upper()

    # Scrape Yahoo Finance for the latest price
    price = scrape_yahoo_finance(stock_symbol)
    
    # Get historical stock data from Yahoo Finance
    stock_data = get_stock_data(stock_symbol)
    
    # Analyze stock data by plotting moving averages
    analyze_stock_data(stock_data)

if __name__ == "__main__":
    main()
