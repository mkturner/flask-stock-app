from flask import Flask
import requests

app = Flask(__name__)

# Template string
API_URL = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{ticker}'

# fetch stock data using requests
def fetch_price(ticker):
    data = requests.get(API_URL.format(ticker=ticker.upper()), 
                        params={'apikey': '5ad5285c31ccdb3fc54dc1c1aea1907b'}).json()
    
    # data should be a dictionary with 2 keys "symbol" and "price"
    # we wanr the price
    return data["price"]

# Take a ticker symbol and return informative string about price 
# capture symbol in URL as parameter
@app.route('/stock/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return "The price of {ticker} is {price}".format(ticker=ticker, price=price)

@app.route('/')
def home_page():
    return 'Try /stock/AAPL'