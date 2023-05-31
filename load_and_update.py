import json
from datetime import datetime
# this file is to load and updtae eaither for new items to be added to the json
# or dates, integers to be updated to the correct format

def load_info():
    full_data = []
    obj_count = 0
    with open('ch_v_rainbow_psa10.json') as f:
        temp = json.load(f)
        for dict in temp:
            obj_count += 1
            full_data.append(dict)
    print(f"number of elements in the list {obj_count}")
    
    return full_data


file = load_info()

#files to update


