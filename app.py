from flask import Flask,render_template
from web3 import Web3
import requests

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/20cd6a62a8d345dbbd32882cb9306222'))
app = Flask(__name__)


@app.route("/")
def index():
    return "<p> index </p>"

#0x495f947276749Ce646f68AC8c248420045cb7b5e
@app.route("/top10/<hash>")
def top10(hash):
    url = "https://api.opensea.io/api/v1/assets"

    querystring = {"asset_contract_address": hash,
                   "order_direction": "desc",
                   "order_by": "sale_count",
                   "offset": "0",
                   "limit": "10"
                   }

    response = requests.request("GET", url, params=querystring)
    processed_response = response.json()

    top10 = []
    for x in range(10):
        price = int(processed_response['assets'][x]['last_sale']['total_price'])
        top10.append(price / 10 ** 18)
    return render_template("top10.html", top10=top10)