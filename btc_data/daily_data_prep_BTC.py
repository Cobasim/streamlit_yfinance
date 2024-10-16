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

import pandas as pd
from datetime import datetime
import numpy as np
from tqdm import tqdm

# # CONST

BTC_DAILY_FILE = '../btc_data/BTC_DAILY.pck'
BTC = '../btc_data/BTC.pck'


# # DEfs

def get_btc_daily_file():
    # Load file
    pck_file = BTC_DAILY_FILE
    df = pd.read_pickle(pck_file)
    
    df.columns=['BTC']
    df.sort_index(ascending=True, inplace=True)
    
    # Dodaj date str
    df['str_date'] = df.index.astype(str)
    
    # Dodaj date w foramcie datetime.date
    df['dt_date'] = [datetime.strptime(str_date, '%Y-%m-%d').date() for str_date in df.str_date]
    
    # Ustal index na format dt
    # df.reset_index(drop=False, inplace=True)
    df.index = df.dt_date
    df.index = pd.to_datetime(df.index).date

    df.drop(columns=['str_date', 'dt_date'], inplace=True)
    return df


def get_all_halvings_dt():
    
    halvings_str = ['08-11-2012', '09-07-2016', '11-05-2020', '19-04-2024', '16-03-2028', '20-02-2032', 
                '25-01-2036', '29-12-2039', '04-12-2043', '08-11-2047', '14-10-2051', '18-09-2055', 
                '23-08-2059', '27-07-2063', '01-07-2067', '05-06-2071', '09-05-2075', '14-04-2079', 
                '18-03-2083', '22-02-2087', '27-01-2091', '01-01-2095', '06-12-2098', '10-11-2102', 
                '16-10-2106', '20-09-2110', '25-08-2114', '30-07-2118', '03-07-2122', '07-06-2126',
                '12-05-2130', '16-04-2134', '20-03-2138', '24-02-2142']

    halvings_dt = [datetime.strptime(str_date, "%d-%m-%Y").date() for str_date in halvings_str]

    return halvings_dt



# # Main DEfs

def prepare_BTC_file_for_analytics():
    
    df = get_btc_daily_file()
    halvings_dt = get_all_halvings_dt()

    start_date = '01/03/2009'  # First BTC block
    end_date = '01/05/2052'    # Last BTC dig
        
    date_range = pd.date_range(start=start_date, end=end_date)
    
    print(f'Range: >>{start_date} - {end_date}<<.')
    
    ad = {}
    for i in tqdm(date_range):
        ad[i] = np.NaN
    
    egg = pd.DataFrame([ad]).T
    egg.rename_axis('dt_date', inplace=True)
    egg.columns = ['h'] # <- zero w halving date
    egg['h'] = np.nan
    egg.sort_index(ascending=True, inplace=True)
    egg.index = pd.to_datetime(egg.index).date
    
    # Ustawienie wartości 0 w dniach halvingów
    egg.loc[egg.index.isin(halvings_dt), 'h'] = 0
    # egg.at['2009-01-03', 'h'] = 0  #<- zero at first day
    egg.iat[0, egg.columns.get_loc('h')] = 0
    
    # dfh <- days from halving
    egg['dfh'] = (egg['h'].ffill() + egg.groupby(egg['h'].eq(0).cumsum()).cumcount() )
    egg.drop(columns=['h'], inplace=True)
    
    # e <- halving epochs
    egg['e'] = (egg['dfh'] == 0).cumsum()
    
    # Dodaj kolumne BTC oraz dane z DF
    egg['BTC'] = -999.0
    egg.update(df)
    
    # Usun wiersze bez danych
    egg = egg[egg.index>=df.index.min()]
    egg = egg[egg.index<=df.index.max()]
    
    print(f'Final range: >>{egg.index.min()} - {egg.index.max()}<<.')
    # Check for err
    egg = egg.replace([np.inf, -np.inf], np.nan)
    print(f'Nan/inf in file:{egg.isna().sum().sum()}.')
    assert egg.isna().sum().sum() == 0
    
    egg.to_pickle(BTC)
    print(f'File prepared:>>{BTC}<<.')

    return egg


# # MAIN



# +
#--------------------------------------
# Prepare clean BTC.pck file
# with all data needed for s2f analytics
#--------------------------------------

df = prepare_BTC_file_for_analytics()
display(df.head(3))
display(df.tail(3))
# -




