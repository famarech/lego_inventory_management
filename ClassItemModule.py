from api import bricklink_api as api
from os.path import abspath
from os.path import exists
from os import listdir
from json import load

global list_dict
list_pict = listdir(abspath('./ressources/pictures'))




class ITEM:

    def __init__(self, lotid, dateadded, category, color, price,
                        qty, bulk, image, description, condition,
                        itemtype, itemid, sale, stockroom, weight,
                        datelastsold, basecurrencycode, categoryname, categorynameunder, colorname,
                        itemtypename, itemidname, box, row, column,
                        dimensionx, dimensiony, dimensionz):
        self.lotid = lotid
        self.dateadded = dateadded
        self.category = self.get_category("Number",
                                            "Category ID",
                                            itemid,
                                            "parts")
        self.color = color
        self.price = price.replace('.',',')
        self.qty = qty.replace('.',',')
        self.bulk = bulk
        self.image = self.exist_picture(itemid, color, image)
        self.description = description
        self.condition = "U" if condition == "" else condition
        self.itemtype = itemtype
        self.itemid = itemid
        self.sale = sale
        self.stockroom = stockroom
        self.weight = self.get_category("Number",
                                            "weight",
                                            itemid,
                                            "parts").replace('.',',')
        self.datelastsold = datelastsold
        self.basecurrencycode = basecurrencycode
        self.categoryname = self.get_category("categoryid",
                                                "categoryname",
                                                category,
                                                "categories")
        self.categorynameunder = categorynameunder
        self.colorname = self.get_category("colorid",
                                                "colorname",
                                                color,
                                                "colors")
        self.itemtypename = self.get_category("itemtypeid",
                                            "itemtypename",
                                            itemtype,
                                            "itemtypes")
        self.itemidname = self.get_category("Number",
                                                "Name",
                                                itemid,
                                                "parts")
        self.box = box
        self.row = row
        self.column = column
        self.dimensionx = dimensionx.replace('.',',')
        self.dimensiony = dimensiony.replace('.',',')
        self.dimensionz = dimensionz.replace('.',',')

    def exist_picture(self, itemid, color, image):
        filename = "id" + itemid + "color" + str(color) + ".jpg"
        if image == filename:
            return image
        else:
            if not(filename in list_pict):
                return "Not Available"
            return filename

    def get_category(self, laurel, hardy, value, file):
        file = abspath('./ressources/' + file + '.json')
        with open(file) as mon_fichier:
            data = load(mon_fichier)
        for d in data:
            if d[laurel] == value:
                return d[hardy]
        return f"{hardy} Not Available"

    def afficher(self):
        print(f"{self.itemid} : {self.color} : {self.qty} : {self.price}€" +\
                f"dans {self.box} : {self.row}{self.column}")

    def prix_total(self):
        a = float(self.price.replace(',','.'))
        b = float(self.qty.replace(',','.'))
        return round(a * b, 2)

    def poid_total(self):
        # en grammes
        a = float(self.itemweight.replace(',','.'))
        b = float(self.qty.replace(',','.'))
        return round(a * b, 2)

    def sauvegarder_format_csv(self):
        a = str(self.price).replace('.',',')
        b = str(self.qty).replace('.',',')
        c = str(self.itemweight).replace('.',',')
        content = self.lotid + ";" +\
                self.dateadded + ";" +\
                self.category + ";" +\
                self.color  + ";" +\
                a + ";" +\
                b + ";" +\
                self.bulk + ";" +\
                self.image + ";" +\
                self.description + ";" +\
                self.condition + ";" +\
                self.itemtype + ";" +\
                self.itemid + ";" +\
                self.sale + ";" +\
                self.stockroom + ";" +\
                c + ";" +\
                self.datelastsold + ";" +\
                self.basecurrencycode + ";" +\
                self.categoryname + ";" +\
                self.categorynameunder + ";" +\
                self.colorname + ";" +\
                self.itemtypename + ";" +\
                self.itemidname + ";" +\
                self.box + ";" +\
                self.row + ";" +\
                self.column + ";" +\
                self.dimensionx + ";" +\
                self.dimensiony + ";" +\
                self.dimensionz + '\n'
        return content

    def transform_to_upload_bricklink_xml(self):
        a = self.price.replace(',','.')
        b = self.box + ' ' + self.row + ' ' + self.column
        # attention la quantité ne doit pas être nulle
        content = "\t<ITEM>\n"
        required = "\t\t<CATEGORY>" + self.category + "</CATEGORY>\n" +\
                    "\t\t<COLOR>" + self.color + "</COLOR>\n" +\
                    "\t\t<PRICE>" + a + "</PRICE>\n" +\
                    "\t\t<QTY>" + self.qty + "</QTY>\n" +\
                    "\t\t<CONDITION>" + self.condition + "</CONDITION>\n" +\
                    "\t\t<ITEMTYPE>" + self.itemtype + "</ITEMTYPE>\n" +\
                    "\t\t<ITEMID>" + self.itemid + "</ITEMID>\n" +\
                    "\t\t<STOCKROOM>" + self.stockroom + "</STOCKROOM>\n" +\
                    "\t\t<DESCRIPTION>" + b + "</DESCRIPTION>\n"
        not_required = "\t\t<LOTID>" + self.lotid + "</LOTID>\n" +\
                    "\t\t<DATEADDED>" + self.dateadded + "</DATEADDED>\n" +\
                    "\t\t<BULK>" + self.bulk + "</BULK>\n" +\
                    "\t\t<IMAGE>" + self.image + "</IMAGE>\n" +\
                    "\t\t<SALE>" + self.sale + "</SALE>\n" +\
                    "\t\t<ITEMWEIGHT>" + self.itemweight + "</ITEMWEIGHT>\n" +\
                    "\t\t<DATELASTSOLD>" + self.datelastsold + "</DATELASTSOLD>\n" +\
                    "\t\t<BASECURRENCYCODE>" + self.basecurrencycode + "</BASECURRENCYCODE>\n"
        content = content + required #+ not_required
        content = content + "\t</ITEM>\n"
        return content

    def transform_to_impression_html(self, index):
        if self.image != "Not Available":
            path_picture = "../03 - Pictures/id" + self.itemid + "color" + self.color + ".jpg"
        else:
            path_picture = "../03 - Pictures/noImage.jpg"
        if (index % 2) == 0:
            pair = "pair"
        else:
            pair = "impair"
        content = '\t\t<div class="' + pair + '">\n' +\
                    '\t\t\t<img src="' + path_picture + '">\n' +\
                    '\t\t\t<p>' + self.itemid + '</p>\n' +\
                    '\t\t\t<p class="itemidname">' + self.itemidname + '</p>\n' +\
                    '\t\t\t<p>' + self.color + '</p>\n' +\
                    '\t\t\t<p>' + self.colorname + '</p>\n' +\
                    '\t\t\t<p>' + self.qty + '</p>\n' +\
                    '\t\t\t<p>' + self.box + '</p>\n' +\
                    '\t\t\t<p>' + self.row + '</p>\n' +\
                    '\t\t\t<p>' + self.column + '</p>\n' +\
                    '\t\t</div>\n'
        return content

    def get_price(self):
        if self.itemtype == 'P':
            type = 'Part'
        json_obj = api.catalog_item.get_price_guide(type, self.itemid, int(self.color), new_or_used= self.condition)
        self.price = (json_obj['data']['avg_price']).replace('.', ',')