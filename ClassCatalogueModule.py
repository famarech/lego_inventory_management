from ClassItemModule import ITEM
import ReadModule
from ReadModule import get_extension
import WriteModule as write
from BrickLinkModule import get_picture
from os.path import abspath
from time import time
from time import localtime
from api import bricklink_api as api




class CATALOGUE:

    def __init__(self, path, where_from, type):

        self.path = get_extension(path)[0]
        self.filename = get_extension(path)[1]
        self.extension = get_extension(path)[2]
        self.where_from = where_from
        self.type = type






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

    def sauvegarder(self, path_destination, refresh):
        path = path_destination + '\\' + self.filename + '.csv'
        self.tab.sort(key=lambda obj: obj.colorid)
        self.tab.sort(key=lambda obj: obj.itemid)
        self.tab.sort(key=lambda obj: obj.column)
        self.tab.sort(key=lambda obj: obj.row)
        self.tab.sort(key=lambda obj: obj.box)
        if refresh is True:
            self.refresh_infos()
        write.save(self.tab, path, "w")
        print("Inventaire trié et sauvegardé !!!\n\n")

    def upload(self):
        for item in self.tab:
            print(item.price)
            print(type(item.price))
            print(item.qty)
            print(type(item.qty))

        index = len(self.tab) - 1
        for item in reversed(self.tab):
            if item.qty == '0' or float(item.price.replace(',','.')) == 0:
                del self.tab[index]
            index -= 1
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
        content = ''
        index = 1
        for each in self.tab:
            infos = INVENTAIRE.trouve(inventory_in_wich.tab, each)
            index += 1
            if (index % 2) == 0:
                pair = "pair"
            else:
                pair = "impair"
            content += '\t\t<div class="' + pair + '">\n' +\
                        '\t\t\t<img src="' + '' + '">\n' +\
                        '\t\t\t<p>' + str(infos[0]) + '</p>\n' +\
                        '\t\t\t<p class="itemidname">' + '' + '</p>\n' +\
                        '\t\t\t<p>' + str(infos[1]) + '</p>\n' +\
                        '\t\t\t<p>' + '' + '</p>\n' +\
                        '\t\t\t<p>' + str(infos[2]) + '</p>\n' +\
                        '\t\t\t<p>' + str(infos[3]) + '</p>\n' +\
                        '\t\t\t<p>' + str(infos[4]) + '</p>\n' +\
                        '\t\t\t<p>' + str(infos[5]) + '</p>\n' +\
                        '\t\t\t<p>' + str(infos[6]) + '</p>\n' +\
                        '\t\t\t<p>' + str(infos[7]) + '</p>\n' +\
                        '\t\t</div>\n'
        write.recherche_impression_html(content, self.filename, inventory_in_wich.filename)
        print("Resultat converti en html.\n\n")

    def trouve(inv, thing):
        a = 0
        z = len(inv)
        mid = int(round(z/2, 0))
        trouve = False
        index = 1
        if (thing.itemid + thing.colorid) == (inv[a].itemid + inv[a].colorid):
            trouve = True
            print(f"{thing.itemidname} : {thing.colorname} : {thing.qty}" +\
                        f" : {inv[a].box} : {inv[a].row}{inv[a].column}")
            if int(inv[a].qty) > int(thing.qty):
                q_command = 0
            else:
                q_command = int(thing.qty) - int(inv[a].qty)
            content = [thing.itemidname, thing.colorname,
                        thing.qty, inv[a].qty, q_command,
                        inv[a].box, inv[a].row, inv[a].column]
        while trouve == False:
            if mid == a or mid == z:
                print(f"{thing.itemidname} : {thing.colorname} : {thing.qty}" +\
                            "\tn'existe pas a commander")
                content = [thing.itemidname, thing.colorname,
                            thing.qty, 0, thing.qty,
                            '', '', '']
                return content
            if (thing.itemid + thing.colorid) == (inv[mid].itemid + inv[mid].colorid):
                trouve = True
                print(f"{thing.itemidname} : {thing.colorname} : {thing.qty}" +\
                            f" : {inv[mid].box} : {inv[mid].row}{inv[mid].column}")
                if int(inv[mid].qty) > int(thing.qty):
                    q_command = 0
                else:
                    q_command = int(thing.qty) - int(inv[mid].qty)
                content = [thing.itemidname, thing.colorname,
                            thing.qty, inv[mid].qty, q_command,
                            inv[mid].box, inv[mid].row, inv[mid].column]
            else:
                if (thing.itemid + thing.colorid) > (inv[mid].itemid + inv[mid].colorid):
                    a = mid
                    mid += int(round((z-mid)/2, 0))
                else:
                    z = mid
                    mid -= int(round((mid-a)/2, 0))
        return content

    def get_picture(self):
        start = time()
        size = len(self.tab)
        time_per_item = 9.5
        finish = localtime(start + (time_per_item * size))
        print("fin du telechargement des images estimé à :\n" +\
                f"{finish.tm_hour}:{finish.tm_min}:{finish.tm_sec} -- heure local\n\n")
        get_picture(self)

    # def compare(self):
        #comparer deux inventaire pour trouver l'un dans l'autre








class INVENTAIRE(CATALOGUE):

    def __init__(self, path, where_from, type):

        super().__init__(path, where_from, type)

        self.tab = ReadModule.loading(path, where_from, type, self.filename, self.extension)

        self.price = self.price_total()
        self.weight = self.weight_total()
        self.qty = self.qty_total()
        self.price_par_piece = self.price / self.qty



    def afficher(self):
        print(f"Inventaire : {self.filename} ===\n")
        for item in self.tab:
            item.afficher()
        print(f"\t--> {len(self.tab)} références.\n\n\n")

    def refresh_infos(self):
        print(f"Rafraichissement des infos de '''{self.filename}''' en cours ...")
        start = time()
        size = len(self.tab)
        # time_per_item = 3.7 # en utilisant les fichiers json
        time_per_item = 1.3004 # en utilisant l'api
        finish = localtime(start + (time_per_item * size))
        print("fin du rafraichissement estimé à :\n" +\
                f"{finish.tm_hour}:{finish.tm_min}:{finish.tm_sec} -- heure local")
        for item in self.tab:
            item.refresh_infos_by_api()
        filename = '/' + self.filename + '_' +\
                    str(localtime().tm_hour) +\
                    str(localtime().tm_min) +\
                    str(localtime().tm_sec) + '_temp.csv'
        path = abspath('./ressources/save_temp')
        write.save(self.tab, path + filename, "w")
        delta = round(time() - start, 2)
        print("\tRafraichissement terminé !!!\n" +\
                f"{len(self.tab)} references en {delta} secondes.\n")








class SET(CATALOGUE):

    def __init__(self, path, where_from, type, qty, box, row, column):

        super().__init__(path, where_from, type)
        self.status = '' # soit complet, modifié ou en cours de construction

        self.itemid = self.filename
        self.name = ''
        self.type = 'SET'
        self.categoryid = ''
        self.urlimage = ''
        self.weight = ''
        self.dimx = ''
        self.dimy = ''
        self.dimz = ''
        self.yearreleased = ''
        self.isobsolete = ''
        self.qty = qty
        self.box = box
        self.row = row
        self.column = column

        self.tab = self.loading()




    def afficher(self):
        print(f"Set N° : {self.filename} ===\n")
        for item in self.tab:
            item.afficher()
        print(f"\t--> {len(self.tab)} références.\n\n\n")

    def loading(self):
        print(f"chargement du set '''{self.filename}{self.extension}''' en cours")
        start = time()
        tab = []
        json_obj = api.catalog_item.get_subsets('Set', self.itemid)
        for each in json_obj['data']:
            for e in each['entries']:
                a = str(e['item']['category_id'])
                c = str(e['color_id'])
                q = str(e['quantity'] * int(self.qty))
                t = e['item']['type']
                b = self.box + ' ' + self.itemid
                n = e['item']['name'].replace(';', '')
                tab.append(ITEM('', '', a, c, '0,00',
                                q, '', '', '', '',
                                t, e['item']['no'], '', '', '0',
                                '', '', n, '', '',
                                '', '', '', '', '',
                                '', '', '', '', '',
                                '', '', '', '', '',
                                '', '', '', '', '',
                                '', '', '', b, self.row,
                                self.column))
        if len(tab) > 0:
            finish = time()
            delta = round(finish - start, 2)
            print("chargement terminé\n" +\
                    f"{len(tab)} references en {delta} secondes.\n")

        filename = '/' + self.filename + '_' +\
                    str(localtime().tm_hour) +\
                    str(localtime().tm_min) +\
                    str(localtime().tm_sec) + '_temp.csv'
        path = abspath('./ressources/save_temp')
        write.save(tab, path + filename, "w")

        filename = '/' + self.filename + '.csv'
        path = abspath('./ressources/sets')
        write.save(tab, path + filename, "w")

        return tab



    # def refresh_infos(self):














