from ClassCatalogueModule import INVENTAIRE
from ClassItemModule import ITEM
from os.path import abspath
from json import load
from api import bricklink_api as api


# json_obj = api.catalog_item.get_subsets('Set', '6608-1')
# code = json_obj['meta']['code']
# if code == 401:
#     print("Impossible de prendre les prix !!!\n" +\
#             " --- !!! --- Erreur d'Authentification --- !!! --- \n\n\n")
# elif code == 200:
#     print(json_obj)
#     # for each in json_obj['data']:
#     #     for e in each['entries']:
#     #         # print(e['item']['no'], e['quantity'])
#     #         print(e)


json_obj = api.catalog_item.get_item('Part', '4276')
code = json_obj['meta']['code']
if code == 401:
    print("Impossible de prendre les prix !!!\n" +\
            " --- !!! --- Erreur d'Authentification --- !!! --- \n\n\n")
elif code == 200:
    print(json_obj['data'])