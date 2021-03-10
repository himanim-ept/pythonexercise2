import csv
from openpyxl import Workbook

wb = Workbook()  #create workbook object
ws = wb.active   #store workbook in worksheet and active it
with open('data.csv', 'r') as f:
     for row in csv.reader(f):
         ws.append(row)  #append row to worksheet
wb.save('name.xls')

#Here is another way to write in .xls file with the use of dictionary
#There are some error Generate in these code
# import xlsxwriter
# import Program6
#
# workbook = xlsxwriter.Workbook('name.xls')
# #worksheet = workbook.add_worksheet()
# wb = workbook.active
#
# csv_columns = ["Order No", "Name", "Address1", "Address2", "City", "Country", "SKU", "Price", "Qty"]
# with open("name.xls", 'w') as destination:
#     Destination_file = wb.write(destination, fieldnames=csv_columns)
#     Destination_file.writeheader()
#
#     for key, values in Program6.csvdictionary.items():
#         Customer = values.get("Customer") #getting value of customer
#         Product = values.get("Product") #getting value from product
#         for i in Product:
#             Destination_file.writerow({"Order No": key,
#                                        "Name": Customer.get('Name'),
#                                        "Address1": Customer.get('address 1'),
#                                        "Address2": Customer.get('address 2'),
#                                        "City": Customer.get('city'),
#                                        "Country": Customer.get('country'),
#                                        "SKU": i.get('sku'),
#                                        "Price": i.get('price'),
#                                        "Qty": i.get('qty')})
#
#
#     print("Succesfully")
# workbook.save('name.xls')

