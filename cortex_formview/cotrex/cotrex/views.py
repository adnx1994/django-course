from django.shortcuts import render
from django.http import Http404
from .forms import searcherForm
from django.views import View
from django.views.generic.edit import FormView


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



class indexView(FormView):
    template_name = "index.html"
    form_class = searcherForm
    success_url = "/"

    def form_valid(self, form):
        searcher = form.cleaned_data.get("searcher")
        print(str(searcher))

        try:
            data = fpy.Get_Price_History(stock=str(searcher), ignore_date=True, adjust_price=True, double_date=True)
            data = data.iloc[:-9500:-1][::-1]
            data.index = data["Date"]

            if data.empty:
                raise Http404("Data not found")

            # ساختن نمودار شمعی با استفاده از Plotly
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

            # تبدیل نمودار به فرمت JSON
            fig_json = fig.to_json()

        except Exception as e:
            print(f"An error occurred: {e}")
            fig_json = None

        return self.render_to_response(self.get_context_data(form=form, fig_json=fig_json))

    def form_invalid(self, form):
        # اگر فرم معتبر نبود، صفحه با فرم غیر معتبر رندر می‌شود.
        return self.render_to_response(self.get_context_data(form=form, fig_json=None))

