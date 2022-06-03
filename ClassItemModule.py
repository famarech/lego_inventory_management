from api import bricklink_api as api

class ITEM:

    def __init__(self, lotid, dateadded, category, color, price, qty, bulk, image, description, condition, itemtype, itemid, sale, stockroom, itemweight, datelastsold, basecurrencycode, categoryname, categorynameunder, colorname, itemtypename, itemidname, box, row, column, dimensionx, dimensiony, dimensionz):
        self.lotid = lotid
        self.dateadded = dateadded
        self.category = category
        self.color = color
        self.price = price
        self.qty = qty
        self.bulk = bulk
        self.image = image
        self.description = description
        self.condition = condition
        self.itemtype = itemtype
        self.itemid = itemid
        self.sale = sale
        self.stockroom = stockroom
        self.itemweight = itemweight
        self.datelastsold = datelastsold
        self.basecurrencycode = basecurrencycode
        self.categoryname = categoryname
        self.categorynameunder = categorynameunder
        self.colorname = colorname
        self.itemtypename = itemtypename
        self.itemidname = itemidname
        self.box = box
        self.row = row
        self.column = column
        self.dimensionx = dimensionx
        self.dimensiony = dimensiony
        self.dimensionz = dimensionz


    def afficher(self):
        print(f"{self.itemid} : {self.color} : {self.qty} : {self.price} : {self.box} : {self.row} : {self.column} : {self.image}")

    def prix_total(self):
        a = self.price.replace(',','.')
        a = float(a)
        b = int(self.qty)
        return (a * b)

    def poid_total(self):
        a = self.itemweight.replace(',','.')
        a = float(a)
        b = int(self.qty)
        return (a * b)

    def sauvegarder(self):
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

    def transform_to_upload_bricklink(self):
        a = self.price.replace(',','.')
        b = self.box + ' ' + self.row + self.column
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

    def transform_to_impression(self, index):
        if (index % 2) == 0:
            pair = "pair"
        else:
            pair = "impair"
        content = '\t<ITEM value="' + pair + '">\n' +\
                    "\t\t<LINE>" + str(index) + "</LINE>\n" +\
                    "\t\t<ITEMID>" + self.itemid + "</ITEMID>\n" +\
                    "\t\t<ITEMIDNAME>" + self.itemidname + "</ITEMIDNAME>\n" +\
                    "\t\t<COLOR>" + self.color + "</COLOR>\n" +\
                    "\t\t<COLORNAME>" + self.colorname + "</COLORNAME>\n" +\
                    "\t\t<QTY>" + self.qty + "</QTY>\n" +\
                    "\t\t<BOX>" + self.box + "</BOX>\n" +\
                    "\t\t<ROW>" + self.row + "</ROW>\n" +\
                    "\t\t<COLUMN>" + self.column + "</COLUMN>\n"
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
        # ajouter dans la description? l'atat used ou new de la pièce
        json_obj = api.catalog_item.get_price_guide("Part", self.itemid, self.color, new_or_used="U")
        item.price = json_obj['data']['avg_price']
        # .replace('.', ',') est-ce que c'est necessaire ?