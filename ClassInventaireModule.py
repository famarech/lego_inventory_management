from ClassItemModule import ITEM
from CutModule import cut_after
from CutModule import cut_before
from os import listdir
from os.path import abspath



class INVENTAIRE:

    def __init__(self, path):
        self.tab = []
        self.label = ["LOTID","DATEADDED", "CATEGORY", "COLOR", "PRICE", "QTY", "BULK", "IMAGE", "DESCRIPTION", "CONDITION", "ITEMTYPE", "ITEMID", "SALE", "STOCKROOM", "ITEMWEIGHT", "DATELASTSOLD", "BASECURRENCYCODE", "CATEGORYNAME", "CATEGORYNAMEUNDER", "COLORNAME", "ITEMTYPENAME", "ITEMIDNAME", "BOX", "LINE", "ROW", "DIMENSIONX", "DIMENSIONY", "DIMENSIONZ"]
        self.path = path
        self.str = self.read_file()
        self.extension = self.choice()
        self.prix = self.prix_total()
        self.poid = self.poid_total()
        self.qty = self.qty_total()
        self.prix_par_piece = self.prix / self.qty


    def read_file(self):
        file_in = open(self.path, "r")
        str = file_in.readlines()
        file_in.close()
        return str

    # # # permet de déterminer quel est le type d'extension pour pouvoir importer n'importe quel inventaire
    def choice(self):
        extension = self.path
        extension = cut_after(".", extension)
        if extension == "csv":
            self.tab = self.from_csv()
        elif extension == "xml":
            self.tab = self.from_xml()
        elif extension == "txt":
            self.tab = self.from_txt()
        return extension

    def from_csv(self):
        str = self.str
        tab = []
        for t in str:
            tab.append(t.split(';'))
        del tab[0]
        new_tab = INVENTAIRE.transform_item_full(tab)
        return new_tab

    def from_xml(self):
        str = self.str
        str = "".join(str)
        str = cut_after("INVENTORY>", str)
        str = cut_before("</INVENTORY", str)
        tab = []
        while len(str) > 15:
            str = cut_after("<ITEM>", str)
            b = cut_after("</ITEM>", str)
            new_tab = []
            for word in self.label:
                str = cut_after((word + ">"), str)
                a = cut_before(("</" + word), str)
                str = cut_after(("</" + word), str)
                new_tab.append(a)
            tab.append(new_tab)
        new_tab = []
        new_tab = INVENTAIRE.transform_item_full(tab)
        return new_tab

    def from_txt(self):
        file_in = open(self.path, 'r')
        tab = []
        for line in file_in.readlines():
            str = line.replace("\t", ";")
            str = str.replace("\n", "")
            str = str.split(";")
            tab.append(str)
        file_in.close()
        del tab[0]
        del tab[0]
        new_tab = INVENTAIRE.transform_item_partiel(tab)
        return new_tab

    def exist_picture(id, color):
        path = abspath('./03 - Pictures')
        list_pict = listdir(path)
        filename = "id" + id + "color" + color + ".jpg"
        if filename in list_pict:
            return ""
        return "Not Available"

    # # # permet quelque soit le type d'inventaire, d'avoir un format d'inventaire unique
    def transform_item_full(tab):
        new_tab= []
        for item in tab:
            new_tab.append(ITEM(item[0], item[1], item[2], item[3], item[4], item[5], item[6], INVENTAIRE.exist_picture(item[11], item[3]), item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[10], item[21], item[22], item[23], item[24], item[25], item[26], item[27].replace('\n', '')))
        return new_tab

    def transform_item_partiel(tab):
        new_tab= []
        for item in tab:
            new_tab.append(ITEM('', '', '', item[4], '0', item[3], '', '', '', '', '', item[1], '', '', '0', '', '', '', '', '', '', '', '', '', '', '', '', ''))
        return new_tab




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




    def sauvegarder(self, path_destination):
        # d'abord faire une sauvegarde du fichier avec un nom temporaire
        # enregistrer le fichier à chaque reference avec le time dans le nom de fichier ("a")
        # enfin ecraser le fichier source
        file_in = open(path_destination, "w")
        content = ";".join(self.label) + '\n'
        file_in.write(content)
        for item in self.tab:
            content = item.sauvegarder()
            file_in.write(content)
        file_in.close()

    def fusionner(self, inventory_to_add):
        # !!!! ATTENTION !!!! met à jour l'objet actuel d'origine avec un nouvel inventaire
        # inventory_to_add est l'inventaire à ajouter à l'objet actuel
        for item in inventory_to_add.tab:
            self.tab.append(item)

    def transform_to_upload_bricklink(self):
        PAQUET = 500
        index = 1
        for i in range(0, len(self.tab), PAQUET):
            partition = self.tab[i:(i+PAQUET)]
            content = "<INVENTORY>\n"
            for item in partition:
                content = content + item.transform_to_upload_bricklink()
            content = content + "</INVENTORY>"
            path = abspath('./05 - Upload') + "/upload(" + str(index) + ").txt"
            index += 1
            file_in = open(path, "w")
            file_in.write(content)

    def transform_to_impression(self):
        content = '<?xml version="1.0" encoding="UTF-8"?>\n' +\
                    '<?xml-stylesheet href="style_xml.css" type="text/css" ?>\n' +\
                    "<!-- commentaires --> \n\n" +\
                    "<INVENTORY>\n" +\
                    '\t<ITEM class="title">\n' +\
                    "\t\t<LINE>LINE</LINE>\n" +\
                    "\t\t<ITEMID>ITEMID</ITEMID>\n" +\
                    "\t\t<ITEMIDNAME>ITEMNAME</ITEMIDNAME>\n" +\
                    "\t\t<COLOR>COLOR</COLOR>\n" +\
                    "\t\t<COLORNAME>COLORNAME</COLORNAME>\n" +\
                    "\t\t<QTY>QTY</QTY>\n" +\
                    "\t\t<BOX>BOX</BOX>\n" +\
                    "\t\t<ROW>ROW</ROW>\n" +\
                    "\t\t<COLUMN>COLUMN</COLUMN>\n" +\
                    "\t</ITEM>\n"
        index = 1
        for item in self.tab:
            content = content + item.transform_to_impression(index)
            index += 1
        content = content + "</INVENTORY>"
        path = abspath('./04 - Impression') + '/impression_test.xml'
        file_in = open(path, "w")
        file_in.write(content)

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
        path = abspath('./04 - Impression') + "/html_test_" + str(number + 1) + ".html"
        file_in = open(path, "w")
        file_in.write(content)

    def get_price(self):
        for item in self.tab:
            item.get_price()
        path = abspath('./06 - Sauvegarde_temp/prices_temp.csv')
        self.sauvegarder(path)

    # def compare(self):
        #comparer deux inventaire pour trouver l'un dans l'autre