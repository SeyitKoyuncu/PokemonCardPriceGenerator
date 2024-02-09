import requests
from bs4 import BeautifulSoup

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found ")

query = "toxicroak #166"

url_list = []
for url in search(query, tld="co.in", num=10, stop=10, pause=2):
    if 'www.pricecharting.com' in url:
        url_list.append(url)

print("Which card type's price you want to search: ")
i = 1
for url in url_list:
    splitted_url = url.split('/')
    print(f"{i}- {splitted_url[len(splitted_url)-1]}")
    i=i+1
user_card_type_choice = int(input()) - 1
print(f"You choice to the this card type: {(url_list[user_card_type_choice].split('/'))[len(url_list[user_card_type_choice].split('/'))-1]}")

# We need to info from <div id = "game-page"> -> <table id = "price_data"> -> <tr> -> <td id = "used_price"> -> <span class = "price js-price">
# Take all prices from <div id = "game-page"> -> <table id = "price_data"> -> <tr>

# TODO Will creating method and, make dynamic for spesific cards
URL = url_list[user_card_type_choice]
print(URL)
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify()) #Print the html in string format
scrapping_prices = soup.find('table', attrs={'id':'price_data'}).find_all('span', attrs = {'class':'price js-price'})
print(scrapping_prices)
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

for key in prices_dict:
    print(f"type = {key}, price = {prices_dict[key]}")
