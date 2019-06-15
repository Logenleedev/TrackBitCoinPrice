import requests
import json



url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
iftt_webhook_url = 'https://maker.ifttt.com/trigger/{}/with/key/cpQXOTgApgT5hbuH4IutA3'

def get_bitcoin_price( ):
      
    parameters = {
      'symbol': 'BTC',
      'CMC_PRO_API_KEY': '56a500d0-51f5-4790-805b-84ba539de7a5'
    }

    response = requests.get(url, params=parameters)

    data = json.loads(response.text)
    
    return float(data[0]['price_usd'])


def post_ifttt_webhook(event, value):
    
    data = {'value1': value}

    ifttt_event_url = iftt_webhook_url.format(event)

    requests.post(ifttt_event_url, json=data)
