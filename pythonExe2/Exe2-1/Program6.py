#Create a program that read a .csv file and print its data in dictionary
#Data is about Sales Order
#The dictionary should have SO number as key and its values as dictionaries
#{SO001 :
#{‘customer’ : {‘name’:<customer name>,‘address 1’ : <value of address1>,’address 2’: <value of address 2>, ‘city’ :<city>, ‘country’: <country>},
#’Products’:[ {‘sku’:<sku>,’price’:<price>,’qty’:<qty>},
#{‘sku’:<sku>,’price’:<price>}]}}

import csv
#empty dictionary for further use
csvdictionary = {}
country_code = {
                    "USA": "America",
                    "UK": "United Kingdom",
                    "DE": "Germany",
                    "AU": "Australia",
                    "IT": "Italy",
                    "ES": "Spain"

}

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "Order No":
            continue
        if row[0] not in csvdictionary.keys():
            csvdictionary.update({row[0]: {"Customer": {
                                                "Name": row[1],
                                                "address 1": row[5],
                                                "address 2": row[6],
                                                "city": row[8],
                                                "country": country_code.get(row[9])},
                                            "Product": [{"sku": row[2],
                                                  "price": row[4],
                                                  "qty": row[3]
                                                  }]
                                }
                                })


        else:
            csvdictionary[row[0]].get("Product").append({"sku": row[2],
                                                "price": row[4],
                                                "qty": row[3]
                                                })

print(csvdictionary)

