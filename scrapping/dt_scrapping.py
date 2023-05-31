import numpy as np
import datetime
import json
import requests
from bs4 import BeautifulSoup
from dataDump import dump_info_alt_art


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

# JSON FUNCTIONS
def dump_info_alt_art(ch_card_dt):
    with open('ch_vmax_alt_art_psa10.json', 'w') as f:
        json.dump(ch_card_dt, f)

def load_info_alt_art():
    full_data = []
    with open('ch_vmax_alt_art_psa10.json') as f:
        temp = json.load(f)
        for dict in temp:
            full_data.append(dict)
    return full_data

# EXTRACTING DATA TO USE
def str_to_date(str):
    '''Function convert str to datetime.
    The month in the string should be in spanish to work'''
    months_dict = {'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6,
                   'jul': 7, 'ago': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dic': 12 }
    all_values = str.split(" ")
    date = int(all_values[2])
    if all_values[3] in months_dict.keys():
        month = months_dict[all_values[3]]
    year = int(all_values[4])
    full_date = datetime.datetime(year, month, date)
    return(full_date.strftime('%Y-%m-%d'))

def sold_price(object_list):
    '''Function that return a list with all the price_sold as float'''
    prices = []
    for items in object_list:
        prices.append(float(items['sold_price']))
    return prices

def date_sold(object_list):
    '''Function that return a list with all the date_sold as datetime'''
    dates = []
    for items in object_list:
        #Convert str to datetime and append it to list
        dates.append(str_to_date(items['date_sold']))
    return dates


# SEARCHING VALUES
ch_rainbow_psa10 = "charizard+vmax+rainbow+psa+10"
ch_v_alt_art = "charizard+brilliant+star+alt+art+psa10"
page = 0
full_parse = []
while page < 4:
    print(page)
    page += 1
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_TitleDesc=0&_nkw={ch_v_alt_art}&rt=nc&LH_Sold=1&LH_Complete=1&_pgn={page}"
    soup = get_data(url)
    full_parse += parse(soup)

"""
# START OF THE PROGRAM
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
print(sorted_data)
filename = 'data_set.json'
export_to_json(sorted_data, filename)"""