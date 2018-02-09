import requests
from bs4 import BeautifulSoup
import codecs
import os

folder = "downloadData"
lidl = folder + "/Lidl.txt"
supervalu = folder + "/SuperValu.txt"
jsonfile = folder + "/json"
tesco = folder + "/TESCO.txt"
dealz = folder + "/DEALZ.txt"

if not os.path.isdir(folder):
    os.mkdir(folder)

# Lidl
print("\n++++++++++++++++++LIDL++++++++++++++++\n")
url="https://www.lidl.ie/en/index.htm"
text_page = requests.get(url).text
with codecs.open(lidl , "w", "utf8") as file:
    file.write(text_page)


soup = BeautifulSoup(text_page, "html.parser")
div_lines = soup.find_all(attrs={"data-creative": "Product Slider"})
count = 0
for line in div_lines:
    count += 1
    print("{:<4} {:<60}{}".format(count, line['data-name'], line['data-price']))

file.close()
    
# SuperValu (only for fruit and vegetables)
print("\n++++++++++++++++++SuperValue++++++++++++++++\n")
url = "https://shop.supervalu.ie/shopping/specialoffers/fruit-vegetables"
text_page = requests.get(url).text
with codecs.open(supervalu , "w", "utf8") as file:
    file.write(text_page)
soup = BeautifulSoup(text_page, "html.parser")
div_lines = soup.find_all('div', attrs={"class": "col-xs-6 col-sm-4 col-md-2-4 ga-impression ga-product"})
count = 0
json_file = open(jsonfile, 'w')
json_file.write("{\n")
for i in range(len(div_lines)):
    json_file.write('\n"' + str(count) + '":\n')
    if i < (len(div_lines)-1):
        json_file.write("\t" + div_lines[i]['data-product'] + ",")
    else:
        json_file.write("\t" + div_lines[i]['data-product'])
    count += 1
    
json_file.write("\n}\n")
json_file.close()
file.close()

import json
json_data = json.load(open(jsonfile))
for i in range(count):
    print("{:<4}{:<60}{}".format(i, json_data[str(i)]['name'], json_data[str(i)]['price']))


'''
# TESCO
url = 'https://www.tesco.com/groceries/en-GB/promotions/alloffers'
text_page = requests.get(url).text
with codecs.open(tesco , "w", "utf8") as file:
    file.write(text_page)
text_page = text_page.replace('&quot;', '\n')
text_page = text_page.replace('<div', '\n<div')
text_page = text_page.replace('/div>', '/div>\n')
print(text_page)
#soup = BeautifulSoup(text_page, "html.parser")
#div_lines = soup.find_all('div', attrs={"class": "col-xs-6 col-sm-4 col-md-2-4 ga-impression ga-product"})
'''

# Dealz
print("\n++++++++++++++++++++ Dealz 1.5 Euro product ++++++++++++++")
products = {
    "Chocolate":  "http://www.dealz.ie/food-and-drink/chocolate",
    "Sweet and Snaks": "http://www.dealz.ie/food-and-drink/sweets-and-snacks",
    "Cakes biscuits and Hot drinks": "http://www.dealz.ie/food-and-drink/cakes-biscuits-and-hot-drinks",
    "Soft drinks" : "http://www.dealz.ie/food-and-drink/soft-drinks" }

item_num = 0
for key, value in products.items():
    item_num += 1
    print(key + ":")
    text_page = requests.get(value).text
    with codecs.open(dealz + "_" + str(item_num), "w", "utf8") as file:
        file.write(text_page)
    soup = BeautifulSoup(text_page, "html.parser")
    div_lines = soup.find_all(attrs={"class": "product-name"})
    count = 0
    for line in div_lines:
        count += 1
        print(count, line.get_text().strip())

file.close()
