
# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from datetime import datetime
import numpy as np
import finpy_tse as fpy
import pytse_client as tse
import requests
import asyncio
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots


#####################################################################################


def yahoo_symbol(symbol="BTC-USD", timeframe='1d'):
    while True:
        try:
            data = yf.download(symbol, period='max', interval=timeframe)
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            asyncio.sleep(2)  # Sleep for 10 seconds before retrying
            return pd.DataFrame()  # Return an empty DataFrame in case of error





def btc(request):
    data = yahoo_symbol(symbol="BTC-USD")

    if data.empty:
        raise Http404("Data not found")
    
    # Create a candlestick chart using Plotly
    fig = make_subplots(rows=1, cols=1)

    candlestick = go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    )
    
    fig.add_trace(candlestick)
    
    fig.update_layout(
        title='Bitcoin Price',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False
    )
    
    # Convert the figure to JSON format
    fig_json = fig.to_json()
    
    context = {
        "fig_json": fig_json
    }
    
    return render(request, "chart/btc.html", context)







#####################################################################################



def gold(request):
    data = yahoo_symbol(symbol="GC=F")

    if data.empty:
        raise Http404("Data not found")
    
    # Create a candlestick chart using Plotly
    fig = make_subplots(rows=1, cols=1)

    candlestick = go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    )
    
    fig.add_trace(candlestick)
    
    fig.update_layout(
        title='XAUUSD Price',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False
    )
    
    # Convert the figure to JSON format
    fig_json = fig.to_json()
    
    context = {
        "fig_json": fig_json
    }
    
    return render(request, "chart/gold.html", context)


#####################################################################################


last_day =datetime.now()
last_day=last_day.date()
last_day=str(last_day)





def boors(request):
    while True:
        try:
            data=fpy.Get_CWI_History(ignore_date=True,double_date=True)
            data=data.iloc[:-9500:-1][::-1]
            data.index=data["Date"]

            if data.empty:
                raise Http404("Data not found")
        except Exception as e:
            print(f"An error occurred: {e}")
            asyncio.sleep(2)  # Sleep for 10 seconds before retrying    
            
    
        # Create a candlestick chart using Plotly
        fig = make_subplots(rows=1, cols=1)

        candlestick = go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close']
        )
        
        fig.add_trace(candlestick)
        
        fig.update_layout(
            title='boors Price',
            xaxis_title='Date',
            yaxis_title='Price (index)',
            xaxis_rangeslider_visible=False
        )
        
        # Convert the figure to JSON format
        fig_json = fig.to_json()
        
        context = {
            "fig_json": fig_json
        }
        
        return render(request, "chart/boors.html", context)






#####################################################################################



def tala(request):
    while True:
        try:
            data=fpy.Get_Price_History(stock="طلا",ignore_date=True,adjust_price=True,double_date= True)
            data=data.iloc[:-9500:-1][::-1]
            data.index=data["Date"]

            if data.empty:
                raise Http404("Data not found")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            asyncio.sleep(2)  # Sleep for 10 seconds before retrying    
            
    
        # Create a candlestick chart using Plotly
        fig = make_subplots(rows=1, cols=1)

        candlestick = go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Adj Close']
        )
        
        fig.add_trace(candlestick)
        
        fig.update_layout(
            title='tala Price',
            xaxis_title='Date',
            yaxis_title='Price (rial)',
            xaxis_rangeslider_visible=False
        )
        
        # Convert the figure to JSON format
        fig_json = fig.to_json()
        
        context = {
            "fig_json": fig_json
        }
        
        return render(request, "chart/tala.html", context)








#####################################################################################





def ahrom(request):
        while True:
            try:
                data=fpy.Get_Price_History(stock="اهرم",ignore_date=True,adjust_price=True,double_date= True)
                data=data.iloc[:-9500:-1][::-1]
                data.index=data["Date"]

                if data.empty:
                    raise Http404("Data not found")
    
    
            except Exception as e:
                print(f"An error occurred: {e}")
                asyncio.sleep(2)  # Sleep for 10 seconds before retrying    
    
            # Create a candlestick chart using Plotly
            fig = make_subplots(rows=1, cols=1)

            candlestick = go.Candlestick(
                x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Adj Close']
            )
            
            fig.add_trace(candlestick)
            
            fig.update_layout(
                title='tala Price',
                xaxis_title='Date',
                yaxis_title='Price (rial)',
                xaxis_rangeslider_visible=False
            )
            
            # Convert the figure to JSON format
            fig_json = fig.to_json()
            
            context = {
                "fig_json": fig_json
            }
            
            return render(request, "chart/ahrom.html", context)
        
        
        
        
#################################################
##################################################
####################################################


