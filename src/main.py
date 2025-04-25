import streamlit as st 
from src.analysis import get_stock_data ,get_real_time_sentiment,analyze_stock
from src.llm_service import get_swot_analysis,final_decision
import os 


st.set_page_config(page_title="📊 Stock Analyzer & Reporter", layout="wide")


st.markdown("""
<style>
.title {
    font-size: 36px;
    font-weight: bold;
    color: #f8a900;
}
.subtitle {
    font-size: 20px;
    color: #999;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📈 Stock Market Analyzer & Reporter</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Analyze Indian stocks with technical indicators, LLM-based SWOT </div>", unsafe_allow_html=True)
st.markdown("---")


stock_options = {
    # Sri Lankan Stocks (Colombo Stock Exchange - CSE)
    "John Keells Holdings": "JKH.CSE",
    "Commercial Bank of Ceylon": "COMB.CSE",
    "Hatton National Bank": "HNB.CSE",
    "Dialog Axiata": "DIAL.CSE",
    "LOLC Holdings": "LOLC.CSE",
    "Ceylon Tobacco Company": "CTC.CSE",
    "Sampath Bank": "SAMP.CSE",
    "Ceylinco Insurance": "CINS.CSE",
    "Hayleys PLC": "HAYL.CSE",
    "Sri Lanka Telecom": "SLTL.CSE",

    # Major International Stocks (NYSE/NASDAQ)
    "Apple (AAPL)": "AAPL",
    "Tesla (TSLA)": "TSLA",
    "Microsoft (MSFT)": "MSFT",
    "Amazon (AMZN)": "AMZN",
    "Alphabet (Google) (GOOGL)": "GOOGL",
    "Meta (Facebook) (META)": "META",
    "NVIDIA (NVDA)": "NVDA",
    "Netflix (NFLX)": "NFLX",
    "Berkshire Hathaway (BRK.B)": "BRK-B",
    "Taiwan Semiconductor (TSM)": "TSM",
    "Samsung (005930.KS)": "005930.KS",  # Korea Exchange
    "Toyota (TM)": "TM",  # NYSE
    "Sony (SONY)": "SONY",
    "LVMH (LVMUY)": "LVMUY",  # Luxury/Europe
    "S&P 500 ETF (SPY)": "SPY"  # Broad market exposure
}
selected_company = st.selectbox("📌 Select a Company (Sri Lankan or International Stocks)", options=list(stock_options.keys()))
ticker = stock_options[selected_company]

period = st.radio("📅 Select Time Period", ["1mo", "3mo", "6mo", "1y", "2y"], horizontal=True)


if st.button("🚀 Run Full Analysis"):
    with st.spinner("⏳ Fetching data and running analysis..."):
        hist, info, sentiment = analyze_stock(ticker, period)
        swot = get_swot_analysis(info, sentiment)
        Decision = final_decision(info,sentiment)


    tab1, tab2 ,tab3 = st.tabs(["📰 Sentiment", "🧠 SWOT", "AI Based Decision"])



    with tab1:
        st.subheader("📰 Real-Time News Sentiment (Powered by LLMA  🔥)")
        st.markdown(f"**{selected_company}** sentiment analysis based on live news:")
        st.markdown(sentiment)


    with tab2:
        st.subheader("🧠 AI SWOT Analysis (Gemma 2)")
        st.code(swot, language='markdown')
        
    with tab3:
        st.subheader("🔥 AI Based Decision (Deepseek)")    
        st.code(Decision, language='markdown')
        
        

else:
    st.markdown("👈 Choose a stock and run the analysis to see results.")
