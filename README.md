# Stock Market Analysis Toolkit

A Python-based tool for analyzing stock data from multiple exchanges (including Sri Lankan CSE and international markets) with real-time sentiment analysis.

## Features

- 📊 **Multi-exchange support**: Analyze stocks from CSE (Sri Lanka), NYSE, NASDAQ, and more
- 📈 **Technical indicators**: MA20, MA50, RSI, MACD calculations
- 🗞️ **Sentiment analysis**: AI-powered news sentiment using Groq API
- 🔄 **Data fallbacks**: Yahoo Finance → Alpha Vantage → CSE API
- 🌍 **International coverage**: 50+ major global stocks pre-configured

## Supported Stock Exchanges

| Exchange       | Example Tickers       | Status       |
|----------------|-----------------------|--------------|
| NYSE/NASDAQ    | `AAPL`, `TSLA`        | ✅ Full support |
| Colombo (CSE)  | `JKH.CSE`, `COMB.CSE` | ⚠️ Fallback needed |
| NSE (India)    | `RELIANCE.NS`         | ✅ Full support |
| Korea (KRX)    | `005930.KS`           | ✅ Full support |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ldotmithu/Stock_Price_Analysis-.git
   cd Stock_Price_Analysis-.git
   ```

2. Install dependencies::
   ```bash
   pip install -r requirements.txt   
   ```

3. Set up environment variables:
   ```.env
   cp .env.example .env 

   GROQ_API_KEY=your_groq_key_here
   ALPHA_API_KEY=your_alpha_vantage_key_here
   ```    