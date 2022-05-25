import pyautogui
from webbrowser import open
from webbrowser import open_new_tab
from time import sleep
from pyperclip import paste
from os import listdir
from os.path import abspath
from CutModule import cut_after
from CutModule import cut_before
from CutModule import traduction
from ClassInventaireModule import INVENTAIRE
from ClassItemModule import ITEM




def get_price(inventaire):
    blk = BRICKLINK(inventaire)
    for i in range(0, len(inventaire.tab), blk.paquet):
        partition = inventaire.tab[i:(i + blk.paquet)]
        blk.ouvrir()
        for item in partition:
            blk.acces_page(item)
            item.price = blk.get_price(item)
        path = abspath('./06 - Sauvegarde_temp/prices_temp.csv').replace('\\', '/')
        inventaire.sauvegarder(path)
        blk.fermer()

def get_picture(inventaire):
    blk = BRICKLINK(inventaire)
    for i in range(0, len(inventaire.tab), blk.paquet):
        partition = inventaire.tab[i:(i + blk.paquet)]
        blk.ouvrir()
        for item in partition:
            filename = "id" + item.itemid + "color" + item.color + ".jpg"
            if blk.exist_picture(filename) == False:
                blk.acces_page(item)
                blk.get_picture(item)
        blk.fermer()

def get_all(inventaire):
    blk = BRICKLINK(inventaire)
    for i in range(0, len(inventaire.tab), blk.paquet):
        partition = inventaire.tab[i:(i + blk.paquet)]
        blk.ouvrir()
        for item in partition:
            blk.acces_page(item)
            item.price = blk.get_price(item)
            filename = "id" + item.itemid + "color" + item.color + ".jpg"
            if blk.exist_picture(filename) == False:
                blk.get_picture(item)
        path = abspath('./06 - Sauvegarde_temp/prices_temp.csv').replace('\\', '/')
        inventaire.sauvegarder(path)
        blk.fermer()




class BRICKLINK():

    def __init__(self, inventaire):
        self.inventaire = inventaire
        self.html0 = "https://www.bricklink.com"
        self.html1 = "https://www.bricklink.com/catalogPG.asp?P="
        self.html2 = "&ColorID="
        self.pseudo = 'famarech'
        self.mdp = 'Vila1981'
        self.paquet = 50
        self.path_picture = abspath('./03 - Pictures/')
        self.path_download = '/home/moyen/Téléchargements'
        self.screen = pyautogui.size()

    def ouvrir(self):
        open(self.html0, new=0, autoraise=True)
        sleep(15)
        pyautogui.click(self.screen.width * 0.388, self.screen.height * 0.827, 1, button='primary')
        pyautogui.click(self.screen.width * 0.678, self.screen.height * 0.176, 1, button='primary')
        sleep(3)
        pyautogui.write(self.pseudo)
        pyautogui.press('tab')
        pyautogui.write(traduction(self.mdp))
        pyautogui.press('enter')
        sleep(2)

    def fermer(self):
        sleep(1)
        pyautogui.click(self.screen.width * 0.991, self.screen.height * 0.041, 1, button='primary')
        print("patienter 30 secondes avant la fermeture de Firefox")
        sleep(30)

    def acces_page(self, item):
        url = self.html1 + item.itemid + self.html2 + item.color
        open_new_tab(url)

    def get_price(self, item):
        sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        sleep(1)
        str = paste()
        prix = self.exist_price(str)
        return prix

    def exist_price(self, str):
        str = cut_after("Used", str)
        str = cut_after("Used", str)
        str = cut_after("Qty Avg Price:", str)
        str = cut_after("Qty Avg Price:", str)
        str = cut_after("Qty Avg Price:", str)
        str = cut_after("Avg Price:", str)
        str = cut_after("EUR ", str)
        str = cut_before("Qty Avg Price", str)
        try:
            float(str)
        except:
            str = '0.01'
        str = str.replace('.',',')
        str = str.replace('\n','')
        return str

    def get_picture(self, item):
        sleep(4)
        pyautogui.click(self.screen.width * 0.518, self.screen.height * 0.350, 1, button='secondary')
        sleep(1)
        pyautogui.click(self.screen.width * 0.541, self.screen.height * 0.532, 1, button='primary')
        sleep(1.5)
<<<<<<< HEAD
        pyautogui.hotkey('ctrl', 'a')
=======
>>>>>>> 5f793dc68112e8a22a17829dc9ed237d9e9bf2db
        pyautogui.hotkey('ctrl', 'c')
        sleep(1)
        str = paste()
        if str != "noImage.gif":
            filename = "id" + item.itemid + "color" + item.color
            pyautogui.write(traduction(filename))
            for i in range(3):
                sleep(0.5)
                pyautogui.press('enter')
        else:
            pyautogui.click(self.screen.width * 0.068, self.screen.height * 0.053, 1, button='primary')
            item.image = "Not Available"

    def exist_picture(self, filename):
        list_pict = listdir(self.path_picture)
        list_down = listdir(self.path_download)
        if filename in list_pict or filename in list_down:
            return True
        return False

# mettre en place des interruptions en cas de deconnexion à la page internet
# mise en place d'un fichier d'écriture des references non trouvées