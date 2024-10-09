# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

from datetime import datetime
import pandas as pd
import urllib.parse
# -

# Ustawienia Streamlit
st.title("BTC/USD.GICL4.")
st.write(f"TIME_: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


# +
# Przykładowy wykres Plotly
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

# Wyświetl wykres w aplikacji Streamlit
st.plotly_chart(fig)


# Tworzenie linku do tweeta z adresem Twojej aplikacji Streamlit
tweet_text = "Zobacz mój najnowszy wykres w aplikacji Streamlit! #dataanalysis"
tweet_text_encoded = urllib.parse.quote(tweet_text)  # Zakodowanie treści tweeta

# Twój URL aplikacji Streamlit lub inny link
app_url = "https://twoja-aplikacja-streamlit-link.com"
app_url_encoded = urllib.parse.quote(app_url)  # Zakodowanie URL-a

# Tworzenie pełnego URL-a do tweetowania
tweet_url = f"https://twitter.com/intent/tweet?text={tweet_text_encoded}&url={app_url_encoded}"

# Przycisk do Tweetowania z unikalnym kluczem
if st.button('Tweet', key="tweet_button"):
    st.write(f"[Kliknij tutaj, aby opublikować tweeta!]( {tweet_url})")



# +



# -










