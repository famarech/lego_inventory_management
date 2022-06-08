from ClassItemModule import ITEM
from ReadModule import loading
from ReadModule import get_extension
import WriteModule as write
from os.path import abspath
from time import time
from time import localtime




class INVENTAIRE:

    def __init__(self, path, where_from, type):

        self.path = get_extension(path)[0]
        self.filename = get_extension(path)[1]
        self.extension = get_extension(path)[2]
        self.where_from = where_from
        self.type = type
        self.tab = loading(path, where_from, type, self.filename, self.extension)

        self.price = self.price_total()
        self.weight = self.weight_total()
        self.qty = self.qty_total()
        self.price_par_piece = self.price / self.qty




    def afficher(self):
        print(f"Inventaire : {self.filename} ===\n")
        for item in self.tab:
            item.afficher()
        print("\n\n\n")

    def price_total(self):
        somme = 0
        for item in self.tab:
            somme = somme + item.price_total()
        return somme

    def weight_total(self):
        somme = 0
        for item in self.tab:
            somme = somme + item.weight_total()
        somme = somme / 1000
        return somme

    def qty_total(self):
        somme = 0
        for item in self.tab:
            somme = somme + int(item.qty)
        return somme




    def sauvegarder(self, path_destination):
        path = path_destination + '\\' + self.filename + '.csv'
        write.save(self.tab, path, "w")
        print("Inventaire sauvegardé !!!")

    def upload(self):
        write.transform_to_upload_blk_xml(self.tab, self.filename)

    def printing(self):
        write.transform_to_impression_html(self.tab, self.filename)
        print("Inventaire printé en html !!!")

    def fusionner(self, inventory_to_add):
        # !!!! ATTENTION !!!! met à jour l'objet actuel d'origine avec un nouvel inventaire
        # inventory_to_add est l'inventaire à ajouter à l'objet actuel
        for item in inventory_to_add.tab:
            self.tab.append(item)
        filename = '/' + self.filename + '_' +\
                    inventory_to_add.filename + '_' +\
                    str(localtime().tm_hour) +\
                    str(localtime().tm_min) +\
                    str(localtime().tm_sec) + '_temp.csv'
        path = abspath('./ressources/save_temp')
        write.save(self.tab, path + filename, "w")
        print(f"l'inventaire '''{inventory_to_add.filename}''' " +\
                f"fusionné dans l'Inventaire '''{self.filename}'''\n\n")

    def get_price(self):
        size = len(self.tab)
        time_per_item = 1
        finish = localtime(time() + (time_per_item * size))
        print("fin de la recherche de prix estimé à :\n" +\
                f"{finish.tm_hour}:{finish.tm_min}:{finish.tm_sec} -- heure local")
        for item in self.tab:
            item.get_price()
        filename = '/' + self.filename + '_' +\
                    str(localtime().tm_hour) +\
                    str(localtime().tm_min) +\
                    str(localtime().tm_sec) + '_temp.csv'
        path = abspath('./ressources/save_temp')
        write.save(self.tab, path + filename, "w")
        print(f"\t\tFin de la Recherche de Prix de l'inventaire {self.filename}\n\n")

    def find_in(self, inventory_in_wich):
        # !!!! ATTENTION !!!! fait une recherche des items de l'inventaire self.tab
        # dans inventory_in_wich qui est passé en parametre
        print(f"Recherche des items de l'inventaire ''''{self.filename}''''\n"+
                f"\tdans l'inventaire ''''{inventory_in_wich.filename}'''' ...\n\n")

        inventory_in_wich.tab.sort(key=lambda obj: obj.colorid)
        inventory_in_wich.tab.sort(key=lambda obj: obj.itemid)
        for each in self.tab:
            print(INVENTAIRE.trouve(inventory_in_wich.tab, each))



    def trouve(inv, thing):
        a = 0
        z = len(inv)
        mid = int(round(z/2, 0))
        trouve = False
        index = 1
        if (thing.itemid + thing.colorid) == (inv[a].itemid + inv[a].colorid):
            trouve = True
            content = (f"{thing.itemidname} : {thing.colorname} : {thing.qty}" +\
                        f" : {inv[a].box} : {inv[a].column}{inv[a].row}\n")
        while trouve == False:
            if mid == a or mid == z:
                content = (f"{thing.itemidname} : {thing.colorname} : {thing.qty}" +\
                            "\t\t\tn'existe pas a commander\n")
                return content
            if (thing.itemid + thing.colorid) == (inv[mid].itemid + inv[mid].colorid):
                trouve = True
                content = (f"{thing.itemidname} : {thing.colorname} : {thing.qty}" +\
                            f" : {inv[mid].box} : {inv[mid].column}{inv[mid].row}\n")
            else:
                if (thing.itemid + thing.colorid) > (inv[mid].itemid + inv[mid].colorid):
                    a = mid
                    mid += int(round((z-mid)/2, 0))
                else:
                    z = mid
                    mid -= int(round((mid-a)/2, 0))
        return content





    # def compare(self):
        #comparer deux inventaire pour trouver l'un dans l'autre