import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Simple SMA crossover learning script.")
    parser.add_argument("--ticker", default="AAPL", help="Ticker to analyze, for example AAPL or BTC-USD.")
    parser.add_argument("--period", default="5y", help="yfinance period, for example 1y, 5y, or max.")
    parser.add_argument("--output", default="", help="Optional path to save the generated chart.")
    return parser.parse_args()


args = parse_args()
ticker = args.ticker.upper()

# Fetch historical daily data for the selected ticker.
print(f"Pulling historical market data for {ticker}...")
data = yf.download(ticker, period=args.period)

if data.empty:
    raise SystemExit(f"No market data returned for {ticker}.")

# Quick sanity check on the dataframe structure
print("Data structure verified.")

# Calculating Technical Indicators: 50-day and 200-day Simple Moving Averages (SMA) (could be any other parameters)
print("Calculating moving averages...")
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

print("Scanning data for BUY/SELL signals...")
data['Signal'] = 0.0
data['Signal'] = np.where(data['SMA_50'] > data['SMA_200'], 1.0, 0.0)
data['Position'] = data['Signal'].diff()

# print the buy/sell signal dates
for date, row in data[data['Position'] == 1].iterrows():
    print(f"[BUY] Signal detected on: {date.strftime('%Y-%m-%d')}")
for date, row in data[data['Position'] == -1].iterrows():
    print(f"[SELL] Signal detected on: {date.strftime('%Y-%m-%d')}")

# Visualizing the Price Action alongside our new SMA indicators and configure the graph
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label=f'{ticker} Close Price', color='midnightblue', alpha=0.5)
plt.plot(data.index, data['SMA_50'], label='50-Day SMA', color='orange', linewidth=2)
plt.plot(data.index, data['SMA_200'], label='200-Day SMA', color='red', linewidth=2)

# add visual markers
plt.plot(data[data['Position'] == 1].index, data['SMA_50'][data['Position'] == 1], '^', markersize=10, color='g', label='Buy Signal')
plt.plot(data[data['Position'] == -1].index, data['SMA_50'][data['Position'] == -1], 'v', markersize=10, color='r', label='Sell Signal')

# Styling the chart for a more explicit analysis
plt.title(f"{ticker} Price Action with 50 & 200-Day SMAs")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)

if args.output:
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"Saved chart to {output_path}")

plt.show()


