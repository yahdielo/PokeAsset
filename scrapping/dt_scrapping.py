from ast import dump
import datetime
import json
from unittest import result
import requests
from bs4 import BeautifulSoup
from pokemonNames import pokemonNames

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
        @params: url of the ebay sells site you want to scrappe
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
    count = 0
    for items in resutls:

        product = {
            'title' :  items.find('div', {'class': 's-item__title'}).text,
            'date_sold' : items.find('span', {'class': 'POSITIVE'}),
            'sold_price' : items.find('span', {'class': 's-item__price'}).text.replace('USD', '').replace('$', '')
        }
        object_list.append(product)
        count += 1

    for item in object_list:
        if item.get('title') == "Shop on eBay":
            object_list.remove(item)
            break

    for item in object_list:
        dirty_date = str(item.get('date_sold'))
        clean_date = dirty_date.replace("<span class=\"POSITIVE\">Vendido", "")
        date = clean_date.replace("</span>", "")
        item['date_sold'] = date

    print(count)
    return object_list

def number_pages(soup) -> int:
    """
        @def: page_number() usually their is multiple pages of data, this function , look how many pages of content
        that site has and returns a integer.
        @params: soup object
    """
    pageNumber = soup.find('ol', {'class': 'pagination__items'})
    print(pageNumber)
    pNumber = pageNumber.find_all('li')
    for i in pNumber:

        number = i.text
        print(f"this is i.text: {number}")


    return number

def dump_info(card_sell_data, fileName):
    """thid module dumps the collected data in to a jsonfile
        using dump
        @params: card_sell_dara is the list containing the sells objects
        @params: FileName is the name you want the file to have
    """
    with open(f'{fileName}.json', 'w') as f:
        json.dump(card_sell_data, f)

def execution(object_search) -> json:
    """ This modules performs a full scrapping of the desire data
        @params: object_search = "charizard+brilliant+star+alt+art+psa10"

        function check for the number of pages containing data, of the sells,
        if ebay has more than 1 page of sells data for that specific item, the function will loop
        the amount of pages collecting all the data and returning it as json
    """

    url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={object_search}&_sacat=0&LH_TitleDesc=0&Grade=10&_oaa=1&_dcat=183454&LH_BO=1&rt=nc&LH_Sold=1&LH_Complete=1&_pgn=1"
    

    # when this function is called it will check number of pages of sell data
    soup = get_soup(url)
    try:
        nPages = int(number_pages(soup))
    except:
        print("only one page of data is avaliable")
        object_list = parse(soup)
        fileName = object_search.replace("+", " ")
        dump_info(object_list, fileName)
        return object_list


    object_list = []
    if nPages > 1:
        page = 1
        print(nPages)
        for page in range(1, nPages + 1):
            #this current url is for the 1st edition
            newUrl = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={object_search}&_sacat=0&LH_TitleDesc=0&Grade=10&_oaa=1&_dcat=183454&LH_BO=1&rt=nc&LH_Sold=1&LH_Complete=1&_pgn={page}"
            #newnew="https://www.ebay.com/sch/i.html?_from=R40&_nkw=1999+charmeleon+shadowless+1st+edition+psa10&_sacat=0&LH_TitleDesc=0&LH_Sold=1&_fsrp=1"
            newSoup = get_soup(newUrl)
            object_list.append(parse(newSoup))
            #page += 1

        fileName = object_search.replace("+", " ")
        dump_info(object_list, fileName)
    return f"Data was scrapped and file creates for {fileName}"

# the first run is to collect data from all 150 pokemonsbase set first edition cards
result = execution(object_search = "charizard+vmax+rainbow+psa+10")

print(result)
