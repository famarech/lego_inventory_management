from ClassItemModule import ITEM
from ReadModule import loading
from ReadModule import get_extension
from os.path import abspath
from time import time
from time import localtime



global label
label = ["LOTID","DATEADDED", "CATEGORY", "COLOR", "PRICE",
        "QTY", "BULK", "IMAGE", "DESCRIPTION", "CONDITION",
        "ITEMTYPE", "ITEMID", "SALE", "STOCKROOM", "ITEMWEIGHT",
        "DATELASTSOLD", "BASECURRENCYCODE", "CATEGORYNAME", "CATEGORYNAMEUNDER", "COLORNAME",
        "ITEMTYPENAME", "ITEMIDNAME", "BOX", "COLUMN", "ROW",
        "DIMENSIONX", "DIMENSIONY", "DIMENSIONZ"]




class INVENTAIRE:

    def __init__(self, path, where_from, type):

        self.path = get_extension(path)[0]
        self.filename = get_extension(path)[1]
        self.extension = get_extension(path)[2]
        self.where_from = where_from
        self.type = type
        self.tab = loading(path, where_from, type, self.filename, self.extension)

        self.prix = self.prix_total()
        self.poid = self.poid_total()
        self.qty = self.qty_total()
        self.prix_par_piece = self.prix / self.qty




    def afficher(self):
        for item in self.tab:
            item.afficher()

    def prix_total(self):
        somme = 0
        for item in self.tab:
            somme = somme + item.prix_total()
        return somme

    def poid_total(self):
        somme = 0
        for item in self.tab:
            somme = somme + item.poid_total()
        somme = somme / 1000
        return somme

    def qty_total(self):
        somme = 0
        for item in self.tab:
            somme = somme + int(item.qty)
        return somme




    def sauvegarder_csv(self, path_destination):
        # d'abord faire une sauvegarde du fichier avec un nom temporaire
        # enregistrer le fichier à chaque reference avec le time dans le nom de fichier ("a")
        # enfin ecraser le fichier source
        file_in = open(path_destination, "w")
        content = ";".join(label) + '\n'
        file_in.write(content)
        for item in self.tab:
            content = item.sauvegarder_format_csv()
            file_in.write(content)
        file_in.close()

    def fusionner(self, inventory_to_add):
        # !!!! ATTENTION !!!! met à jour l'objet actuel d'origine avec un nouvel inventaire
        # inventory_to_add est l'inventaire à ajouter à l'objet actuel
        for item in inventory_to_add.tab:
            self.tab.append(item)

    def transform_to_upload_bricklink_xml(self):
        PAQUET = 500 #nombre max autorisé par Bricklink
        index = 1
        for i in range(0, len(self.tab), PAQUET):
            partition = self.tab[i:(i+PAQUET)]
            content = "<INVENTORY>\n"
            for item in partition:
                content = content + item.transform_to_upload_bricklink_xml()
            content = content + "</INVENTORY>"
            path = abspath('./ressources/uploads') + "/upload(" + str(index) + ").txt"
            index += 1
            file_in = open(path, "w")
            file_in.write(content)
        print(f"creation des fichiers terminées, {index - 1} fichier(s) produit(s)\n")

    def transform_to_impression_html(self, number):
        content = '<!DOCTYPE html>\n\n' +\
                    '<html>\n\n' +\
                    '\t<head>\n' +\
                    '\t\t<title> Impression </title>\n' +\
                    '\t\t<meta charset="utf-8"/>\n' +\
                    '\t\t<link href="style_html.css" rel="stylesheet">\n' +\
                    '\t\t<!-- commentaires -->\n' +\
                    '\t</head>\n\n' +\
                    '\t<body>\n' +\
                    '\t\t<div class="title">\n' +\
                    '\t\t\t<p>IMAGE</p>\n' +\
                    '\t\t\t<p>ITEMID</p>\n' +\
                    '\t\t\t<p>ITEMIDNAME</p>\n' +\
                    '\t\t\t<p>COLOR</p>\n' +\
                    '\t\t\t<p>COLORNAME</p>\n' +\
                    '\t\t\t<p>QTY</p>\n' +\
                    '\t\t\t<p>BOX</p>\n' +\
                    '\t\t\t<p>ROW</p>\n' +\
                    '\t\t\t<p>COLUMN</p>\n' +\
                    '\t\t</div>\n'
        index = 1
        for item in self.tab:
            content = content + item.transform_to_impression_html(index)
            index += 1
        content = content + "\t</body>\n\n</html>"
        path = abspath('./ressources/printables') + "/printable(" + str(number + 1) + ").html"
        file_in = open(path, "w")
        file_in.write(content)

    def get_price(self):
        size = len(self.tab)
        time_per_item = 1
        finish = localtime(time() + (time_per_item * size))
        print("fin de la recherche de prix estimé à :\n" +\
                f"{finish.tm_hour}:{finish.tm_min}:{finish.tm_sec} -- heure local\n")
        for item in self.tab:
            item.get_price()
        # path = abspath('./ressources/save_temp/inventory_temp_hh_mm_ss.csv')
        # self.sauvegarder(path)

    def get_picture(self):
        return 0

    # def compare(self):
        #comparer deux inventaire pour trouver l'un dans l'autre