from api import bricklink_api as api
from os.path import abspath

def get_price(inventaire):
    for item in inventaire.tab:
        itemid = item.itemid
        color = item.color
        try:
            json_obj = api.catalog_item.get_price_guide("Part", itemid, color, new_or_used="U")
            item.price = json_obj['data']['avg_price'].replace('.', ',')
            print(item.price)
        except:
            item.price = '0'
        path = abspath('./06 - Sauvegarde_temp/prices_temp.csv')
        inventaire.sauvegarder(path)