import csv
import Program6

#header name
csv_columns = ["Order No", "Name", "Address1", "Address2", "City", "Country", "SKU", "Price", "Qty"]
#open file in writing mode
with open("dict.csv", 'w') as destination:
    Destination_file = csv.DictWriter(destination, fieldnames=csv_columns)
    Destination_file.writeheader()
    #itreate key and value of dictionary
    for key, values in Program6.csvdictionary.items():
        Customer = values.get("Customer") #getting value of customer
        Product = values.get("Product") #getting value from product
        for i in Product:
            Destination_file.writerow({"Order No": key,
                                       "Name": Customer.get('Name'),
                                       "Address1": Customer.get('address 1'),
                                       "Address2": Customer.get('address 2'),
                                       "City": Customer.get('city'),
                                       "Country": Customer.get('country'),
                                       "SKU": i.get('sku'),
                                       "Price": i.get('price'),
                                       "Qty": i.get('qty')})


    print("Succesfully")

# second method of program when we don't want to work with dictionary
#open source file in reading mode
#with open('data.csv', 'r') as source:
    #read the file and store it in source_file
    #source_file = csv.reader(source)
    #open destination file in writing mode
    #with open('dict.csv', 'w') as destination:
     #   destination_file = csv.writer(destination)
      #  for data in source_file: #iterate the data from source file
       #     destination_file.writerow(data)#write data in destination from source
    #destination.close()
#source.close()


#with open('dict.csv', 'w') as csv_file:
 #   writer = csv.writer(csv_file)
 #   for key, value in mydict.items():
  #     writer.writerow([key, value])