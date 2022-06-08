from os.path import abspath

# après des grosses opérations (recherche de prix par exemple)
# à chaque item qui met à jour son prix,
# faire une sauvegarde dans un nouveau dossier temporaire avec la fonction save_temp()
#
# une fonction sauvegarde permet d'enregistrer l'inventaire dans un dossier au format souhaité
# dans un dossier souhaité
# soit pour upload, soit pour impression, soit pour bdd en csv
# si pas de fichier spécifié, enregistrer dans ressources appropriés

global label
label = ["LOTID","DATEADDED", "CATEGORY", "COLOR", "PRICE",
        "QTY", "BULK", "IMAGE", "DESCRIPTION", "CONDITION",
        "ITEMTYPE", "ITEMID", "SALE", "STOCKROOM", "WEIGHT",
        "DATELASTSOLD", "CURRENCY", "CATEGORYNAME", "CATNAME1", "CATNAME2",
        "CATNAME3", "CATNAME4", "COLORNAME", "RGB", "COLORTYPE",
        "SUBCONDITION", "REMARKS", "TIERQTY1", "TIERPRICE1", "TIERQTY2",
        "TIERPRICE2", "TIERQTY3", "TIERPRICE3", "RESERVEDFOR", "RETAIN",
        "SUPERLOTID", "SUPERLOTQTY", "EXTDESCRIPTION", "ITEMTYPENAME", "ITEMIDNAME",
        "DIMENSIONX", "DIMENSIONY", "DIMENSIONZ", "BOX", "COLUMN",
        "ROW"]




def save(tab, path, mode):
    file_in = open(path, mode, encoding="utf-8")
    content = ";".join(label) + '\n'
    file_in.write(content)
    for item in tab:
        content = item.sauvegarder_format_csv()
        file_in.write(content)
    file_in.close()
    return 0

def transform_to_upload_blk_xml(tab, filename):
    PAQUET = 500 #nombre max autorisé par Bricklink
    index = 1
    for i in range(0, len(tab), PAQUET):
        partition = tab[i:(i+PAQUET)]
        content = '<?xml version="1.0" encoding="UTF-8"?>\n' +\
                    "<INVENTORY>\n"
        for item in partition:
            content = content + item.transform_to_upload_blk_xml()
        content = content + "</INVENTORY>"
        path = abspath('./ressources/uploads') + "/" +\
                        filename + "_upload(" + str(index) + ").txt"
        index += 1
        file_in = open(path, "w", encoding="utf-8")
        file_in.write(content)
    print(f"creation des fichiers terminées, {index - 1} fichier(s) produit(s)\n")

def transform_to_impression_html(tab, filename):
    content = '<!DOCTYPE html>\n\n' +\
                '<html>\n\n' +\
                '\t<head>\n' +\
                '\t\t<title>' + filename + '</title>\n' +\
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
    for item in tab:
        content = content + item.transform_to_impression_html(index)
        index += 1
    content = content + "\t</body>\n\n</html>"
    path = abspath('./ressources/printables') + "/" +\
                    filename + "_printable.html"
    file_in = open(path, "w", encoding="utf-8")
    file_in.write(content)

def recherche_impression_html(content, filenameset, filenameinv):
    title = '<!DOCTYPE html>\n\n' +\
            '<html>\n\n' +\
            '\t<head>\n' +\
            '\t\t<title>Recherche de ' + filenameset + ' dans ' + filenameinv + '</title>\n' +\
            '\t\t<meta charset="utf-8"/>\n' +\
            '\t\t<link href="style_recherche.css" rel="stylesheet">\n' +\
            '\t\t<!-- commentaires -->\n' +\
            '\t</head>\n\n' +\
            '\t<body>\n' +\
            '\t\t<div class="title">\n' +\
            '\t\t\t<p>IMAGE</p>\n' +\
            '\t\t\t<p>ITEMID</p>\n' +\
            '\t\t\t<p>ITEMIDNAME</p>\n' +\
            '\t\t\t<p>COLOR</p>\n' +\
            '\t\t\t<p>COLORNAME</p>\n' +\
            '\t\t\t<p>QTY NECESSAIRE</p>\n' +\
            '\t\t\t<p>QTY DISPONIBLE</p>\n' +\
            '\t\t\t<p>QTY A COMMANDER</p>\n' +\
            '\t\t\t<p>BOX</p>\n' +\
            '\t\t\t<p>ROW</p>\n' +\
            '\t\t\t<p>COLUMN</p>\n' +\
            '\t\t</div>\n'
    content = title + content
    content += "\t</body>\n\n</html>"
    path = abspath('./ressources/printables') + "/" +\
                    filenameset + '_in_' + filenameinv + "_printable.html"
    file_in = open(path, "w", encoding="utf-8")
    file_in.write(content)