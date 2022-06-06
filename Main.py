from ClassInventaireModule import INVENTAIRE
from ClassItemModule import ITEM
from os.path import abspath

f_1 = abspath('./ressources/exemples/from_blk_inv_xml.txt')
f_2 = abspath('./ressources/exemples/from_blk_inv_tab.txt')
f_3 = abspath('./ressources/exemples/from_blk_inv_coma.csv')
f_4 = abspath('./ressources/exemples/set_from_blk.xml')
f_5 = abspath('./ressources/exemples/set_from_blk.txt')
f_6 = abspath('./ressources/exemples/upload_from_python.txt')
f_7 = abspath('./ressources/exemples/impression_from_python.html')
f_8 = abspath('./ressources/exemples/inventaire_from_python.csv')
f_9 = abspath('./ressources/exemples/from_user_inv_semicolon.csv')
f10 = abspath('essai.csv')
f11 = abspath('essai2.csv')


all = [f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9]

# for a in all:
#     inv = INVENTAIRE(a, 'blk', 'inv')

inv1 = INVENTAIRE(f_1, 'blk', 'inv') #ok
# inv2 = INVENTAIRE(f_2, 'blk', 'inv') #ok
# inv3 = INVENTAIRE(f_3, 'blk', 'inv') # ok
# inv4 = INVENTAIRE(f_4, 'blk', 'set') #ok
# inv5 = INVENTAIRE(f_5, 'blk', 'set') #ok
# inv6 = INVENTAIRE(f_6, 'pyth', 'upload') #ok
# inv7 = INVENTAIRE(f_7, 'pyth', 'impression') # a faire
# inv8 = INVENTAIRE(f_8, 'pyth', 'inv') #pose certains problemes conversion int et str
# inv9 = INVENTAIRE(f_9, 'user', 'inv') #ok
inv1.afficher()
inv1.upload()
inv1.printing()


