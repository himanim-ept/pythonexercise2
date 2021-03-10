#Write a program which is having a class InventoryManagement.
#System should manage the quantity of purchase and sales processes.
#Users should be able to purchase the product with different prices in the same object of Inventory Management -
# Use a dictionary, maintain a numerical index and store product price and product quantity against it.
#Whenever the product is sold, it will start deducting the product qty whichever entry is done first in the dictionary,
# so qty will be deducted as FIFO (First In First Out).
#Whenever product qty is deducted change the price of that index.
#Formula -
#Once the qty from each purchase is used make sure, it is not used again, so update the dictionary accordingly.
#Program should be able to handle the valuation.
#Formula for valuation - sum of price * qty / sum of total qty.
#Write appropriate constructor, methods to manage the sales and purchase processes.
# There should be a provision to view the available quantities.
# This should be a menu driven program, which allows to
# Purchase Product
# Sale Product
# View Available Product Quantities
# Exit
# Whenever sales take place, the system should process the quantities and then should show the available quantities.

class InventoryManagement:
    #class constructor
    def __init__(self):

        self.Product = {}

    def purchase(self,qty,unit_price):
        # returns nothing
        list1 = list(self.Product)
        index = len(list1) + 1
        self.Product[index] = {'qty': qty, 'unit_price': unit_price, 'sub_total': (qty * unit_price)}
        print((self.Product))

    def total_qty_stock(self):
        # to count total qty in stock
        total_stock = 0
        for key1, value1 in self.Product.items():
            total_stock += value1['qty']
        # print(self.main_dictionary)
        return total_stock
    def total_stock(self):
        #print remaining dictionry
            print(self.Product)

    def total_price(self):
        #to calculate the sum of all unit_price
        total_price = 0
        for key1,value1 in self.Product.items():
            total_price +=value1['sub_total']

    def sale(self,sale_qty):
        #returns nothing
        # for loop  checks if sales qty equals to 1st dict qty then pop
        total_stock = self.total_qty_stock()
        if sale_qty>total_stock:
            # First check total_stock less then sale_qty ?yes print error message
            print("Does not have enough stock for sale")
            return

        for key,value in self.Product.items():
            # for loop  checks if sales qty equals to 1st dict qty then pop
            if sale_qty == value['qty']:
                self.Product.pop(key)
                return
            elif sale_qty < value['qty']:
                # Another if condition to check if sales qty is less then 1st dict then reduce the qty and subtotal
                value['qty'] -= sale_qty
                value['sub_total'] = value['sub_total'] - (sale_qty * value['unit_price'])
                return
            elif sale_qty > value['qty']:
                # Last if condition to check if sales qty is greater pop the 1st dict then call sales with remaining qty
                remain_qty=sale_qty-value['qty']
                self.Product.pop(key)
                self.sale(remain_qty)
                return

        def valuation(self):
            #average Valuation
            # Formula for valuation - sum of price * qty / sum of total qty.
            valuation = self.total_price * sale_qty/self.total_qty_stock
            print("valuation : ",valuation)

Invmangobj = InventoryManagement() # object for class

ch = 0
while ch<4:
    print("[1] press 1 for purchase the product :")
    print("[2] press 2 for sale Product :")
    print("[3] press 3 for view Available Product Quantity :")
    print("[4] press 4 for exit :")
    ch = int(input("select Number for continue :"))

    if ch == 1:
        qty = int(input("Enter Qty :"))
        unit_price = int(input("Enter unit price :"))
        Invmangobj.purchase(qty,unit_price)
    elif ch == 2:
        sale_qty = int(input("Enter Qty you want to sale :"))
        Invmangobj.sale(sale_qty)
    elif ch == 3:
        Invmangobj.total_stock()
    else:
        ("Exit")



#def total_qty_stock(self):
#print((self.Product))
