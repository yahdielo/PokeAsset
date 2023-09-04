#!/usr/bin/env python3
'''This document contains web scrapping process for TCG Sets'''


import requests
import json
from bs4 import BeautifulSoup


def get_sets():
    '''Function that web scrap and generate json file'''
    tcg_sets = {}
    uri = 'https://www.pocketmonsters.net/tcg'
    response = requests.get(uri)
    soup = BeautifulSoup(response.text, "html.parser")
    lst = soup.find_all('a')

    for i in range(37, 236):
        set_name = lst[i].get_text()
        set_img = lst[i].get('href')
        tcg_sets[set_name] = set_img
        # añadirle a cada set mas info e img del set

    with open('tcg_sets.json', 'w') as f:
        json.dump(tcg_sets, f)

# Use function:
# get_sets()