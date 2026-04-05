import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

apple = yf.download("AAPL", start="2020-01-01", end="2024-01-01")
tesla = yf.download("TSLA", start="2020-01-01", end="2024-01-01")

plt.figure()
plt.plot(apple['Close'], label='Apple')
plt.plot(tesla['Close'], label='Tesla')
plt.title("Apple vs Tesla Stock Price")
plt.legend()
plt.show()
# Moving averages
apple['MA50'] = apple['Close'].rolling(window=50).mean()
apple['MA200'] = apple['Close'].rolling(window=200).mean()

plt.figure()
plt.plot(apple['Close'], label='Apple Price')
plt.plot(apple['MA50'], label='50-Day MA')
plt.plot(apple['MA200'], label='200-Day MA')

plt.title("Apple Stock Price with Moving Averages")
plt.legend()
plt.show()
# Daily returns
apple['Daily Return'] = apple['Close'].pct_change()

plt.figure()
apple['Daily Return'].plot(title="Apple Daily Returns")
plt.show()
# -----------------------
# Insights
# -----------------------

# Apple shows a steady upward trend over time
# Tesla is more volatile compared to Apple
# Moving averages help identify long-term trends
# Daily returns highlight periods of high volatility