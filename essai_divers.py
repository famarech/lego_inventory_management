import pyautogui
from time import sleep
from pyperclip import paste







def ouvrir():
    # Point(x=682, y=845)
    pyautogui.click(u.width * 0.355, u.height * 0.782, 1, button='primary')
    # Point(x=1255, y=167)
    pyautogui.click(u.width * 0.653, u.height * 0.155, 1, button='primary')


def fermer():
    # Point(x=1881, y=12)
    pyautogui.click(u.width * 0.979, u.height * 0.011, 1, button='primary')


def get_price():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')


def get_picture():
    # Point(x=958, y=344)
    pyautogui.click(u.width * 0.498, u.height * 0.318, 1, button='secondary')
    # Point(x=1024, y=583)
    pyautogui.click(u.width * 0.533, u.height * 0.539, 1, button='primary')
    # Point(x=1850, y=1008)
    pyautogui.click(u.width * 0.963, u.height * 0.933, 1, button='primary')


def point():
    u = pyautogui.size()
    p = pyautogui.position()
    sleep(3)
    print(p.x / u.width)
    print(p.y / u.height)

point()
