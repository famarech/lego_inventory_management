from ReadModule import get_extension
from os.path import abspath
import csv
from WriteModule import save
from ClassCatalogueModule import SET

class SETS:

    def __init__(self, path, where_from, type):
        self.path = get_extension(path)[0]
        self.filename = get_extension(path)[1]
        self.extension = get_extension(path)[2]
        self.wherefrom = where_from
        self.type = type
        self.tab = self.loading(path)




    def loading(self, file):
        tab = []
        with open(file, encoding="utf-8", newline='') as csvfile:
            data = csv.reader(csvfile.readlines()[1:], delimiter=';')
            for row in data:
                complete_path = self.path + row[0] + self.extension
                tab.append(SET(complete_path, self.wherefrom, self.type,
                                    row[1], row[3], row[4], row[5]))
        return tab

    def afficher(self):
        for set in self.tab:
            set.afficher()

    def fusionner(self, newpath, newfilename):
        size = len(self.tab)
        for i in range(1,size,1):
            self.tab[0].fusionner(self.tab[i])
        self.tab[0].filename = newfilename
        self.tab[0].sauvegarder(newpath, False)



    # refresh et save
    # rafraichir les infos spécifique du set
    # et sauvegarder dans un fichier from_pyth_inv_of_set