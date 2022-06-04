import BrickLinkModule as blk
from ClassInventaireModule import INVENTAIRE
from ClassItemModule import ITEM
from os import listdir
from os.path import abspath


# path_stocks = abspath('./02 - Stocks')
# all_stocks = listdir(path_stocks)
# inventaire = INVENTAIRE(path_stocks + '/' + all_stocks[0])
# i = 1
# for i in range(13):
#     inventaire_temp = INVENTAIRE(path_stocks + '/' + all_stocks[i])
#     inventaire.fusionner(inventaire_temp)
#     i += 1
#
# print(len(inventaire.tab))



inventaire = INVENTAIRE(abspath('essai.csv'))
print(inventaire.prix_total())
