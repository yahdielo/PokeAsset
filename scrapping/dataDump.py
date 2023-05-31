import json

def dump_info_alt_art(ch_card_dt):
    """thid module dumps the collected data in to a jsonfile
        using dump
    """
    with open('ch_vmax_alt_art_psa10.json', 'w') as f:
        json.dump(ch_card_dt, f)