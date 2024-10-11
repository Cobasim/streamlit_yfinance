# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import requests
import pandas as pd
from datetime import datetime
from tqdm import tqdm

# # CONSt

BTC_DAILY_FILE = 'BTC_DAILY.pck'
start_date = '18/07/2010'


# # DEfs

# +
def ts_from_date(date_str):
    # Przykładowa data\

    # date_str = '2020-10-30'
    
    
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Konwersja daty na znacznik czasu
    ts = int(date.timestamp())
    
    # print("Znacznik czasu:", ts)
    return ts

    
def date_from_ts(ts):

    date_str = datetime.fromtimestamp(ts).date()
    return date_str


def get_btc_value_by_date(str_date):
    # str_date = '2020-10-10'
    ts = ts_from_date(str_date)
    
    url = f'https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD&ts={ts}'
    
    resp = requests.get(url)
    btc_value = eval(resp.text)['BTC']['USD']

    return btc_value

def err_test():
    ts = ts_from_date('2010-10-09')
    
    url = f'https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD&ts={ts}'
    
    resp = requests.get(url)
    print(resp)
    print(resp.text)
    print('-'*80)


# -

# # Main DEfs

def update_btc_file():
    '''
    #--------------------------------------
    # MAIN DOWNLOADING / UPDATING LOOP
    # u can reset kernel any time and start over
    # file just keeps fillig blank spaces
    #--------------------------------------
    start_date set for '18/07/2010' (max from cryptocompare) till today
    url = f'https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD&ts={ts}' (ts - linux date)
    '''
    #---------------------------------
    
    #---------------------------------
    err_code = 0
    #---------------------------------
    today = datetime.today().strftime("%d/%m/%Y")
    
    date_range = pd.date_range(start=start_date, end=today)
    print('Downloading BTC USD daily from cryptocompare.com')
    print(f'Range: from start:{start_date} - today:{today}.')
    
    INIT_DICT = False
    if INIT_DICT:
        btc_dict = {}
    else:
        btc_dict = dict(pd.read_pickle(BTC_DAILY_FILE)[0])
    
    # display only date using date() function
    for i in tqdm(date_range):
        #--------------------
        try:
            # print()
            str_date = str(i.date())
        
            if str_date in btc_dict.keys():
                # print(f'.', end='')
                pass
            else:
                ts = ts_from_date(str_date)
                
                url = f'https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD&ts={ts}'
                resp = requests.get(url)
                
                if resp.status_code == 200:
                    btc_value = eval(resp.text)['BTC']['USD']
                
                    btc_dict[str_date] = btc_value
            
                    # DUMP
                    df = pd.DataFrame([btc_dict]).T
                    df.sort_index(ascending=True, inplace= True)
                    df.to_pickle(BTC_DAILY_FILE)
                else:
                    err_code = f"Response err code other than 200 :{resp.status_code}"
                    
                    break
            
                
        except:
            print('@', end='')
    
    #-----------------
    # ENDING
    print('-'*80)
    if err_code != 0:
        print(err_code)
    else:
        print(f'DONE! {start_date} - {today}. Stored in >>{BTC_DAILY_FILE}<<. No errors.')

# # Main

# +
#--------------------------------------
# Test - if failed than serwer just died 
# probably of too many requests/day
#--------------------------------------
err_test()

#--------------------------------------
# Run loop
#--------------------------------------
update_btc_file()
# -




