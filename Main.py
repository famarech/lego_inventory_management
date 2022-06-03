import BrickLinkModule as blk
from ClassInventaireModule import INVENTAIRE
from ClassItemModule import ITEM
from os import listdir
from os.path import abspath
import ApiModule as api
import time

# general_path = abspath('./').replace('\\', '/')
# inventaire = INVENTAIRE(general_path + '/essai.csv')
# blk.get_all(inventaire)
# inventaire.afficher()

# path_stocks = abspath('./02 - Stocks').replace('\\', '/')
# all_stocks = listdir(path_stocks)
# # inventaire = INVENTAIRE(path_stocks + '/' + all_stocks[0])
# i = 0
# for i in range(13):
#     inventaire = INVENTAIRE(path_stocks + '/' + all_stocks[i])
#     inventaire.transform_to_impression_html(i)
#     i += 1



# json_obj = api.catalog_item.get_price_guide("Part", "3005", color_id="11", new_or_used="U")
# print(json_obj['data']['avg_price'])


general_path = abspath('./').replace('\\', '/')
inventaire = INVENTAIRE(general_path + '/essai.csv')
start = time.time()
api.get_price(inventaire)
finish = time.time()
delta = finish - start
ratio = round(delta / len(inventaire.tab), 0)
inventaire.afficher()
print(f'{ratio} secondes par reference\n')