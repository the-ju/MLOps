import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import scipy.optimize as sco

# Fetch stock data
def fetch_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Optimize Portfolio
def optimize_portfolio(tickers, start_date, end_date):
    stock_data = fetch_stock_data(tickers, start_date, end_date)
    returns = stock_data.pct_change().dropna()

    # Define Sharpe ratio function
    def sharpe_ratio(weights):
        portfolio_return = np.sum(returns.mean() * weights)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov(), weights)))
        return -portfolio_return / portfolio_volatility  # Minimize negative Sharpe ratio

    # Constraints and bounds
    num_assets = len(tickers)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(num_assets))
    init_guess = num_assets * [1. / num_assets]

    # Optimization
    result = sco.minimize(sharpe_ratio, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x  # Optimized weights

# Streamlit UI
st.title("AI-Powered Finance Advisor")
tickers = st.text_input("Enter stock tickers (comma-separated):", "AAPL, AMZN, TSLA")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Optimize Portfolio"):
    tickers_list = [t.strip() for t in tickers.split(',')]
    optimized_weights = optimize_portfolio(tickers_list, str(start_date), str(end_date))
    st.write(f"Optimized Portfolio Weights: {dict(zip(tickers_list, optimized_weights))}")
