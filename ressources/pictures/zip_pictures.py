from os import listdir
import zipfile as zp


list = listdir('./')
fin = len(list) - 3
paquet = 2000

j = 0
index = 1
while j < fin:
    i = j
    filename = 'pictures' + str(index) + '.zip'
    print(filename)

    with zp.ZipFile(filename, 'w', compression=zp.ZIP_DEFLATED) as myzip:
        while i < (j + paquet):
            if i <= fin:
                myzip.write(list[i])
            i += 1
        myzip.close()

    index += 1
    j += paquet