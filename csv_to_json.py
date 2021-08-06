import csv
import json

csvfile = open("data/products.csv", "r")
jsonfile = open("data/products.json", "w")

json_data = []

fieldnames = ("Product Name", "Description", "Price")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json_data.append(row)

json.dump(json_data, jsonfile)
