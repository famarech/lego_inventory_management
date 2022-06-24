from ClassInventaireModule import INVENTAIRE
from ClassItemModule import ITEM
from os.path import abspath
from json import load
from api import bricklink_api as api

# f_1 = abspath('./ressources/exemples/from_blk_inv_xml.txt')
# f_2 = abspath('./ressources/exemples/from_blk_inv_tab.txt')
# f_3 = abspath('./ressources/exemples/from_blk_inv_coma.csv')
# f_4 = abspath('./ressources/exemples/from_blk_set.xml')
# f_5 = abspath('./ressources/exemples/from_blk_set_tab.txt')
# f_6 = abspath('./ressources/exemples/from_pyth_upload_xml.txt')
# f_7 = abspath('./ressources/exemples/impression_from_python.html')
# f_8 = abspath('./ressources/exemples/from_pyth_inv_semicolon.csv')
# f_9 = abspath('./ressources/exemples/from_user_inv_semicolon.csv')
# f10 = abspath('essai.csv')
# f11 = abspath('./ressources/stocks/casier_moyen_gris.csv')

# inv1 = INVENTAIRE(f_1, 'blk', 'inv') #ok
# inv2 = INVENTAIRE(f_2, 'blk', 'inv') #ok
# inv3 = INVENTAIRE(f_3, 'blk', 'inv') # ok
# inv4 = INVENTAIRE(f_4, 'blk', 'set') #ok
# inv5 = INVENTAIRE(f_5, 'blk', 'set') #ok
# inv6 = INVENTAIRE(f_6, 'pyth', 'upload') #ok
# inv7 = INVENTAIRE(f_7, 'pyth', 'impression') # a faire
# inv8 = INVENTAIRE(f_8, 'pyth', 'inv') #ok
# inv9 = INVENTAIRE(f_9, 'user', 'inv') #ok

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
# inv10.sauvegarder(abspath('./ressources/stocks/'), False)
#
# inv10 = INVENTAIRE(f10, 'pyth', 'inv')
# inv10.get_picture()

# inv11 = INVENTAIRE(f11, 'user', 'inv')
# inv11.get_price()
# inv11.refresh_infos()
# inv11.sauvegarder(abspath('./ressources/stocks/'), False)
# f11 = abspath('./ressources/stocks/casier_grand_orangedeux.csv')
# inv11 = INVENTAIRE(f11, 'pyth', 'inv')
# inv11.sauvegarder(abspath('./ressources/stocks/'), False)
# print(inv11.price_total())
# print(inv11.weight_total())
# print(inv11.qty_total())

f1 = abspath('./ressources/stocks/casier_grand_bleueclair.csv')
f2 = abspath('./ressources/stocks/casier_grand_orangedeux.csv')
f3 = abspath('./ressources/stocks/casier_moyen_gris.csv')
f4 = abspath('./ressources/stocks/casier_petit_gris.csv')
f5 = abspath('./ressources/stocks/casier_petit_noir.csv')
f6 = abspath('./ressources/stocks/malette_noire.csv')
f7 = abspath('./ressources/stocks/tritiroir_violetfonce.csv')

inv1 = INVENTAIRE(f1, 'pyth', 'inv')
inv2 = INVENTAIRE(f2, 'pyth', 'inv')
inv3 = INVENTAIRE(f3, 'pyth', 'inv')
inv4 = INVENTAIRE(f4, 'pyth', 'inv')
inv5 = INVENTAIRE(f5, 'pyth', 'inv')
inv6 = INVENTAIRE(f6, 'pyth', 'inv')
inv7 = INVENTAIRE(f7, 'pyth', 'inv')

inv1.fusionner(inv2)
inv1.fusionner(inv3)
inv1.fusionner(inv4)
inv1.fusionner(inv5)
inv1.fusionner(inv6)
inv1.fusionner(inv7)

inv1.filename = 'stock_total'
inv1.sauvegarder(abspath('./ressources/stocks/'), True)

print(inv1.price_total())













































