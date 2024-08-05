

from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
import yfinance as yf
import pandas as pd


from datetime import datetime
import numpy as np
import finpy_tse as fpy
import pytse_client as tse
import requests
import asyncio



###########################

def yahoo_symbol(symbol="BTC-USD", timeframe='1d'):
    try:
        data = yf.download(symbol, period='max', interval=timeframe)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

def btc(request):
    data = yahoo_symbol(symbol="BTC-USD")


    if data.empty:
        raise Http404("Data not found")
    
    # Convert the DataFrame to JSON format
    data_json = data.reset_index().to_json(orient='split')
    context = {
        "data_json": data_json
    }
    
    return render(request, "market/btc.html", context)




def gold(request):
    data = yahoo_symbol(symbol="GC=F")
    if data.empty:
        raise Http404("Data not found")
    
    data_json = data.to_json(orient='split')  # Convert DataFrame to JSON format
    context = {
        "data_json": data_json
    }
    
    return render(request, "market/gold.html", context)




last_day =datetime.now()
last_day=last_day.date()
last_day=str(last_day)
last_day


def index_kol(bars:int=9500):
        while True:
            try:
                data=fpy.Get_CWI_History(ignore_date=True,double_date=True)
                data=data.iloc[:-bars:-1][::-1]
                return data
            except Exception as e:
                print(f"An error occurred: {e}")
                asyncio.sleep(2)  # Sleep for 10 seconds before retrying





def boors(request):
    data =index_kol()
    if data.empty:
        raise Http404("Data not found")
    
    # Convert the DataFrame to JSON format
    data_json = data.reset_index().to_json(orient='split')
    context = {
        "data_json": data_json
    }
    
    return render(request, "market/boors.html", context)









def saham_price(symbol='طلا',bars:int=9500):
    while True:
        try:
                
            data=fpy.Get_Price_History(stock=symbol,ignore_date=True,adjust_price=True,double_date= True)
            data=data.iloc[:-bars:-1][::-1]
            # data.index=data['Date']
            return(data)

        except Exception as e:
            print(f"An error occurred: {e}")
            asyncio.sleep(2)  # Sleep for 10 seconds before retrying








def tala(request):
    data=saham_price(symbol='طلا')
    data=pd.DataFrame(data)
    if data.empty:
        raise Http404("Data not found")
    
    # Convert the DataFrame to JSON format
    data_json = data.reset_index().to_json(orient='split')
    context = {
        "data_json": data_json
    }
    
    return render(request, "market/tala.html", context)






def ahrom(request):
    data=saham_price(symbol='اهرم')
    data=pd.DataFrame(data)
    if data.empty:
        raise Http404("Data not found")
    
    # Convert the DataFrame to JSON format
    data_json = data.reset_index().to_json(orient='split')
    context = {
        "data_json": data_json
    }
    
    return render(request, "market/ahrom.html", context)


