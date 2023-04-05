import requests
import json


new_brand = "Araliya"


url = 'http://host1.open.uom.lk:8080/api/products/85'

headers = {'Content-Type': 'application/json'}

response = requests.get(url)
product_data = response.json()


product_data['brand'] = new_brand


response = requests.put(url, headers=headers, data=json.dumps(product_data))


print(response.json())