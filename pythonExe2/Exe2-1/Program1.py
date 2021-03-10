#Write a program that contains ‘manufacturing’ class which allows product manufacturing.
#It purchases raw material from the market and produces a product.
#One should manage the raw material product to produce the actual product.
#One should manage the ratio of raw material to produce the actual product.
#Example - 2 wheels(raw material) are required to produce 1 bicycle(actual product)
#Take input from user raw material, raw material ratio qty, actual product
#While producing the actual product, if the system doesn’t have enough of its stock of raw material, it should show a warning message as “Not enough raw material available to produce the product, please do the purchase”.
#Program should be menu driven allowing to
#Purchase Raw Material Product
#Manufacture Actual Product
#Show Raw Material Quantity
#Show Actual Product Quantity
#Exit
#Following attributes and method function should be part of the class
#Appropriate constructor to set the values for raw material product, actual product, raw material ratio qty value, raw material qty
#produce() - taking no qty to be produced for actual product as argument
#display_raw_material_stock()
#display_final_product_stock()
#purchase_raw_material() - taking no of qty of raw material to be purchased


class Manufacturing:
    #class constructor
    def __init__(self,rawmatrial_qty,actual_Product):
        #parameters
        Initial_ratio = 2
        self.ratio = Initial_ratio #maintain ratio of raw material
        self.rawmatrial_qty = rawmatrial_qty #maintain qty of raw material
        self.actual_Product = actual_Product# maintain qty of actual product

    def printManuf(self):
        print("ratio:",self.ratio)
        print("RawMaterial Qty :",self.rawmatrial_qty)
        print("Actual Product :",self.actual_Product)

        #purchase material for product
    def purchase_raw_material(self):
        #No parameter passed
        #return nothing
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

        #Display the stock of material
    def display_raw_material_stock(self):
        print("Display Available raw material:",self.rawmatrial_qty)
        #display the produce product
    def display_final_product_stock(self):
        print("Display final stock of product:",self.actual_Product)
Manuobject = Manufacturing(0,0)#create object for class and pass the value

ch = 0
while ch<5:
    print("[1] press 1 for purchase the raw material for product :")
    print("[2] press 2 for Manufacture Actual Product :")
    print("[3] press 3 for Show Raw Material Quantity :")
    print("[4] press 4 for Show Actual Product Quantity :")
    print("[5] press 5 for Exist")
    ch = int(input("select Number for continue :"))
    if ch == 1:
        Manuobject.purchase_raw_material()
    elif ch == 2:
         Manuobject.produce()
    elif ch == 3:
         Manuobject.display_raw_material_stock()
    elif ch == 4:
        Manuobject.display_final_product_stock()
    else:
        print("Exit")










