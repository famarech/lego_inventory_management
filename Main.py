from ClassInventaireModule import INVENTAIRE
from ClassItemModule import ITEM
from os.path import abspath

f_1 = abspath('./ressources/exemples/from_blk_inv_xml.txt')
f_2 = abspath('./ressources/exemples/from_blk_inv_tab.txt')
f_3 = abspath('./ressources/exemples/from_blk_inv_coma.csv')
f_4 = abspath('./ressources/exemples/from_blk_set.xml')
f_5 = abspath('./ressources/exemples/from_blk_set_tab.txt')
f_6 = abspath('./ressources/exemples/from_pyth_upload_xml.txt')
f_7 = abspath('./ressources/exemples/impression_from_python.html')
f_8 = abspath('./ressources/exemples/from_pyth_inv_semicolon.csv')
f_9 = abspath('./ressources/exemples/from_user_inv_semicolon.csv')
f10 = abspath('essai.csv')
f11 = abspath('essai2.csv')

# inv = INVENTAIRE(f_1, 'blk', 'inv') #ok
# inv = INVENTAIRE(f_2, 'blk', 'inv') #ok
# inv = INVENTAIRE(f_3, 'blk', 'inv') # ok
# inv4 = INVENTAIRE(f_4, 'blk', 'set') #ok
# inv = INVENTAIRE(f_5, 'blk', 'set') #ok
# inv = INVENTAIRE(f_6, 'pyth', 'upload') #ok
# inv = INVENTAIRE(f_7, 'pyth', 'impression') # a faire
inv8 = INVENTAIRE(f_8, 'pyth', 'inv') #ok
# inv = INVENTAIRE(f_9, 'user', 'inv') #ok

inv8.refresh_infos()