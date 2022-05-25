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

def rot(number):
    symbols = ['@','&','~','"','{','(','|','7','_','^']
    # caractère pour le nombre 7 introuvable 
    return symbols[number]
    
def traduction(str):
    new_str = []
    for s in str:
        try:
            new_str.append(rot(int(s)))
        except:
            new_str.append(s)
    return "".join(new_str)
