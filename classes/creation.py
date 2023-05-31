#this is the base class where creation happens
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime


class Creation:
    """
    This class will handlee de creation of new lists as a json,
    cleans data updating price_sold in to integer.
    """

    def create(url):
        """
        this module calls find_all method in the suop object, and pass the div specific div class
        to look in and scrappes the data, then we run inside the dict and clean elemenetns that we do not
        want in the list, then we clean all the dates 
        """

        #request the hml element to create a soup object
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

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

if __name__ == "__main__":
    print(Creation.create("https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_TitleDesc=0&_nkw=charizard+vmax+rainbow+psa+10&rt=nc&LH_Sold=1&LH_Complete=1&_pgn=1"))
