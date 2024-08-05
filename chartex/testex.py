
import yfinance as yf
import asyncio


# Create your views here.

def yahoo_symbol(symbol="BTC-USD",timeframe='1d'):
    while True:
        try:
            data = yf.download(symbol,period='max',interval= timeframe)
            return(data)
        except Exception as e:
            print(f"An error occurred: {e}")
            asyncio.sleep(2)  # Sleep for 10 seconds before retrying








def btc():
    data=yahoo_symbol(symbol="BTC-USD")
    
    # data=dict(data)
    print(data)
    


btc()


