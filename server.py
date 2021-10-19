# import render_template to use html templates
from flask import Flask, render_template
import requests

app = Flask(__name__)

# Template string
# /api/v3/profile offers more useful info than /api/v3/stock/real-time-price
# TODO: Use more info than just price i.e. companyName, address, description, etc
API_URL = 'https://financialmodelingprep.com/api/v3/profile/{ticker}'

# fetch stock data using requests
def fetch_price(ticker):
    data = requests.get(API_URL.format(ticker=ticker), 
                        params={'apikey': '5ad5285c31ccdb3fc54dc1c1aea1907b'}).json()
    print(data)
    # data should be a dictionary with 2 keys "symbol" and "price"
    # we wanr the price
    return data[0]["price"]

# Take a ticker symbol and return informative string about price 
# capture symbol in URL as parameter
@app.route('/stock/<ticker>')
def stock(ticker):
    ticker = ticker.upper()
    price = fetch_price(ticker)
    return render_template('stock.html', ticker=ticker, price=price)

@app.route('/')
def home_page():
    return render_template('index.html')