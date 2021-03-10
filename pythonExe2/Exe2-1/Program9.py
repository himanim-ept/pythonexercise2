import datetime


class Product:
    def __init__(self):
        self.products = {"PRD1": {"Product Name": "Pencil",
                                  "Product Qty": 100,
                                  "Product Type": "Stackable",
                                  "Product Unit Price": 10,
                                  "Product cost": 20},
                         "PRD2": {"Product Name": "Pen",
                                  "Product Qty": 100,
                                  "Product Type": "Consumable",
                                  "Product Unit Price": 20,
                                  "Product cost": 20}}
        # Dictionary "products" will contain:
        # product_name
        # product_unit_price
        # product_cost
        # product_type
        # product_qty
        # sku
        self.sku = 0

    def create_product(self):
        # creates a product and calls "prepare_product" method
        # argument - 0
        # return - 0
        print(self.prepare_product())

    def prepare_product(self):
        # collects all the details of products and inserts in "products" dictionary
        # argument - 0
        # returns the uniquely generated sku to the "create_product" method
        product_name = input("Enter the name of the product : ")
        product_type = input("Enter the type of product from below 3 :\nstackable or service or consumable\n")
        product_qty = int(input("Enter the qty of product :"))
        product_unit_price = int(input("Enter the product_unit_price :"))
        product_cost = int(input("Enter the product cost :"))
        # if dictionary not empty then inserts next value
        # if empty then else condition is implemented and first value is inserted in dictionary
        if len(self.products) > 0:
            l = list(self.products.keys())
            # unique sku no. are generated. eg : PRD1, PRD2, PRD3, .... etc.
            for key in l:
                no = str(int(key.split("PRD")[-1]) + 1)
                sku = "PRD" + no
            self.products.update({sku: {"Product Name": product_name, "Product Type": product_type,
                                                "Product Unit Price": product_unit_price,
                                                "Product cost": product_cost,
                                                "Product Qty": product_qty}})
            return sku
        else:
            sku = "PRD1"
            self.products.update({sku: {"Product Name": product_name, "Product Type": product_type,
                                                "Product Unit Price": product_unit_price,
                                                "Product cost": product_cost, "Product Qty": product_qty}})
            return sku

    def display_product_details(self):
        # displays product details
        # argument - 0
        # return - 0
        print(self.products)

    def stock_update(self):
        # for qty increment of specific product ( using sku )
        sku = input("Enter the sku of product : ")
        qty = int(input("Enter the qty of product : "))
        if sku in self.products.keys():
            product_qty = self.products[sku].get("Product Qty")
            self.products[sku].update({"Product Qty": qty + product_qty})
        self.display_product_details()


class Customer:
    def __init__(self):
        self.customers = {"Cust_1": {"Name": "Him",
                                     "Email": "him@gmail.com",
                                     "Phone No": "9776514032"}}
        # dictionary "customers" contains:
        # customer_name
        # customer_email
        # customer_phone
        self.customer_details = {"Cust_1": {"Address1": "abc",
                                            "Address2": "pqr",
                                            "City": "rajkot",
                                            "State": "gujarat",
                                            "Country": "india",
                                            "Zipcode": "587461"}}
        # dictionary "customer_details" contains:
        # customer_address1
        # customer_address2,
        # customer_city
        # customer_zipcode
        # customer_state
        # customer_country

    def create_customer(self):
        # creates a customer and calls "prepare_customer" method
        # argument - 0
        # return - 0
        print(self.prepare_customer())

    def prepare_customer(self):
        # collects all details of products and inserts in respective two dictionaries
        customer_name = input("Enter customer's name :")
        customer_email = input("Enter customer's email :")
        customer_phone = input("Enter customer's phone :")
        customer_address1 = input("Enter customer's address 1 :")
        customer_address2 = input("Enter customer's address 2 :")
        customer_city = input("Enter customer's city :")
        customer_state = input("Enter customer's state :")
        customer_country = input("Enter customer's country :")
        customer_zipcode = input("Enter customer's zipcode :")
        # if dictionary not empty then inserts next value
        # if empty then else condition is implemented and first value is inserted in dictionary
        if len(self.customers) > 0:
            l = list(self.customers.keys())
            # unique customer no. is generated. eg : cust_1, cust_2, cust_3, .... etc.
            for key in l:
                no = str(int(key.split("Cust_")[-1]) + 1)
                customer_no = "Cust_" + no
            self.customers.update({customer_no: {"Name": customer_name, "Email":
                                                      customer_email, "Phone No": customer_phone}})
            self.customer_details.update({customer_no: {"Address1": customer_address1, "Address2":
                                                              customer_address2, "City": customer_city,
                                                              "State": customer_state, "Country":
                                                              customer_country, "Zipcode": customer_zipcode}})
            return customer_no
        else:
            customer_no = "Cust_1"
            self.customers.update({customer_no: {"Name": customer_name, "Email":
                                                      customer_email, "Phone No": customer_phone}})
            self.customer_details.update({customer_no: {"Address1": customer_address1, "Address2":
                                                             customer_address2, "City": customer_city,
                                                             "State": customer_state, "Country":
                                                             customer_country, "Zipcode": customer_zipcode}})
            return customer_no

    def display_customers_details(self):
        # displays customer's details
        # argument - 0
        # return - 0
        print(self.customers)
        print(self.customer_details)


class SalesOrder(Product, Customer):
    # this class inherits "Product" and "Customer" classes
    # so, there init methods are also inherited and written so, they don't get overwritten
    def __init__(self):
        Product.__init__(self)
        Customer.__init__(self)
        self.sales_order = {}

    def create_sales_order(self):
        # creates sales order and calls "prepare_sales_order" method
        # argument - 0
        # returns - 0
        self.prepare_sales_order()

    def prepare_sales_order(self):
        if len(self.sales_order) > 0:
            l = list(self.sales_order.keys())
            cust_code = self.display_customers()
            sales_order_lines, total = self.display_products()
            for key in l:
                no = str(int(key.split("SO")[-1]) + 1)
                sales_order_no = "SO" + no
            self.sales_order.update({sales_order_no: {"Customer Code": cust_code,
                                                     "Order Date": datetime.datetime.now().strftime("%d %B %Y"),
                                                      "Products": sales_order_lines,
                                                      "Total": total,
                                                      "State": "Draft"}})
        else:
            sales_order_no = "SO1"
            cust_code = self.display_customers()
            sales_order_lines, total = self.display_products()
            self.sales_order.update({sales_order_no: {"Customer Code": cust_code,
                                                      "Order Date": datetime.datetime.now().strftime("%d %B %Y"),
                                                      "Products": sales_order_lines,
                                                      "Total": total,
                                                      "State": "Draft"}})

    def display_customers(self):
        for key, value in self.customers.items():
            l = list(self.customers.keys())
            choice = input("Enter one particular customer code : ")
            for key in l:
                if choice == key:
                    return choice

            print("Invalid Choice")
            return

    def display_products(self):
        product_list = []
        for key, value in self.products.items():
            print(key, self.products[key].get("Product Name"), self.products[key].get("Product Qty"),
                  self.products[key].get("Product cost"))

        return self.order_lines(product_list)

    def order_lines(self, product_list):
        product_code_list = []
        while True:
            list_of_product_keys = list(self.products.keys())
            print("\n1 - Add products\n2 - exit\n")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                product_code = input("Enter one particular product code : ")
                qty = int(input("Enter qty of product: "))
                if product_code not in product_code_list:
                    product_code_list.append(product_code)
                    product_list.append({"SKU": product_code,
                                         "Product Name": self.products[product_code]["Product Name"],
                                         "Product Qty": qty,
                                         "Product cost": self.products[product_code]["Product cost"],
                                         "Product Subtotal": qty*int(self.products[product_code]["Product Unit Price"])})

                else:
                    index = 0
                    for same_product in product_list:
                        if product_list[index]["SKU"] == product_code:
                            qty += int(product_list[index]["Product Qty"])
                            # self.products[product_code]["Product Qty"] -= qty
                            product_list[index].update({"Product Qty": qty,
                                                        "Product Subtotal": qty*int(self.products[product_code]["Product Unit Price"])})
                            break
                        index += 1
            if choice == 2:
                total = self.calculate_total(product_list)
                return product_list, total

    def calculate_total(self, product_list):
        total = 0
        for item in product_list:
            print(item)
            total += int(item["Product Subtotal"])
        return total

    def display_sales_order(self):
        print(self.sales_order)

    def change_product_state(self):
        print("The following states of order are available :"
              "\n1 - draft"
              "\n2 - cancel"
              "\n3 - confirm"
              "\n4 - done")

        sales_no = input("\nEnter the sales order no. : ")
        sales_order_keys = list(self.sales_order)

        if sales_no in sales_order_keys:
            for key in sales_order_keys:
                print(self.sales_order[key].get("State"))
                if self.sales_order[key].get("State") == "Draft":
                    print("Your current state is:", self.sales_order[key].get("State"))
                    print("This state can only change to :\n1 - confirm\n2 - cancel")
                    state = input("Enter the state you chose : ")
                    self.sales_order[key].update({"State": state})

                elif self.sales_order[key].get("State") == "Confirm":
                    print("Your current state is:", self.sales_order[key].get("State"))
                    print("This state can only change to :\n1 - Done\n2 - cancel")
                    state = input("Enter the state you chose : ")
                    self.sales_order[key].update({"State": state})

                elif self.sales_order[key].get("State") == "Cancel":
                    print("Your current state is:", self.sales_order[key].get("State"))
                    print("This state can only change to :\n1 - draft")
                    state = input("Enter the state you chose : ")
                    self.sales_order[key].update({"State": state})
                    print("Your current state is:", self.sales_order[key].get("State"))

                elif self.sales_order[key].get("State") == "Done":
                    print("From done you can't change to any state")
                    state = input("Enter the state you chose : ")
                    self.sales_order[key].update({"State": state})


# object of "SalesOrder" class
s = SalesOrder()

# a menu is provided to user as to select the operation to be implemented
while True:
    print("\n1 - Create Product"
          "\n2 - Update Stock\n"
          "3 - Display Products"
          "\n4 - Create Customer\n"
          "5 - Display Customer"
          "\n6 - Create SalesOrder"
          "\n7 - Display SalesOrder\n"
          "8 - Change Product State\n"
          "9 - exit()\n")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        s.create_product()
    if choice == 2:
        s.stock_update()
    if choice == 3:
        s.display_product_details()
    if choice == 4:
        s.create_customer()
    if choice == 5:
        s.display_customers_details()
    if choice == 6:
        s.create_sales_order()
    if choice == 7:
        s.display_sales_order()
    if choice == 8:
        s.change_product_state()
    if choice == 9:
        exit()