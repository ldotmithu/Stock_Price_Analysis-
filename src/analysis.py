import yfinance as yf 
import os 
import re 
from dotenv import load_dotenv
import requests
load_dotenv()
import pandas as pd 

GROQ_API_KEY = os.getenv('GROQ_API_KEY') 
AlPHA_API_KEY = os.getenv('AlPHA_API_KEY')

def get_stock_data(ticker,period = "6mo"):
    try:
        stock = yf.Ticker(ticker=ticker)
        hist = stock.history(period=period)
        info = stock.info
    except Exception as e:
        hist, info = get_from_alpha_vantage(ticker)
    return hist, info


def get_real_time_sentiment(ticker):
    prompt = f"Search the latest 3 news about {ticker}. Summarize sentiment and cite headlines."
    url = "https://api.groq.com/openai/v1/chat/completions"  # endpoint
    headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}
    
    data = {
        'model': 'meta-llama/llama-4-scout-17b-16e-instruct', 
        'messages': [{'role': 'user', 'content': prompt}]  
    }
    
    response = requests.post(url=url, headers=headers, json=data)
    response.raise_for_status()  
    return response.json()['choices'][0]['message']['content']

# get from gpt 
def get_from_alpha_vantage(ticker: str):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": ticker,
        "apikey": AlPHA_API_KEY,
        "outputsize": "compact"
    }
    r = requests.get(url, params=params).json()
    ts = r.get("Time Series (Daily)", {})
    df = pd.DataFrame.from_dict(ts, orient="index").sort_index()
    df = df.rename(columns={"5. adjusted close": "Close"})
    df["Close"] = df["Close"].astype(float)
    df.index = pd.to_datetime(df.index)
    return df.tail(120), {"shortName": ticker, "sector": "N/A", "marketCap": "N/A", "longBusinessSummary": "N/A"}
    
    
            
def analyze_stock(ticker: str, period="6mo"):
    hist, info = get_stock_data(ticker, period)
    sentiment = get_real_time_sentiment(ticker)
    return hist, info, sentiment