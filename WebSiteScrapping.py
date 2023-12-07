import requests
from bs4 import BeautifulSoup

# We need to info from <div id = "game-page"> -> <table id = "price_data"> -> <tr> -> <td id = "used_price"> -> <span class = "price js-price">
# Take all prices from <div id = "game-page"> -> <table id = "price_data"> -> <tr>

# TODO Will creating method and, make dynamic for spesific cards
URL = "https://www.pricecharting.com/game/pokemon-fusion-strike/schoolboy-276?q=schoolboy+%23276#completed-auctions-used"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify()) Print the html in string format
scrapping_prices = soup.find('table', attrs={'id':'price_data'}).find_all('span', attrs = {'class':'price js-price'})

prices_dict = {
    "Ungraded": "",
    "Grade 7": "",
    "Grade 8": "",
    "Grade 9": "",
    "Grade 9.5": "",
    "PSA 10": ""
}

i = 0
list_of_prices = []
for price in scrapping_prices:
    if(i == 6):
        break
    prices_dict[list(prices_dict.keys())[i]] = (price.text).strip()
    i = i + 1


