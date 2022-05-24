import pyautogui
from time import sleep
from pyperclip import paste
# données pour ubuntu

def ouvrir():
    u = pyautogui.size()
    pyautogui.click(u.width * 0.388, u.height * 0.827, 1, button='primary')
    pyautogui.click(u.width * 0.678, u.height * 0.176, 1, button='primary')

def fermer():
    u = pyautogui.size()
    pyautogui.click(u.width * 0.991, u.height * 0.041, 1, button='primary')

def get_price():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')

def get_picture():
    u = pyautogui.size()
    pyautogui.click(u.width * 0.518, u.height * 0.350, 1, button='secondary')
    sleep(1)
    pyautogui.click(u.width * 0.541, u.height * 0.532, 1, button='primary')
    sleep(1)
    pyautogui.click(u.width * 0.068, u.height * 0.053, 1, button='primary')

def point():
    u = pyautogui.size()
    sleep(3)
    p = pyautogui.position()
    print(p.x / u.width)
    print(p.y / u.height)

def password():
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['@','&','~','"','{','(','|','','_','^']
    
    sleep(2)
    for s in symbols:
        pyautogui.write(s)
    pyautogui.press('enter')
    
def rot(number):
    symbols = ['@','&','~','"','{','(','|','_','^']
    return symbols[number]
    
def traduction(str):
    new_str = []
    for s in str:
        try:
            int(s)
            new_str.append(rot(s))
        except:
            new_str.append(s)
    return "".join(new_str)

sleep(2)
pyautogui.write('')
pyautogui.press('enter')
    