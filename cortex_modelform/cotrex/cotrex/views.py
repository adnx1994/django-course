from django.shortcuts import render
from django.http import Http404
from .forms import searcherForm




#######################################################################################
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



#######################################################################################


# def index(request):
#    if  (request.method=="POST"):
#           print(request.POST["searcher"])
          
#    return render(request,"index.html")



#######################################################################################



# def index(request):
#     if request.method=='POST' :
#             searcher_form= searcherForm(request.POST)
#             if searcher_form.is_valid():
#                 print(searcher_form.cleaned_data)
#                 searcher=searcher_form.cleaned_data.get("searcher")
#                 print(str(searcher))

                 
#     else:
#         searcher_form= searcherForm()
#     return render(request,"index.html",{
#         'searcher_form' :searcher_form,

#     })
    
    
    
    
    
 #######################################################################################   
    

def index(request):
    searcher_form = searcherForm()

    if request.method == 'POST':
        searcher_form = searcherForm(request.POST)
        if searcher_form.is_valid():
            searcher = searcher_form.cleaned_data.get("searcher")
            print(str(searcher))
        else:
            searcher = None  # یا هر مقدار پیش‌فرض دیگری

    else:
        searcher = None  # یا هر مقدار پیش‌فرض دیگری

    if searcher:
        try:
            data = fpy.Get_Price_History(stock=str(searcher), ignore_date=True, adjust_price=True, double_date=True)
            data = data.iloc[:-9500:-1][::-1]
            data.index = data["Date"]

            if data.empty:
                raise Http404("Data not found")

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

        except Exception as e:
            print(f"An error occurred: {e}")
            fig_json = None

    else:
        fig_json = None  # در صورتی که هیچ داده‌ای وجود ندارد

    return render(request, "index.html", {
        'searcher_form': searcher_form,
        'fig_json': fig_json,
    })










