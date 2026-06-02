# SMA Crossover Bot

A small learning project that fetches historical market data, calculates 50-day and 200-day Simple Moving Averages, and marks basic crossover signals.

The goal is not to provide trading advice. It is a practical first project for getting comfortable with Python, financial data APIs, time series data, and simple visualization.

![AAPL Bot Chart](assets/apple.png)
![BTC-USD Bot Chart](assets/btc-usd.png)
![NVDA Bot Chart](assets/NVDA.png)

## Key Features
- Fetches historical daily market data using the `yfinance` API.
- Calculates 50-day and 200-day Simple Moving Averages.
- Detects basic buy/sell crossover points using NumPy.
- Visualizes close price, moving averages, and crossover markers with Matplotlib.

## Tech Stack
- Python
- Pandas
- NumPy
- yfinance
- Matplotlib

## Setup
```bash
python -m pip install -r requirements.txt
```

## How to Run
```bash
python main.py
```

You can also choose a ticker and period:

```bash
python main.py --ticker NVDA --period 5y --output assets/NVDA.png
```

## Notes
This is an introductory project for learning purposes. The default example analyzes Apple (`AAPL`) over a 5-year period.
