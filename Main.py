from ClassCatalogueModule import INVENTAIRE
from ClassSetsModule import SETS
from ClassItemModule import ITEM
from os.path import abspath
from json import load
from api import bricklink_api as api




f01 = (abspath('./ressources/stocks/stock_total.csv'))
inv01 = INVENTAIRE(f01, 'pyth', 'inv')
inv01.upload()

#
# f02 = (abspath('./ressources/exemples/from_user_inv_of_sets.csv'))
# sets02 = SETS(f02, 'user', 'sets')
#
#
# sets02.afficher()






















# f11 = abspath('./en_cours/casier_moyen_bleue.csv')
# inv11 = INVENTAIRE(f11, 'user', 'inv')
# inv11.get_price()
# inv11.refresh_infos()
# inv11.sauvegarder(abspath('./ressources/stocks/'), False)
# f11 = abspath('./ressources/stocks/casier_moyen_bleue.csv')
# inv11 = INVENTAIRE(f11, 'pyth', 'inv')
# inv11.sauvegarder(abspath('./ressources/stocks/'), False)
# print(inv11.price_total())
# print(inv11.weight_total())
# print(inv11.qty_total())


























# f1 = abspath('./ressources/stocks/casier_grand_bleueclair.csv')
# f2 = abspath('./ressources/stocks/casier_grand_orangedeux.csv')
# f3 = abspath('./ressources/stocks/casier_moyen_gris.csv')
# f4 = abspath('./ressources/stocks/casier_petit_gris.csv')
# f5 = abspath('./ressources/stocks/casier_petit_noir.csv')
# f6 = abspath('./ressources/stocks/malette_noire.csv')
# f7 = abspath('./ressources/stocks/tritiroir_violetfonce.csv')
# f8 = abspath('./ressources/stocks/casier_moyen_bleue.csv')
#
# inv1 = INVENTAIRE(f1, 'pyth', 'inv')
# inv2 = INVENTAIRE(f2, 'pyth', 'inv')
# inv3 = INVENTAIRE(f3, 'pyth', 'inv')
# inv4 = INVENTAIRE(f4, 'pyth', 'inv')
# inv5 = INVENTAIRE(f5, 'pyth', 'inv')
# inv6 = INVENTAIRE(f6, 'pyth', 'inv')
# inv7 = INVENTAIRE(f7, 'pyth', 'inv')
# inv8 = INVENTAIRE(f8, 'pyth', 'inv')
#
# inv1.fusionner(inv2)
# inv1.fusionner(inv3)
# inv1.fusionner(inv4)
# inv1.fusionner(inv5)
# inv1.fusionner(inv6)
# inv1.fusionner(inv7)
# inv1.fusionner(inv8)
#
# inv1.filename = 'stock_total'
# inv1.sauvegarder(abspath('./ressources/stocks/'), False)
#
# print(inv1.price_total(), '€')
# print(inv1.weight_total(), 'kg')














































# f10 = abspath('essai.csv')
# inv10 = INVENTAIRE(f10, 'pyth', 'inv')
#
# list_items = []
# file = abspath('./ressources/parts.json')
# with open(file) as mon_fichier:
#     data = load(mon_fichier)
# for d in data:
#     if (d['Category Name'] == 'Technic, Axle') or (d['Category Name'] == 'Technic, Brick') or (d['Category Name'] == 'Technic, Connector') or (d['Category Name'] == 'Technic, Gear') or (d['Category Name'] == 'Technic, Liftarm') or (d['Category Name'] == 'Technic, Link') or (d['Category Name'] == 'Technic, Pin') or (d['Category Name'] == 'Technic, Plate'):
#         list_items.append(d['Number'])
#
# for item in list_items:
#     list_color = []
#     json_obj = api.item_mapping.get_element_id('Part', item)
#     for each in json_obj['data']:
#         print(item, each['color_id'])
#         list_color.append(each['color_id'])
#
#     for c in list_color:
#
#         inv10.tab.append(ITEM('', '', '', str(c), '0.00',
#                                 '1', '', '', '', '',
#                                 'P', str(item), '', '', '0',
#                                 '', '', '', '', '',
#                                 '', '', '', '', '',
#                                 '', '', '', '', '',
#                                 '', '', '', '', '',
#                                 '', '', '', '', '',
#                                 '', '', '', '', '',
#                                 ''))
#
# inv10.sauvegarder(abspath('./'), False)
# inv10 = INVENTAIRE(f10, 'pyth', 'inv')
# inv10.sauvegarder(abspath('./'), False)
#
# inv10 = INVENTAIRE(f10, 'pyth', 'inv')
# inv10.get_picture()