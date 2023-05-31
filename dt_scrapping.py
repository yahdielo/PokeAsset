import numpy as np
import pandas as pd
import datetime
import json
import requests
from bs4 import BeautifulSoup


# WEBSCRAPPING FUNCTIONS
def  get_data(url):
    """
    this module takes url as parameter, and creats a soup object
    and returns it
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

def parse(soup):
    """
    this module calls find_all method in the suop object, and pass the div specific div class
    to look in and scrappes the data, then we run inside the dict and clean elemenetns that we do not
    want in the list, then we clean all the dates 
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
    #loop to clean ebay item
    for item in object_list.copy():
        if item.get('title') == "Shop on eBay":
            object_list.remove(item)
            break
    #loop to clean the date_sold to for m/d/y
    for item in object_list:
        item["sold_price"] = float(item["sold_price"])
        months_dict = {
            'Jan': 1,'Feb': 2,'Mar': 3,'Apr': 4,'May': 5,
            'Jun': 6,'Jul': 7,'Aug': 8,'Sep': 9,'Oct': 10,'Nov': 11,
            'Dec': 12
        }
        dirty_date = str(item.get('date_sold'))
        clean_date = dirty_date.replace("<span class=\"POSITIVE\">Sold  ", "")
        cleaner_date = clean_date.replace(",", "")
        date = cleaner_date.replace("</span>", "")
        monthToInt = date.split()

        if monthToInt[0] in months_dict:
            complete_date = f"{monthToInt[2]}-{months_dict[monthToInt[0]]}-{monthToInt[1]}"
        item['date_sold'] = complete_date

    return object_list

# JSON FUNCTIONS
def dump_info_alt_art(ch_card_dt):
    with open('ch_vmax_alt_art_psa10.json', 'w') as f:
        json.dump(ch_card_dt, f)


def sold_price(object_list):
    '''Function that return a list with all the price_sold as float'''
    prices = []
    for items in object_list:
        prices.append(float(items['sold_price']))
    return prices

"""def date_sold(object_list):
    '''Function that return a list with all the date_sold as datetime'''
    dates = []
    for items in object_list:
        #Convert str to datetime and append it to list
        dates.append(str_to_date(items['date_sold']))
    return dates"""


# SEARCHING VALUES
ch_rainbow_psa10 = "charizard+vmax+rainbow+psa+10"
ch_v_alt_art = "charizard+brilliant+star+alt+art+psa10"
pk_total_PsaSells = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=pokemon+psa&_sacat=0&LH_TitleDesc=0&_fsrp=1&rt=nc&_odkw=pokemon&_osacat=0&_ipg=240&LH_Sold=1"
bgs_ebay_totalSells = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=pokemon+bgs&_sacat=0&LH_TitleDesc=0&_fsrp=1&_osacat=0&_odkw=pokemon+bgs&_ipg=240&LH_Sold=1"
page = 0
full_parse = []
while page < 4:
    page += 1
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_TitleDesc=0&_nkw={ch_v_alt_art}&rt=nc&LH_Sold=1&LH_Complete=1&_pgn={page}"
    soup = get_data(url)
    full_parse += parse(soup)
dump_info_alt_art(full_parse)

print(full_parse[2])
"""# START OF THE PROGRAM
dump_info_alt_art(full_parse)
loadaded_data = load_info_alt_art()

# DATASET TO USE
prices = np.array(sold_price(loadaded_data))
dates = np.array(date_sold(loadaded_data))
data_set = np.column_stack((dates, prices))
sorted_data = data_set[data_set[:,0].argsort()]
x_data = sorted_data[:, 0]
y_data = sorted_data[:, 1]

def export_to_json(data_set, filename):
    converted_data = data_set.tolist()

    with open(filename, 'w') as json_file:
        json.dump(converted_data, json_file)

# GRAPH CONFIG
print(dates)
print(sorted_data)
filename = 'data_set.json'
export_to_json(sorted_data, filename)

# CONNECTION TO FRONT-END
"""