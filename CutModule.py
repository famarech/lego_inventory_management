import json as _json
import pathlib as _pathlib
from os.path import abspath

def cut_after(mot, str):
    index = str.find(mot)
    if index >= 0:
        index = index + (len(mot))
    else:
        index = 0
    return str[index:]

def cut_before(mot, str):
    index = str.find(mot)
    if index >= 0:
        index = index
    else:
        index = len(str)
    return str[:index]