# app.py
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from openai import OpenAI
from openai._client import OpenAIError  # base error class

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = os.getenv("MODEL", "gpt-4o-mini")

markets = ["USA", "Norway", "Japan", "Germany", "UK"]

def fetch_news(query, num_articles=3):
    url = f"https://news.google.com/rss/search?q={query}+regulation&hl=en-US&gl=US&ceid=US:en"
    response = requests.get(url)

    # Try XML → fallback to HTML
    try:
        soup = BeautifulSoup(response.content, "lxml-xml")
    except Exception:
        soup = BeautifulSoup(response.content, "html.parser")

    items = soup.find_all("item")[:num_articles]

    news_list = []
    for item in items:
        title = item.title.text if item.title else "No title"
        link = item.link.text if item.link else "No link"
        news_list.append({"title": title, "link": link})

    return news_list

def summarize_article(article_title):
    prompt = f"Summarize this regulatory news article for a financial dashboard: {article_title}" 
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content

all_news = []
for market in markets:
    news = fetch_news(market)
    for article in news:
        summary = summarize_article(article["title"])
        all_news.append({
            "Market": market,
            "Title": article["title"],
            "Summary": summary,
            "Link": article["link"]
        })

df = pd.DataFrame(all_news)

st.set_page_config(page_title="NBIM Regulatory News", layout="wide")
st.title("NBIM Regulatory News Dashboard")

selected_market = st.selectbox("Select Market:", markets)
df_filtered = df[df['Market'] == selected_market]

for idx, row in df_filtered.iterrows():
    st.subheader(row["Title"])
    st.write(row["Summary"])
    st.markdown(f"[Read more]({row['Link']})")

