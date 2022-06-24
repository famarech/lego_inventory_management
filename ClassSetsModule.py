from ReadModule import get_extension
from os.path import abspath
import csv
from WriteModule import save
from ClassInventaireModule import SET

class SETS:

    def __init__(self, path, where_from, type):
        self.path = get_extension(path)[0]
        self.filename = get_extension(path)[1]
        self.extension = get_extension(path)[2]
        self.wherefrom = where_from
        self.type = type
        self.tab = []
        self.list = self.loading(path)




    def loading(self, file):
        list = []
        tab = []
        with open(file, encoding="utf-8", newline='') as csvfile:
            data = csv.reader(csvfile.readlines()[1:], delimiter=';')
            for row in data:

                # list.append(abspath('./ressources/sets/') + '/' + row[0] + '.csv')
                # filename = '/' + row[0] + '.csv'
                # path = abspath('./ressources/sets/')
                # save(tab, path + filename, "w")

                complete_path = self.path + row[0] + self.extension
                print(complete_path)
                self.tab.append(SET(complete_path, self.wherefrom, self.type,
                                    row[1], row[3], row[4], row[5]))
        return list







invS = SETS(abspath('./ressources/exemples/from_user_inv_of_sets.csv'), 'user', 'sets')

for s in invS:
    print(s)