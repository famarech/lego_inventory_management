import xml.etree.ElementTree as ET
import csv
from os.path import abspath
from os.path import splitext
from os.path import split
from ClassItemModule import ITEM
from json import load
from time import time





def get_extension(path):
    head, tail = split(path)
    root, extension = splitext(path)
    return [head + '\\',
            tail[:tail.index('.')],
            extension]

def get_category(laurel, hardy, value, file):
    file = abspath('./ressources/' + file + '.json')
    with open(file) as mon_fichier:
        data = load(mon_fichier)
    for d in data:
        if d[laurel] == value:
            return d[hardy]
    return f"{hardy} Not Available"




def from_blk_set_txt(file):
    tab = []
    with open(file, encoding="utf-8", newline='') as csvfile:
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

def from_blk_set_xml(file):
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

def from_blk_inv_xml_txt(file):
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

def from_blk_inv_tab_txt(file):
    tab = []
    with open(file, encoding="utf-8", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter='\t')
        for i, row in enumerate(data):
            if i > 1:
                a = row[5].split()
                b = get_category("colorname", "colorid", row[1], "colors")
                # c'est cette variable b qui provoque le ralentissement
                c = row[7].replace('â‚¬', '')
                tab.append(ITEM(row[0], row[26], row[2], b, c,
                                    row[8], row[9], '', (' ').join(a[:-3]), row[3],
                                    '', row[12], row[10], row[20], row[24],
                                    row[27], row[28], '', '', row[1],
                                    '', '', (' ').join(a[-4:-2]), a[-2], a[-1],
                                    '', '', ''))
    return tab

def from_blk_semicolon_csv(file):
    tab = []
    with open(file, encoding="utf-8", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(data):
            if i > 1:
                a = row[5].split()
                b = get_category("colorname", "colorid", row[1], "colors")
                # c'est cette variable b qui provoque le ralentissement
                c = row[7].replace('â‚¬', '')
                tab.append(ITEM(row[0], row[26], row[2], b, c,
                                    row[8], row[9], '', (' ').join(a[:-3]), row[3],
                                    '', row[12], row[10], row[20], row[24],
                                    row[27], row[28], '', '', row[1],
                                    '', '', (' ').join(a[-4:-2]), a[-2], a[-1],
                                    '', '', ''))
    return tab

def from_pyth_semicolon_csv(file):
    tab = []
    with open(file, encoding="utf-8", newline='') as csvfile:
        data = csv.reader(csvfile.readlines()[:1], delimiter=';', quotechar=' ')
        for row in data:
            tab.append(ITEM(row[0], row[1], row[2], row[3], row[4],
                                row[5], row[6], row[7], row[8], row[9],
                                row[10], row[11], row[12], row[13], row[14],
                                row[15], row[16], row[17], row[18], row[19],
                                row[10], row[21], row[22], row[23], row[24],
                                row[25], row[26], row[27]))
    return tab








def loading(path, where_from, type, filename, extension):
    print(f"chargement de l'inventaire '''{filename}{extension}''' en cours")
    start = time()

    if where_from == 'blk':
        if type == 'inv':
            if extension == '.txt':
                try:
                    tab = from_blk_inv_xml_txt(path)
                except:
                    tab = from_blk_inv_tab_txt(path)
            elif extension == '.csv':
                tab = from_blk_semicolon_csv(path)
        elif type == 'set':
            if extension == '.xml':
                tab = from_blk_set_xml(path)
            elif extension == '.txt':
                tab = from_blk_set_txt(path)
    elif where_from == 'pyth':
        if type == 'inv' or type == 'upload':
            # if extension == '.txt':
            #     tab = from_blk_inv_xml_txt(path)
            # el
            if extension == '.csv':
                tab = from_pyth_semicolon_csv(path)
        # elif type == 'impression':
    # elif where_from == 'user':
    else:
        print("format non reconnu\n\t\t\tABANDON\n")
        exit()

    if len(tab) > 0:
        finish = time()
        delta = round(finish - start, 2)
        print("chargement terminé\n" +\
                f"{len(tab)} references en {delta} secondes.\n")
    return extension