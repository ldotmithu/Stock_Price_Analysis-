from dotenv import load_dotenv
import requests
import os 
load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY') 
def get_swot_analysis(info,sentiment):
    prompt = f"""
    Create a SWOT analysis of the company with this context:
    🔸 Company: {info.get('shortName')}
    🔸 Sector: {info.get('sector')}
    🔸 Market Cap: {info.get('marketCap')}
    🔸 Summary: {info.get('longBusinessSummary')}
    🔸 Real-time Sentiment: {sentiment}

    Format it with clear headings:
    Strengths:
    Weaknesses:
    Opportunities:
    Threats:
    """
    
    url = "https://api.groq.com/openai/v1/chat/completions"  # endpoint
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json" 
    }
    
    data = {
        'model': 'gemma2-9b-it', 
        'messages': [{'role': 'user', 'content': prompt}]  
    }
    
    response = requests.post(url=url, headers=headers, json=data)
    response.raise_for_status()  
    return response.json()['choices'][0]['message']['content']

def final_decision(info,sentiment):
    prompt = f"""
    Based on the following information: {info}
    And the overall sentiment: {sentiment}

    What should the user do — buy the stock or wait? 
    Please give a final decision in simple and easy-to-understand language .
    """
    
    url = "https://api.groq.com/openai/v1/chat/completions"  # endpoint
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json" 
    }
    
    data = {
        'model': 'deepseek-r1-distill-llama-70b', 
        'messages': [{'role': 'user', 'content': prompt}]  
    }
    
    response = requests.post(url=url, headers=headers, json=data)
    response.raise_for_status()  
    return response.json()['choices'][0]['message']['content']