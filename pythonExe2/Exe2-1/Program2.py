#Write a program which extends Program - 1
#Add appropriate class and perform inheritance
#Add the facility of scrapping the raw material product and actual product
#Add appropriate option in the menu for
#scrapping the raw material product
#scrapping the actual product
#Add appropriate methods to scrap the raw material product and actual

class Manufacturing:
    #class constructor
    def __init__(self,rawmatrial_qty,actual_Product,ratio):
        #parameters
        self.ratio = ratio #maintain ratio of raw material
        self.rawmatrial_qty = rawmatrial_qty #maintain qty of raw material
        self.actual_Product = actual_Product # maintain qty of actual product

        # purchase material for product
    def purchase_raw_material(self):
        # No parameter passed
        # return nothing
        self.purchse_raw_material_qty = int(input("Enter the no. of raw material you want to purchase:"))
        self.rawmatrial_qty += self.purchse_raw_material_qty

        # for produvction of raw material
    def produce(self):
        self.qty_produce = int(input("Enter the no. of product you want to produce:"))
        if self.rawmatrial_qty >= self.ratio*self.qty_produce:
            self.rawmatrial_qty -=self.ratio*self.qty_produce
            self.actual_Product +=self.qty_produce
            # row materinal minus
            # calculate actaulproduct
        else:
            print("Not enough raw material available to produce the product, please do the purchase")

        # Display the stock of material
    def display_raw_material_stock(self):
        print("Display Available raw material:",self.rawmatrial_qty)

        # display the produce product
    def display_final_product_stock(self):
        print("Display final stock of product:",self.actual_Product)

#inherite from manufacturing
class Manufatureextend(Manufacturing):
        #class constructor
    def __init__(self,rawmatrial_qty,actual_Product,ratio):
        Manufacturing.__init__(self,rawmatrial_qty,actual_Product,ratio)

    def Scrap_raw_material(self):
        rawmaterial_to_be_scrapped = int(input("Enter the no. of material to be scrapped "))
        self.rawmatrial_qty -= rawmaterial_to_be_scrapped

    def Scrap_actual_material(self):
        actualproduct_to_be_scrapped = int(input("Enter the no. of material to be scrapped"))
        self.actual_Product -= actualproduct_to_be_scrapped

manuobj = Manufatureextend(0,0,0) #create subclass obj and pass the value


ch = 0
while ch<6:
    print("[1] press 1 for purchase the raw material for product :")
    print("[2] press 2 for Manufacture Actual Product :")
    print("[3] press 3 for Show Raw Material Quantity :")
    print("[4] press 4 for Show Actual Product Quantity :")
    print("[5] press 5 for Scrapping")
    print("[6] press 6 for Exist")
    ch = int(input("select Number for continue :"))
    if ch == 1:
        manuobj.purchase_raw_material()
    elif ch == 2:
         manuobj.produce()
    elif ch == 3:
         manuobj.display_raw_material_stock()
    elif ch == 4:
        manuobj.display_final_product_stock()
    elif ch ==5:
        print("[1] press 1 for scrap raw material:")
        print("[2] press 2 for scrap actual product:")
        select = int(input("Select your choice:"))
        if select == 1:
            manuobj.Scrap_raw_material()
        elif select ==2:
            manuobj.display_Scrap_actual_stock()
    else:
        print("Exit")
