import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}

laughs_bread =  'https://scrape-sm1.github.io/site1/Crimson%20Bread%20Sliced%20market1super.com.html'
glomark_bread =  'https://glomark.lk/sandwich-bread-450g/p/13606'
    
laughs_tissue = 'https://scrape-sm1.github.io/site1/FLORA%20FACIAL%20TISSUES%202%20X%20160%20BOX%20-%20HOUSEHOLD%20-%20Categories%20market1super.com.html'
glomark_tissue = 'https://glomark.lk/flora-facial-tissues-160s/p/10470'
    
laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'


def compare_prices(product_laughs, product_glomark):
    
    # Parameters are the links to particular product website
    
    #TODO: Aquire the web pages which contain product Price
    laughs_response = requests.get(product_laughs)
    laughs_html = laughs_response.content
    
    glomark_response = requests.get(product_glomark)
    glomark_html = glomark_response.content

    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    laughs_soup = BeautifulSoup(laughs_html, 'html.parser')
    laughs_price = laughs_soup.find('span', {'class': 'regular-price'}).text
    product_name_laughs = laughs_soup.find('div', {'class': 'product-name'}).text.strip()
    # new = int(round(float(laughs_price.replace('Rs.', '').strip())))
    # print(product_name_laughs)

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    glomark_soup = BeautifulSoup(glomark_html, 'html.parser')
    glomark_price = glomark_soup.find_all('script')
    product_name_glomark = glomark_soup.find('div', {'class': 'product-title'}).text.strip()
    # print(product_name_glomark)
    # print(json.loads(glomark_price[6].string)['offers'][0]['price'])
    glomark_price_new = json.loads(glomark_price[6].string)['offers'][0]['price']
    
    #TODO: Parse the values as floats, and print them.
    price_laughs = float(laughs_price.replace('Rs.', '').strip())
    price_glomark = float(glomark_price_new)
    
    print('Laughs  ',product_name_laughs,'Rs.: ' ,price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' ,price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')
    
    
    
compare_prices(laughs_coconut, glomark_coconut)