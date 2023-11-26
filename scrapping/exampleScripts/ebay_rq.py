import requests
from bs4 import BeautifulSoup

def ebay_url(poke_name, card_type, foil_type, psa_num):
    '''Function that return a url for the ebay request
        poke_name = "charizard"
        card_type = "vmax"
        foil_type = "rainbow"
    '''
    poke_search = poke_name + "+"
    card_type_search = card_type + "+"
    foil_search = foil_type + "+"
    psa_search = "psa+" + str(psa_num)
    ebay_search = poke_search + card_type_search + foil_search + psa_search
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_TitleDesc=0&_nkw={ebay_search}&rt=nc&LH_Sold=1&LH_Complete=1"
    ebay_search = ebay_search.replace("+", "_")
    return [ebay_search, url]

def number_pages(soup):
    '''Function that return the number of pages'''
    pageNumber = soup.find('ol', {'class': 'pagination__items'})
    pNumber = pageNumber.find_all('li')
    for i in pNumber:
        number = i.text
    return number

def  get_data(url):
    """
    this module takes url as parameter, and creats a soup object
    and returns it
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

# Example of how to use the function:
# poke_name should be a string with the pokemon name
poke_name = "charizard"
# card_type should be a string with the type of ultra rare and secret pokémon cards
# example: vmax, gx, etc.
card_type = "vmax"
# foil_type should be a string with the foil type of the card
foil_type = "rainbow"
# psa should be a int (can be string) with the grade of psa
psa = 10


list_url = ebay_url(poke_name, card_type, foil_type, psa)
print(list_url)
# This will be used to name the json file

soup = get_data(list_url[1])

print(number_pages(soup))