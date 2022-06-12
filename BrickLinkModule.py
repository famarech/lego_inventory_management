import pyautogui
import webbrowser as wb
from time import sleep
from pyperclip import paste
from pyperclip import copy
from os import listdir
from os.path import abspath
import json




def get_picture(inventaire):
    sleep(3)
    blk = BRICKLINK(inventaire)
    for i in range(0, len(inventaire.tab), blk.paquet):
        partition = inventaire.tab[i:(i + blk.paquet)]
        blk.ouvrir()
        for item in partition:
            filename = "id" + item.itemid + "color" + item.colorid + ".jpg"
            if blk.exist_picture(filename) == False:
                blk.acces_page(item)
                blk.get_picture(item)
        blk.fermer()




class BRICKLINK():

    def __init__(self, inventaire):
        self.inventaire = inventaire
        self.html0 = "https://www.bricklink.com"
        self.html1 = "https://www.bricklink.com/catalogPG.asp?P="
        self.html2 = "&ColorID="
        self.pseudo = ''
        self.mdp = ''
        self.paquet = 50
        self.path_picture = abspath('./ressources/pictures/')
        self.path_download = '/home/gros_pc/Téléchargements'
        self.screen = pyautogui.size()

        self.get_mdps()

    def get_mdps(self):
        file = abspath('./ressources/mdp.json')
        with open(file) as mon_fichier:
            data = json.load(mon_fichier)
        self.pseudo = data["Pseudo"]
        self.mdp = data["MDP"]

    def ouvrir(self):
        wb.open(self.html0, new=1, autoraise=True)
        sleep(8)
        pyautogui.click(self.screen.width * 0.388, self.screen.height * 0.827, 1, button='primary')
        pyautogui.click(self.screen.width * 0.678, self.screen.height * 0.176, 1, button='primary')
        sleep(3)
        pyautogui.write(self.pseudo)
        pyautogui.press('tab')
        pyautogui.write(self.mdp)
        pyautogui.press('enter')
        sleep(2)

    def fermer(self):
        sleep(1)
        pyautogui.click(self.screen.width * 0.991, self.screen.height * 0.041, 1, button='primary')
        print("patienter 30 secondes avant la fermeture de Firefox")
        sleep(30)

    def acces_page(self, item):
        url = self.html1 + item.itemid + self.html2 + item.colorid
        wb.open_new_tab(url)

    def get_picture(self, item):
        sleep(4)
        pyautogui.click(self.screen.width * 0.518, self.screen.height * 0.350, 1, button='secondary')
        sleep(1)
        pyautogui.click(self.screen.width * 0.541, self.screen.height * 0.532, 1, button='primary')
        sleep(1.5)
        pyautogui.hotkey('ctrl', 'c')
        sleep(1)
        str = paste()
        if str != "noImage.gif":
            filename = "id" + item.itemid + "color" + item.colorid + ".jpg"
            pyautogui.hotkey('ctrl', 'a')
            sleep(1)
            copy(filename)
            # pyautogui.write(filename)
            sleep(1)
            pyautogui.hotkey('ctrl', 'v')
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