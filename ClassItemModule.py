from api import bricklink_api as api
from os.path import abspath
from os.path import exists
from os import listdir
from json import load

global list_dict
list_pict = listdir(abspath('./ressources/pictures'))




class ITEM:

    def __init__(self, lotid, dateadded, categoryid, colorid, price,
                    qty, bulk, urlimage, description, condition,
                    itemtype, itemid, salediscount, stockroom, weight,
                    datelastsold, currency, categorynamefull, categoryname1, categoryname2,
                    categoryname3, categoryname4, colorname, colorrgb, colortype,
                    subcondition, remarks, tierqty1, tierprice1, tierqty2,
                    tierprice2, tierqty3, tierprice3, reservedfor, retain,
                    superlotid, superlotqty, extdescription, itemtypename, itemidname,
                    dimensionx, dimensiony, dimensionz, box, row,
                    column):
        self.lotid = lotid
        self.dateadded = dateadded
        self.categoryid = categoryid
        self.colorid = self.check_color(colorid, colorname)
        self.price = price.replace('.',',')
        self.qty = qty.replace('.',',')
        self.bulk = bulk
        self.urlimage = self.exist_picture(itemid, colorid, urlimage)
        self.description = description
        self.condition = self.what_condition(condition)
        self.itemtype = 'P' if itemtype == 'Parts' else itemtype
        self.itemid = itemid
        self.salediscount = salediscount
        self.stockroom = 'Y' if stockroom == 'Yes' else stockroom
        self.weight = weight.replace('.',',')
        self.datelastsold = datelastsold
        self.currency = currency
        self.categorynamefull = categorynamefull
        self.categoryname1 = categoryname1
        self.categoryname2 = categoryname2
        self.categoryname3 = categoryname3
        self.categoryname4 = categoryname4
        self.colorname = colorname
        self.colorrgb = colorrgb
        self.colortype = colortype
        self.subcondition = subcondition
        self.remarks = remarks
        self.tierqty1 = tierqty1
        self.tierprice1 = tierprice1
        self.tierqty2 = tierqty2
        self.tierprice2 = tierprice2
        self.tierqty3 = tierqty3
        self.tierprice3 = tierprice3
        self.reservedfor = reservedfor
        self.retain = retain
        self.superlotid = superlotid
        self.superlotqty = superlotqty
        self.extdescritpion = extdescription
        self.itemtypename = itemtypename
        self.itemidname = itemidname
        self.dimensionx =  dimensionx
        self.dimensiony = dimensiony
        self.dimensionz = dimensionz
        self.box = box
        self.row = row
        self.column = column





    def check_color(self, colorid, colorname):
        if colorid == '':
            colorid = self.get_category("colorname",
                                        "colorid",
                                        colorname,
                                        "colors")
        return colorid

    def exist_picture(self, itemid, colorid, urlimage):
        filename = "id" + itemid + "color" + str(colorid) + ".jpg"
        if urlimage == filename:
            return urlimage
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
                return str(d[hardy])
        return f"{hardy} Not Available"

    def what_condition(self, condition):
        if condition == "U" or condition == "Used":
            return 'U'
        if condition == "N" or condition == "New":
            return 'N'
        return 'U'

    def refresh_infos(self):
        self.categoryid = self.get_category("Number",
                                            "Category ID",
                                            self.itemid,
                                            "parts")
        w = self.get_category("Number",
                            "weight",
                            self.itemid,
                            "parts").replace('.',',')
        if w == "weight Not Available":
            self.weight = '0'
        else:
            self.weight = w
        self.categorynamefull = self.get_category("Number",
                                            "Category Name",
                                            self.itemid,
                                            "parts")
        self.categoryname1 = self.get_category("Number",
                                            "Category1",
                                            self.itemid,
                                            "parts")
        self.categoryname2 = self.get_category("Number",
                                            "Category2",
                                            self.itemid,
                                            "parts")
        self.categoryname3 = self.get_category("Number",
                                            "Category3",
                                            self.itemid,
                                            "parts")
        self.categoryname4 = self.get_category("Number",
                                            "Category4",
                                            self.itemid,
                                            "parts")
        self.colorname = self.get_category("colorid",
                                            "colorname",
                                            self.colorid,
                                            "colors")
        self.colorrgb = self.get_category("colorid",
                                            "rgb",
                                            self.colorid,
                                            "colors")
        self.colortype = self.get_category("colorid",
                                            "type",
                                            self.colorid,
                                            "colors")
        self.itemtypename = self.get_category("itemtypeid",
                                            "itemtypename",
                                            self.itemtype,
                                            "itemtypes")
        self.itemidname = self.get_category("Number",
                                            "Name",
                                            self.itemid,
                                            "parts")
        self.dimensionx =  self.get_category("Number",
                                            "DimensionX",
                                            self.itemid,
                                            "parts")
        self.dimensiony = self.get_category("Number",
                                            "DimensionY",
                                            self.itemid,
                                            "parts")
        self.dimensionz = self.get_category("Number",
                                            "DimensionZ",
                                            self.itemid,
                                            "parts")
        self.urlimage = self.exist_picture(self.itemid,
                                            self.colorid,
                                            self.urlimage)

    def afficher(self):
        print(f"{self.itemid} : {self.colorid} : {self.qty} : {self.price}€ " +\
                f"dans {self.box} : {self.row}{self.column}")

    def price_total(self):
        a = float(self.price.replace(',','.'))
        b = float(self.qty.replace(',','.'))
        return round(a * b, 2)

    def weight_total(self):
        # en grammes
        a = float(self.weight.replace(',','.'))
        b = float(self.qty.replace(',','.'))
        return round(a * b, 2)

    def sauvegarder_format_csv(self):
        a = str(self.price).replace('.',',')
        b = str(self.qty).replace('.',',')
        c = str(self.weight).replace('.',',')
        content = self.lotid + ";" +\
                self.dateadded + ";" +\
                self.categoryid + ";" +\
                self.colorid  + ";" +\
                a + ";" +\
                b + ";" +\
                self.bulk + ";" +\
                self.urlimage + ";" +\
                self.description + ";" +\
                self.condition + ";" +\
                self.itemtype + ";" +\
                self.itemid + ";" +\
                self.salediscount + ";" +\
                self.stockroom + ";" +\
                c + ";" +\
                self.datelastsold + ";" +\
                self.currency + ";" +\
                self.categorynamefull + ';' +\
                self.categoryname1 + ";" +\
                self.categoryname2 + ";" +\
                self.categoryname3 + ";" +\
                self.categoryname4 + ";" +\
                self.colorname + ";" +\
                '#' + self.colorrgb + ";" +\
                self.colortype + ";" +\
                self.subcondition + ";" +\
                self.remarks + ";" +\
                self.tierqty1 + ";" +\
                self.tierprice1 + ";" +\
                self.tierqty2 + ";" +\
                self.tierprice2 + ";" +\
                self.tierqty3 + ";" +\
                self.tierprice3 + ";" +\
                self.reservedfor + ";" +\
                self.retain + ";" +\
                self.superlotid + ";" +\
                self.superlotqty + ";" +\
                self.extdescritpion + ";" +\
                self.itemtypename + ";" +\
                self.itemidname + ";" +\
                self.dimensionx + ";" +\
                self.dimensiony + ";" +\
                self.dimensionz  + ";" +\
                self.box + ";" +\
                self.row + ";" +\
                self.column + ";" + '\n'
        return content

    def transform_to_upload_blk_xml(self):
        a = self.price.replace(',','.')
        b = self.box + ' ' + self.row + ' ' + self.column
        if b == '  ':
            b=''
        # attention la quantité ne doit pas être nulle
        content = "\t<ITEM>\n"
        required = "\t\t<CATEGORY>" + self.categoryid + "</CATEGORY>\n" +\
                    "\t\t<COLOR>" + self.colorid + "</COLOR>\n" +\
                    "\t\t<PRICE>" + a + "</PRICE>\n" +\
                    "\t\t<QTY>" + self.qty + "</QTY>\n" +\
                    "\t\t<CONDITION>" + self.condition + "</CONDITION>\n" +\
                    "\t\t<ITEMTYPE>" + self.itemtype + "</ITEMTYPE>\n" +\
                    "\t\t<ITEMID>" + self.itemid + "</ITEMID>\n" +\
                    "\t\t<DESCRIPTION>" + b + "</DESCRIPTION>\n"
        not_required = "\t\t<LOTID>" + self.lotid + "</LOTID>\n" +\
                    "\t\t<DATEADDED>" + self.dateadded + "</DATEADDED>\n" +\
                    "\t\t<BULK>" + self.bulk + "</BULK>\n" +\
                    "\t\t<IMAGE>" + self.urlimage + "</IMAGE>\n" +\
                    "\t\t<SALE>" + self.salediscount + "</SALE>\n" +\
                    "\t\t<STOCKROOM>" + self.stockroom + "</STOCKROOM>\n" +\
                    "\t\t<ITEMWEIGHT>" + self.weight + "</ITEMWEIGHT>\n" +\
                    "\t\t<DATELASTSOLD>" + self.datelastsold + "</DATELASTSOLD>\n" +\
                    "\t\t<BASECURRENCYCODE>" + self.currency + "</BASECURRENCYCODE>\n"
        content = content + required #+ not_required
        content = content + "\t</ITEM>\n"
        return content

    def transform_to_impression_html(self, index):
        if self.urlimage != "Not Available":
            path_picture = "../pictures/id" + self.itemid +\
                                                "color" + self.colorid + ".jpg"
        else:
            path_picture = "../pictures/noImage.jpg"
        if (index % 2) == 0:
            pair = "pair"
        else:
            pair = "impair"
        content = '\t\t<div class="' + pair + '">\n' +\
                    '\t\t\t<img src="' + path_picture + '">\n' +\
                    '\t\t\t<p>' + self.itemid + '</p>\n' +\
                    '\t\t\t<p class="itemidname">' + self.itemidname + '</p>\n' +\
                    '\t\t\t<p>' + self.colorid + '</p>\n' +\
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
        else:
            type = 'Part'
        json_obj = api.catalog_item.get_price_guide(type,
                                                    self.itemid,
                                                    int(self.colorid),
                                                    new_or_used= self.condition)
        code = json_obj['meta']['code']
        if code == 401:
            print("Impossible de prendre les prix !!!\n" +\
                    " --- !!! --- Erreur d'Authentification --- !!! --- \n\n\n")
        elif code == 200:
            self.price = (json_obj['data']['avg_price']).replace('.', ',')