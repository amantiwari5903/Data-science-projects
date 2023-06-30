import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Read the data from the CSV file
data = pd.read_csv("TATAMOTORS.NS.csv")
# Print the data
print(data)
# Display information about the data
data.info()
# Generate descriptive statistics of the data
data.describe()
# Check for missing values in the data
data.isnull().sum()
# Create a line plot with Open, High, and Low prices
plt.figure(figsize=(20, 7))
plt.plot(data['Date'], data['Open'], color='blue', label='Open')
plt.plot(data['High'], color='grey', label='High')
plt.plot(data['Low'], color='orange', label='Low')
plt.title("Tata Motors Stocks Open,High and Low")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend(title="")
plt.show()
# Create a candlestick chart using Plotly
figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"], high=data["High"],
                                        low=data["Low"], close=data["Close"])])
figure.update_layout(title="Tata Motors Stock Price Analysis",
                     xaxis_rangeslider_visible=False)
figure.show()

#I used a tool called yfinance from Yahoo Finance to collect stock price data. It helped me get information about the prices of different stocks, like their opening and closing prices, highest and lowest prices, and the number of shares traded. Overall, yfinance was a great and trustworthy resource for getting the most recent and accurate stock price information.
