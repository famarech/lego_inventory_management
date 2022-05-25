import pyautogui
from time import sleep

def traduction(tab):
    sleep(2)
    for s in tab:
        pyautogui.write(s)
        pyautogui.press('enter')

azerty_min = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
traduc_min = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
azerty_maj = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
traduc_maj = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
azerty_chiffre = ['0','1','2','3','4','5','6','7','8','9']
traduc_chiffre = ['à','&','é','"',"'",'(','-','è','_','ç']
azerty_symbole_min =               ['œ','&','é','"',"'",'(','-','è','_','ç','à',')','=','^','$','ù','*',',',';',':','!','<']
traduc_symbole_min =               [' ','1',' ','3',"'",'5','-',' ','8',' ',' ','°','=','9','£',' ','µ',',',';','/','§','>']
azerty_symbole_maj_ver =           ['Œ','&','É','"',"'",'(','-','È','_','Ç','À',')','=','^','$','Ù','*',',',';',':','!','<']
traduc_symbole_maj_ver =           [' ','1',' ','3',"'",'5','-',' ','8',' ',' ','°','=','9','£',' ','µ',',',';','/','§','>']
azerty_symbole_touche_maj =        ['Œ','1','2','3',"4",'5','6','7','8','9','0','°','+','¨','£','%','µ','?','.','/','§','>']
traduc_symbole_touche_maj =        [' ','&','é','"',"'",'(','-','è','_','ç','à',' ','+',' ',' ','%',' ','?',';',':',' ','>']
azerty_symbole_touche_alt_gr =     ['“','´','~','#','{','[','|','`',' ','^','@',']','}','~','ê','²','³','¿','×','÷','¡','|']
traduc_symbole_touche_alt_gr =     [' ',' ','2','3','4','(','6','p',' ','9','0',')','+','2',' ',' ',' ',' ',' ',' ',' ','6']
azerty_symbole_touche_maj_alt_gr = ['”','·','É','¸','´','¨','¦','È','¯','Ç','À','ÿ','°',"'",'ë','Ù','¥','º','×','÷','˙','¦']
traduc_symbole_touche_maj_alt_gr = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',"'",' ',' ',' ',' ',' ',' ',' ',' ']
azerty_autre = ['\n','\t','\\']
traduc_autre = ['\n','\t','_']

azerty = [azerty_min, azerty_maj, azerty_chiffre, azerty_symbole_min, azerty_symbole_maj_ver, azerty_symbole_touche_maj, azerty_symbole_touche_alt_gr, azerty_symbole_touche_maj_alt_gr, azerty_autre]

traduc = [traduc_min, traduc_maj, traduc_chiffre, traduc_symbole_min, traduc_symbole_maj_ver, traduc_symbole_touche_maj, traduc_symbole_touche_alt_gr, traduc_symbole_touche_maj_alt_gr, traduc_autre]

for a in azerty:
    traduction(a)t

for t in traduc:
    traduction(t)

