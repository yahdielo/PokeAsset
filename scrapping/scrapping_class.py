from datetime import datetime
import json
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

@def: number_pages() usually their is multiple pages of data, this function , look how many pages of content
that site has and returns a integer.
    @params: soup object

@def: execution() function execute the whole process of getting the soup element, parsing the data
                    and dumping the sell data into a json file
    @params: object seach meaning the name and edition of the card
    @example: charizard+vmax+rainbow+psa+10
"""

class Ebay_Scrapper():

    def __init__(self, pokemon) -> None:
        self.pokemon = pokemon

    def __get_metadata(self, file_name, url, quantity) -> dict:
        now = datetime.now()
        date = now.strftime("%Y-%m-%d") 
        hour = now.strftime("%H:%M:%S")
        metadata = {"date": date, "hour": hour, "file_name": file_name, "url": url, "quantity": quantity}
        return metadata


    def __url_builder(self, poke_name, card_type, foil_type, psa_num) -> list:
        '''Function that return a url for the ebay request
            poke_name = "charizard"
            card_type = "vmax"
            foil_type = "rainbow"
        '''
        poke_search = poke_name + "+"
        card_type_search = card_type + "+"
        foil_search = foil_type + "+"
        psa_search = "psa+" + str(psa_num)
        object_search = poke_search + card_type_search + foil_search + psa_search
        url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={object_search}&_sacat=0&LH_TitleDesc=0&Grade=10&_oaa=1&_dcat=183454&LH_BO=1&rt=nc&LH_Sold=1&LH_Complete=1"
        object_search = object_search.replace("+", "_")
        return [object_search, url]


    def __get_soup(self, url) -> str: # lets you know the return type of the function
        """
            @def: get_soup() pass url and retuns a soup object
            @params: url of the ebay sells site you want to scrappe
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup


    def __parse(self, soup): 
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
            if item.get('title') == "Shop on eBay": # if this element exist remove it
                object_list.remove(item)
                break

        for item in object_list:
            dirty_date = str(item.get('date_sold'))
            clean_date = dirty_date.replace("<span class=\"POSITIVE\">Vendido", "")
            date = clean_date.replace("</span>", "")
            item['date_sold'] = date

        return object_list

    def __number_pages(self, soup) -> int:
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

    def __dump_info(self, card_sell_data, fileName):
        """thid module dumps the collected data in to a jsonfile
            using dump
            @params: card_sell_dara is the list containing the sells objects
            @params: FileName is the name you want the file to have
        """
        with open(f'{fileName}.json', 'w') as f:
            json.dump(card_sell_data, f)

    def execution(self, card_type, foil_type, psa_num) -> json:
        """ This modules performs a full scrapping of the desire data
            @params: object_search = "charizard+brilliant+star+alt+art+psa10"

            function check for the number of pages containing data, of the sells,
            if ebay has more than 1 page of sells data for that specific item, the function will loop
            the amount of pages collecting all the data and returning it as json
        """

        file_name, url = self.__url_builder(self.pokemon, card_type, foil_type, psa_num)
        soup = self.__get_soup(url)
        object_list = []

        try:
            number_pages = int(self.__number_pages(soup))
            if number_pages > 1:
                url = f"{url}&_pgn="
                for page in range(1, number_pages + 1):
                    new_url = f"{url}{page}"
                    print(new_url)
                    new_soup = self.__get_soup(new_url)
                    object_list.extend(self.__parse(new_soup))
        except:
            print("only one page of data is avaliable")
            object_list.extend(self.__parse(soup))

        metadata = [self.__get_metadata(file_name, url, len(object_list))]
        object_list.extend(metadata)
        self.__dump_info(object_list, file_name)
        return f"Data was scrapped and file creates for {file_name}"

#the first run is to collect data from all 150 pokemonsbase set first edition cards
obj = Ebay_Scrapper("charizard")
result = obj.execution("vmax", "rainbow", 10)

#print(result)
