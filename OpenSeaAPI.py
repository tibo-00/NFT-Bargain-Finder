import requests
from web3 import Web3

url = "https://api.opensea.io/api/v1/assets"

querystring = {"asset_contract_address": "0x495f947276749Ce646f68AC8c248420045cb7b5e",
               "order_direction": "desc",
               "order_by":"sale_count",
               "offset": "0",
               "limit": "10"
               }

response = requests.request("GET", url, params=querystring)
processed_response = response.json()

top10 = []
for x in range(10):
    price = int(processed_response['assets'][x]['last_sale']['total_price'])
    top10.append(price/10**18)

print(top10)
