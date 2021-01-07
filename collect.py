from bs4 import BeautifulSoup
import requests

root = "http://ge-tracker.com/item/"

def parse(items):
    prices= {}

    for item in items:
        page = requests.get(root + item)

        soup = BeautifulSoup(page.content,'html.parser')

        sell = soup.find('td',attrs={'id':'item_stat_sell_price'})
        sell_text = sell.text.replace("\n", "").replace(",","").strip()
        prices[item] = int(sell_text)

    return prices
