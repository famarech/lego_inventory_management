import xml.etree.ElementTree as ET
import csv
from os.path import abspath
from os.path import splitext
from ClassItemModule import ITEM
from json import load

file_xml = abspath('./ressources/exemples/download_inv_store_from_blk_xml_format.txt')
file_csv_by_me = abspath('essai.csv')
file_csv_from_blk = abspath('./ressources/exemples/download_inv_store_from_blk.csv')
file_txt_from_blk = abspath('./ressources/exemples/download_inv_store_from_blk_tab_delimited.txt')
file_set_xml = abspath('./ressources/exemples/set_from_blk.xml')
file_set_txt = abspath('./ressources/exemples/set_from_blk.txt')





def from_txt_set(file):
    tab = []
    with open(file, newline='') as csvfile:
        data = csv.reader(csvfile.readlines()[2:], delimiter='\t')
        for row in data:
            # row[6] est ALTERNATE, faut-il le décompter ?
            if row[8] == "N" and row[5] == "N" and row[0] == "P":
                tab.append(ITEM('', '', '', row[4], '',
                                row[3], '', '', '', '',
                                row[0], row[1], '', '', '',
                                '', '', '', '', '',
                                row[2], '', '', '', '',
                                '', '', ''))
    return tab



def from_xml_set(file):
    tree = ET.parse(file)
    root = tree.getroot()
    tab = []
    for item in root:
        # item[5].text est ALTERNATE, faut-il le décompter ?
        if item[7].text == "N" and item[4].text == "N" and item[0].text == "P":
            tab.append(ITEM('', '', '', item[3].text, '',
                            item[2].text, '', '', '', '',
                            item[0].text, item[1].text, '', '', '',
                            '', '', '', '', '',
                            '', '', '', '', '',
                            '', '', ''))
    return tab



set = from_txt_set(file_set_txt)
for each in set:
    each.afficher()














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


def get_category(laurel, hardy, value, file):
    file = abspath('./ressources/' + file + '.json')
    with open(file) as mon_fichier:
        data = load(mon_fichier)
    for d in data:
        if d[laurel] == value:
            return d[hardy]
    return f"{hardy} Not Available"

def from_txt_from_blk(file):
    tab = []
    with open(file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter='\t')
        try:
            for i, row in enumerate(data):
                if i > 1:
                    a = row[5].split()
                    b = get_category("colorname", "colorid", row[1], "colors")
                    c = row[7].replace('â‚¬', '')
                    tab.append(ITEM(row[0], row[26], row[2], b, c,
                                        row[8], row[9], '', (' ').join(a[:-3]), row[3],
                                        '', row[12], row[10], row[20], row[24],
                                        row[27], row[28], '', '', row[1],
                                        '', '', (' ').join(a[-4:-2]), a[-2], a[-1],
                                        '', '', ''))
        except UnicodeDecodeError:
            print("Impossible de charger l'inventaire dans sa totalité\n" +\
                    "certaines références n'ont pas été créées\n"
                    "fichier provenant de Bricklink contenant des '''Chinese Logogram'''\n" +\
                    "A effacer manuellement\n\n")
    return tab

def from_csv_from_blk(file):
    tab = []
    with open(file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        try:
            for i, row in enumerate(data):
                if i > 1:
                    a = row[5].split()
                    b = get_category("colorname", "colorid", row[1], "colors")
                    c = row[7].replace('â‚¬', '')
                    tab.append(ITEM(row[0], row[26], row[2], b, c,
                                        row[8], row[9], '', (' ').join(a[:-3]), row[3],
                                        '', row[12], row[10], row[20], row[24],
                                        row[27], row[28], '', '', row[1],
                                        '', '', (' ').join(a[-4:-2]), a[-2], a[-1],
                                        '', '', ''))
        except UnicodeDecodeError:
            print("Impossible de charger l'inventaire dans sa totalité\n" +\
                    "certaines références n'ont pas été créées\n"
                    "fichier provenant de Bricklink contenant des '''Chinese Logogram'''\n" +\
                    "A effacer manuellement\n\n")
    return tab



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
        data = csv.reader(csvfile.readlines()[:1], delimiter=';', quotechar=' ')
        for row in data:
            tab.append(ITEM(row[0], row[1], row[2], row[3], row[4],
                                row[5], row[6], row[7], row[8], row[9],
                                row[10], row[11], row[12], row[13], row[14],
                                row[15], row[16], row[17], row[18], row[19],
                                row[10], row[21], row[22], row[23], row[24],
                                row[25], row[26], row[27]))
    return tab



