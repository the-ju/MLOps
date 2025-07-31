from models.stock_forecast import predict_stock_price
from models.sentiment_model import analyze_sentiment
from models.portfolio_opt import optimize_portfolio
import pandas as pd

def display_menu():
    print("\nAI-Powered Finance Advisor")
    print("1. Predict Stock Prices")
    print("2. Analyze Financial News Sentiment")
    print("3. Optimize Investment Portfolio")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter stock ticker (e.g., AAPL, TSLA): ").upper()
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            predict_stock_price(ticker, start_date, end_date)

        elif choice == "2":
            news_text = input("Enter financial news headline: ")
            sentiment = analyze_sentiment(news_text)
            print(f"Sentiment Analysis Result: {sentiment}")

        elif choice == "3":
            tickers = list(set(input("Enter stock tickers (comma-separated): ").replace(" ", "").split(",")))
            optimize_portfolio(tickers)

        elif choice == "4":
            print("Exiting AI Finance Advisor. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1-4.")

if __name__ == "__main__":
    main()
