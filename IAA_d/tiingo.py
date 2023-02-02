import datetime

import requests
from django.shortcuts import render
from datetime import date
from datetime import timedelta
from datetime import datetime
headers={
    'Content-Type':'application/json',
    'Authorization':'Token 986866c741f8014a33d7147ffa39f35eb90963a8'
}
def get_price_data(ticker):
    t=date.today()
    m=t.month
    y=t.year
    sd=str(y)+"-"+str(m)+"-"+str(1)
    url="https://api.tiingo.com/tiingo/daily/{}/prices?startDate={}&endDate={}".format(ticker,sd,t)
    response = requests.get(url, headers=headers).json()
    return response
def get_today_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices".format(ticker)
    response = requests.get(url, headers=headers).json()
    return response
def get_meta_data(ticker):
    url="https://api.tiingo.com/tiingo/daily/{}".format(ticker)
    response =requests.get(url,headers=headers)
    return response.json()
def get_intraday_data(ticker):
    today = date.today()
    d= today - timedelta(days=1)
    url="https://api.tiingo.com/iex/{}/prices?startDate=2021-5-12&resampleFreq=5min".format(ticker)
    response=requests.get(url,headers=headers).json()
    return response
