# Financial_Data_Web_SCraper_Data_Analyzer

Financial Data Web Scraper & Analyzer:
This project is a simple financial data scraper and analyzer that fetches stock data, does some basic analysis, and saves it in a CSV file. It pulls data from Yahoo Finance and uses Python libraries like yfinance, requests, BeautifulSoup, pandas, and matplotlib to get, process, and visualize the data.

What It Does:
Scrapes Stock Data:
Gets the current price of a stock by scraping Yahoo Finance.
Downloads Historical Data:
Uses yfinance to download historical stock data like open, close, high, low, and volume for the last few years.

Simple Analysis:

Step1.It calculates the 50-day and 200-day Simple Moving Averages (SMA) for the stock.

Step2.It then plots the stock’s price and these moving averages on a graph.

Step3.Saves Data to CSV:

Step4.The stock data is saved to a CSV file, making it easy for you to download and analyze it offline.

Technologies Used:

Python: The main language used to build the scraper, perform analysis, and create visualizations.
yfinance: This library helps to fetch historical stock data directly from Yahoo Finance.
requests: Used to send HTTP requests and fetch live data from the web.
BeautifulSoup: Helps to extract stock prices from the Yahoo Finance web page.
pandas: For handling and processing the stock data.
matplotlib: Used to create graphs and plots to visualize stock trends.

How to Use:
1.Clone or download the repository.
2.Install the required libraries by running the following in your terminal:
3.Run in terminal (pip install requests beautifulsoup4 pandas matplotlib yfinance)
5.Run the script financial_data_scraper_analyzer.py.
6.When prompted, enter a stock symbol (e.g., AAPL for Apple, TSLA for Tesla).
7.The script will:
Display the current stock price.
Download the stock’s historical data.
Plot the 50-day and 200-day Simple Moving Averages (SMA).
Save the data to a CSV file, named <stock_symbol>_data.csv.


Enter the stock symbol (e.g., AAPL, MSFT, TSLA): AAPL
Current Price of AAPL: 150.22
Data for AAPL from 2020-01-01 to 2025-01-01:
                  Open        High         Low       Close   Adj Close   Volume
Date                                                                        
2020-01-02  296.23999  298.929993  295.419998  296.23999  296.23999  33870100
2020-01-03  296.050018  298.279999  294.75     297.429993  297.429993  36586700
...
Data saved to AAPL_data.csv


Date,Open,High,Low,Close,Adj Close,Volume
2020-01-02,296.23999,298.929993,295.419998,296.23999,296.23999,33870100
2020-01-03,296.050018,298.279999,294.75,297.429993,297.429993,36586700
...

if you feel that something can be improved in this project, feel free to create a pull request.
