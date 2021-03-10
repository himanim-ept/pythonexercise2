#Write a program which is having a class InventoryManagement.
#System should manage the quantity of purchase and sales processes.
#If the system is not having enough quantity during sales, the system should show a warning message “Not enough product quantities to sell”.
#Write appropriate constructor, methods to manage the sales and purchase processes.
#There should be a provision to view the available quantities.
#This should be a menu driven program, which allows to
#Purchase Product
#Sale Product
#View Available Product Quantities
#Exit
#Whenever sales take place, the system should process the quantities and then should show the available quantities.
class InventoryManagement:
    #class constructor
    def __init__(self,purchase_qty):
        #manage qty for purchase
        self.purchase_qty = purchase_qty

    def printatt(self):
        print("no. of purchase Quantity :",self.purchase_qty)

    def purchase_product_fun(self):
        #no parameter
        #return null
        purchase_product = int(input("enter the no. of product you want to purchase"))
        self.purchase_qty += purchase_product

    def sale_product_fun(self):
        #no parameter
        #return null
        sale_product = (int(input("enter the no. of sale product")))
        if self.purchase_qty >= sale_product:
            self.purchase_qty -=sale_product
        else:
            print("Not enough product quantities to sell")

    def available_quantities(self):
        #no parameter
        #return null
        print("Available Quantity of the product :",self.purchase_qty)

Invmangobj = InventoryManagement(0) # object for class

ch = 0
while ch<4:
    print("[1] press 1 for purchase the product :")
    print("[2] press 2 for sale Product :")
    print("[3] press 3 for view Available Product Quantity :")
    print("[4] press 4 for exit :")
    ch = int(input("select Number for continue :"))

    if ch == 1:
        Invmangobj.purchase_product_fun()
    elif ch == 2:
        Invmangobj.sale_product_fun()
    elif ch == 3:
        Invmangobj.available_quantities()
    else:
        ("Exit")