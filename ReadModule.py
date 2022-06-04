import xml.etree.ElementTree as ET
import csv
from os.path import abspath
from os.path import splitext
from ClassItemModule import ITEM

file_xml = abspath('./ressources/exemples/download_inv_store_from_blk_xml_format.txt')
file_csv_by_me = abspath('essai.csv')
file_csv_from_blk = abspath('./ressources/exemples/download_inv_store_from_blk.csv')


def from_csv_from_blk(file):
    tab = []
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
        for row in spamreader:
            print(len(row))
            # tab.append(ITEM(row[0], row[1], row[2], row[3], row[4],
            #                     row[5], row[6], row[7], row[8], row[9],
            #                     row[10], row[11], row[12], row[13], row[14],
            #                     row[15], row[16], row[17], row[18], row[19],
            #                     row[10], row[21], row[22], row[23], row[24],
            #                     row[25], row[26], row[27]))
    # del tab[0]
    return tab

from_csv_from_blk(file_csv_from_blk)


def read_file(self):
    file_in = open(self.path, "r")
    str = file_in.readlines()
    file_in.close()
    return str

# # # permet de déterminer quel est le type d'extension pour pouvoir importer n'importe quel inventaire


def from_csv(self):
    str = self.str
    tab = []
    for t in str:
        tab.append(t.split(';'))
    del tab[0]
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

# # # permet quelque soit le type d'inventaire, d'avoir un format d'inventaire unique
def transform_item_full(tab):
    new_tab= []
    for item in tab:
        new_tab.append(ITEM(item[0], item[1], item[2], item[3], item[4],
                            item[5], item[6], item[7], item[8], item[9],
                            item[10], item[11], item[12], item[13], item[14],
                            item[15], item[16], item[17], item[18], item[19],
                            item[10], item[21], item[22], item[23], item[24],
                            item[25], item[26], item[27].replace('\n', '')))
    return new_tab

def transform_item_partiel(tab):
    new_tab= []
    for item in tab:
        new_tab.append(ITEM('', '', '', item[4], '0',
                            item[3], '', '', '', '',
                            '', item[1], '', '', '0',
                            '', '', '', '', '',
                            '', '', '', '', '',
                            '', '', ''))
    return new_tab









def choice(file):
    root, extension = splitext(file)
    print(f"chargement de l'inventaire '.{extension}' en cours")
    # if extension == ".csv":
    #     self.tab = self.from_csv()
    # elif extension == ".xml":
    #     self.tab = self.from_xml_v2()
    # elif extension == ".txt":
    #     self.tab = self.from_txt()
    # if len(self.tab) > 0:
    #     print("chargement terminé\n")
    return extension

def from_xml_v2(file):
    tree = ET.parse(file)
    root = tree.getroot()
    tab = []
    for item in root:
        row = []
        for param in item:
            row.append(param.text)
        place = row[8].split()
        tab.append(ITEM(row[0], row[1], row[2], row[3], row[4],
                        row[5], row[6], row[7], '', row[9],
                        row[10], row[11], row[12], row[13], row[14],
                        row[15], row[16], '', '', '',
                        '', '', (' ').join(place[:-2]), place[-2], place[-1],
                        '', '', ''))
    return tab

def from_csv_by_me(file):
    tab = []
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar=' ')
        for row in spamreader:
            # print(len(row))
            tab.append(ITEM(row[0], row[1], row[2], row[3], row[4],
                                row[5], row[6], row[7], row[8], row[9],
                                row[10], row[11], row[12], row[13], row[14],
                                row[15], row[16], row[17], row[18], row[19],
                                row[10], row[21], row[22], row[23], row[24],
                                row[25], row[26], row[27]))
    del tab[0]
    return tab