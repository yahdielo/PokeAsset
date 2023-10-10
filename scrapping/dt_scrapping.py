import datetime
import json
from unittest import result
import requests
from bs4 import BeautifulSoup

""" 
This module contains multiple function to automate the process of scrapping ebay sell data of pokemon cards.

@def: get_soup() pass url and retuns a soup object
    @params: url of the ebay sells site you want to scrappe.
    @note: we search the url of ebay sells items, where you can see all the sold items,
    and from there we proceded to modify the request changing the items name, in to something secific like :
    *charizard brillain star v alt art
@def: parse() this function scrappes the sell price, date sold, and title of each element of the site.
    @params: soup object
@def: page_number() usually their is multiple pages of data, this function , look how many pages of content
that site has and returns a integer.
    @params: soup object
"""

def get_soup(url) -> str: # lets you know the return type of the function
    """
        @def: get_soup() pass url and retuns a soup object
        @params: url of the ebay sells site you want to scappe
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

def parse(soup): 
    """
        @def: parse() this function scrappes the sell price, date sold, and title of each element of the site.
        @params: soup object
    """

    resutls = soup.find_all('div', {'class': 's-item__info clearfix'})
    object_list = []
    for items in resutls:

        product = {
            'title' :  items.find('div', {'class': 's-item__title'}).text,
            'date_sold' : items.find('span', {'class': 'POSITIVE'}),
            'sold_price' : items.find('span', {'class': 's-item__price'}).text.replace('USD', '').replace('$', '')
        }
        object_list.append(product)

    for item in object_list.copy():
        if item.get('title') == "Shop on eBay":
            object_list.remove(item)
            break

    for item in object_list:
        dirty_date = str(item.get('date_sold'))
        clean_date = dirty_date.replace("<span class=\"POSITIVE\">Vendido", "")
        date = clean_date.replace("</span>", "")
        item['date_sold'] = date

    return object_list

def number_pages(soup) -> int:
    """
        @def: page_number() usually their is multiple pages of data, this function , look how many pages of content
        that site has and returns a integer.
        @params: soup object
    """
    pageNumber = soup.find('ol', {'class': 'pagination__items'})
    pNumber = pageNumber.find_all('li')
    for i in pNumber:
        number = i.text
    return number


def execution(object_search):
    """ """

    url = f"https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_TitleDesc=0&_nkw={object_search}&rt=nc&LH_Sold=1&LH_Complete=1&_pgn=1"

    # when this function is called it will check number of pages of sell data
    soup = get_soup(url)
    nPages = int(number_pages(soup))

    object_list = []
    if nPages > 1:
        page = 1
        while page <= nPages:
            newUrl = f"https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_TitleDesc=0&_nkw={object_search}&rt=nc&LH_Sold=1&LH_Complete=1&_pgn={page}"
            newSoup = get_soup(newUrl)
            object_list += parse(newSoup)
            page += 1
    else:
        return parse(soup)

    return object_list

result = execution(object_search = "charizard+brilliant+star+alt+art+psa10")

print(result)