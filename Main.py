import BrickLinkModule as blk
from ClassInventaireModule import INVENTAIRE
from ClassItemModule import ITEM
from os import listdir
from os.path import abspath


general_path = abspath('./').replace('\\', '/')
inventaire = INVENTAIRE(general_path + '/essai.csv')
blk.get_all(inventaire)
inventaire.afficher()

# path_stocks = abspath('./02 - Stocks').replace('\\', '/')
# all_stocks = listdir(path_stocks)
# # inventaire = INVENTAIRE(path_stocks + '/' + all_stocks[0])
# i = 0
# for i in range(13):
#     inventaire = INVENTAIRE(path_stocks + '/' + all_stocks[i])
#     inventaire.transform_to_impression_html(i)
#     i += 1
