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

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

# +
# # Ustawienia Streamlit
# now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# st.write(f"[{now}]")
# st.title("BTC/USD \n")



# @st.cache_data(ttl=3600)
# def get_btc_data():
    
#     st.write(f"Downloaded: {now}")
#     btc_data = yf.download("BTC-USD", period="10y", interval="1d")
#     return btc_data



# # Pobranie danych BTC z yfinance
# btc_data = get_btc_data()

# # Tworzenie wykresu
# fig = go.Figure()

# fig.add_trace(go.Scatter(
#     x=btc_data.index,
#     y=btc_data['Close'],
#     mode='lines+markers',
#     name='BTC/USD',
#     line=dict(color='red', width=1),  # Cieńsza linia
#     marker=dict(size=1)  # Rozmiar markerów
# ))

# # Ustawienia wykresu
# fig.update_layout(
#     title="Kurs BTC/USD",
#     xaxis_title="Data",
#     yaxis_title="Cena (USD)",
#     plot_bgcolor='rgba(240, 240, 240, 0.85)',  # Tło wykresu
#     paper_bgcolor='rgba(240, 240, 240, 0.85)',  # Tło papieru
#     xaxis=dict(showgrid=True, gridcolor='Blue',griddash='dash' ),  # Siatka na osi X
#     yaxis=dict(showgrid=True, gridcolor='LightGray', type='log'),  # Siatka na osi Y
#     legend=dict(x=0, y=1.0),  # Pozycja legendy
#     hovermode='x unified'  # Tryb podpowiedzi
# )

# # Wyświetlenie wykresu
# st.plotly_chart(fig)



# +
# import streamlit as st
# import yfinance as yf
# import plotly.graph_objects as go
# from datetime import datetime
# import numpy as np

# # Ustawienia Streamlit
# st.title("Wykres kursu BTC/USD")
# st.write(f"Data i godzina pobrania: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# # Daty halvingów
# halving_dates = [
#     datetime(2012, 11, 28),
#     datetime(2016, 7, 9),
#     datetime(2020, 5, 11),
#     datetime(2024, 4, 15)  # Przewidywana data
# ]

# # Funkcja do pobierania danych BTC z yfinance z cache
# @st.cache_data(ttl=3600)  # Cache na 3600 sekund (1 godzina)
# def get_btc_data():
#     return yf.download("BTC-USD", period="max", interval="1d")  # Maksymalny okres i interwał dzienny

# # Pobranie danych
# btc_data = get_btc_data()

# # Tworzenie wykresu
# fig = go.Figure()

# # Ustalanie kolorów dla halvingów
# colors = ['red', 'yellow', 'blue']
# halving_dates.append(btc_data.index[-1])  # Dodaj ostatnią datę do końca wykresu

# # Przygotowanie danych do rysowania wykresu
# x = btc_data.index
# y = btc_data['Close']

# # Interpolacja kolorów
# color_scale = []
# num_colors = len(colors) - 1  # Ilość kolorów między halvingami

# for i in range(len(x)):
#     # Zmienna, aby przechowywać odległość od najbliższego halvingu
#     closest_halving_idx = np.searchsorted(halving_dates, x[i]) - 1
#     closest_halving_idx = max(0, closest_halving_idx)  # Upewnij się, że nie jest ujemne

#     # Obliczanie proporcji do interpolacji
#     if closest_halving_idx < num_colors:
#         color_ratio = (x[i] - halving_dates[closest_halving_idx]) / (
#             halving_dates[closest_halving_idx + 1] - halving_dates[closest_halving_idx]
#         )
#         color_ratio = min(max(color_ratio, 0), 1)  # Ogranicz do zakresu 0-1
#         color = f'rgba({int((1 - color_ratio) * 255)}, {int(color_ratio * 255)}, 0, 1)'  # Interpolacja kolorów
#     else:
#         color = 'rgba(0, 0, 255, 1)'  # Ostatni kolor na końcu wykresu

#     color_scale.append(color)

# # Tworzenie wykresu z kolorami
# fig.add_trace(go.Scatter(
#     x=x,
#     y=y,
#     mode='lines',
#     line=dict(width=2, color='rgba(0, 0, 0, 0)'),  # Przezroczysta linia
# ))

# # Dodanie kolorowych segmentów
# for i in range(len(x) - 1):
#     fig.add_trace(go.Scatter(
#         x=[x[i], x[i + 1]],
#         y=[y[i], y[i + 1]],
#         mode='lines',
#         line=dict(color=color_scale[i], width=2),
#         showlegend=False
#     ))

# # Ustawienia wykresu
# fig.update_layout(
#     title="Kurs BTC/USD z kolorami halvingów",
#     xaxis_title="Data",
#     yaxis_title="Cena (USD)",
#     plot_bgcolor='rgba(240, 240, 240, 0.85)',  # Tło wykresu
#     paper_bgcolor='white',  # Tło papieru
#     xaxis=dict(showgrid=True, gridcolor='LightGray', griddash='dash'),  # Przerywana siatka na osi X
#     yaxis=dict(
#         showgrid=True, 
#         gridcolor='LightGray', 
#         type='log'  # Ustawienie skali logarytmicznej na osi Y
#     ),
#     legend=dict(x=0, y=1.0),  # Pozycja legendy
#     hovermode='x unified'  # Tryb podpowiedzi
# )

# # Wyświetlenie wykresu
# st.plotly_chart(fig)


# +
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

# Ustawienia Streamlit
st.title("BTC/USD.GICL2.")
st.write(f"Data i godzina pobrania: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")





# +
import streamlit as st
import plotly.express as px
import plotly.io as pio
import io
import urllib.parse

# Przykładowy wykres Plotly
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

# Zapisz wykres jako plik PNG w pamięci
img = io.BytesIO()
pio.write_image(fig, img, format='png')
img.seek(0)

# Wyświetl wykres w aplikacji Streamlit
st.plotly_chart(fig)

# Przycisk do pobrania pliku z unikalnym kluczem
st.download_button(
    label="Pobierz wykres jako PNG",
    data=img,
    file_name="wykres.png",
    mime="image/png",
    key="download_png"
)

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

# # Daty halvingów
# halving_dates = [
#     datetime(2012, 11, 28),
#     datetime(2016, 7, 9),
#     datetime(2020, 5, 11),
#     datetime(2024, 4, 15)  # Przewidywana data
# ]

# # Funkcja do pobierania danych BTC z yfinance z cache
# @st.cache_data(ttl=3600)  # Cache na 3600 sekund (1 godzina)
# def get_btc_data():
#     return yf.download("BTC-USD", period="max", interval="1d")  # Maksymalny okres i interwał dzienny

# # Pobranie danych
# btc_data = get_btc_data()

# # Inicjalizacja kolumn
# btc_data['Months Since Halving'] = 0
# btc_data['Color'] = '#FF0000'  # Domyślny kolor

# # Obliczenia dla każdego przedziału halvingów
# for i in range(len(halving_dates) - 1):
#     start_date = halving_dates[i]
#     end_date = halving_dates[i + 1]

#     # Filtracja danych w tym przedziale
#     mask = (btc_data.index >= start_date) & (btc_data.index < end_date)

#     # Obliczanie liczby miesięcy od ostatniego halvingu
#     months_passed = ((btc_data.index[mask].year - start_date.year) * 12 + 
#                      (btc_data.index[mask].month - start_date.month))

#     # Ustalanie koloru w zależności od liczby miesięcy
#     for j in range(len(months_passed)):
#         if months_passed[j] < 5:  # 0-4 miesiące
#             btc_data['Color'][mask][j] = '#FF0000'  # Czerwony
#         elif months_passed[j] < 10:  # 5-9 miesięcy
#             btc_data['Color'][mask][j] = '#FFA500'  # Pomarańczowy
#         elif months_passed[j] < 15:  # 10-14 miesięcy
#             btc_data['Color'][mask][j] = '#FFFF00'  # Żółty
#         elif months_passed[j] < 20:  # 15-19 miesięcy
#             btc_data['Color'][mask][j] = '#008000'  # Zielony
#         else:  # 20+ miesięcy
#             btc_data['Color'][mask][j] = '#0000FF'  # Niebieski

#     # Ustawianie liczby miesięcy od halvingu w kolumnie
#     btc_data['Months Since Halving'][mask] = months_passed

# # Tworzenie wykresu
# fig = go.Figure()

# # Dodajemy jeden trace z danymi kolorów
# fig.add_trace(go.Scatter(
#     x=btc_data.index,
#     y=btc_data['Close'],
#     mode='lines',
#     line=dict(width=2),
#     marker=dict(color=btc_data['Color']),  # Kolory z kolumny 'Color'
#     showlegend=False
# ))

# # Ustawienia wykresu
# fig.update_layout(
#     title="Kurs BTC/USD z kolorami halvingów",
#     xaxis_title="Data",
#     yaxis_title="Cena (USD)",
#     plot_bgcolor='rgba(240, 240, 240, 0.85)',  # Tło wykresu
#     paper_bgcolor='white',  # Tło papieru
#     xaxis=dict(showgrid=True, gridcolor='LightGray', griddash='dash'),  # Przerywana siatka na osi X
#     yaxis=dict(
#         showgrid=True, 
#         gridcolor='LightGray', 
#         type='log'  # Ustawienie skali logarytmicznej na osi Y
#     ),
#     legend=dict(x=0, y=1.0),  # Pozycja legendy
#     hovermode='x unified'  # Tryb podpowiedzi
# )

# # Wyświetlenie wykresu
# st.plotly_chart(fig)
# -






