from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/arb/<ticker>', methods=['GET'])
def arbitrage(ticker):
  print(f'Ticker: {ticker}')

  return f"<h2>{ticker}</h2>"

@app.route('/currency/map', methods=['GET'])
def currency_map():
  symbol = request.args.get('symbol')
  r = requests.get(f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?symbol={symbol}', headers={ 
      "X-CMC_PRO_API_KEY": os.environ.get('CMC_API_KEY') 
    })

  return r.json()

if __name__ == '__main__':
  app.run(port=5000, debug=True)