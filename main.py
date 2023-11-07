import requests
from bs4 import BeautifulSoup

HEADERS = {'Accept-Language': 'en-US, en;q=0.5'}


URL_snapdeal = input("Enter link for Snapdeal: ")
URL_flipkart = input("Enter link for Flipkart: ")

print("\n\n\nSearching on Snapdeal...\n")

webpage_snapdeal = requests.get(URL_snapdeal, headers=HEADERS)

html_text_snapdeal = webpage_snapdeal.text

soup_snapdeal = BeautifulSoup(html_text_snapdeal, 'html.parser')

products_snapdeal = soup_snapdeal.find_all('div', class_="product-tuple-listing")

productsSnapdeal = {}

for productSnapdeal in products_snapdeal:
    product_details_snapdeal = productSnapdeal.find('div', class_="product-tuple-description")
    product_name_snapdeal = product_details_snapdeal.find('p', class_="product-title").text.split(" (")[0]
    product_price_snapdeal = int(product_details_snapdeal.find('span', class_="lfloat product-price").text.split()[-1].replace(",", ""))
    productsSnapdeal[product_name_snapdeal] = product_price_snapdeal

sorted_products_snapdeal = dict(sorted(productsSnapdeal.items(), key=lambda item: item[1]))

max_key_length = max(len(key) for key in sorted_products_snapdeal)

for key, value in sorted_products_snapdeal.items():
    print(f"{key:<{max_key_length}} : {value}")




print("\n\n\nSearching on Flipkart...\n")

webpage_flipkart = requests.get(URL_flipkart, headers=HEADERS)

html_text_flipkart = webpage_flipkart.text

soup_flipkart = BeautifulSoup(html_text_flipkart, 'html.parser')

products_flipkart = soup_flipkart.find_all('div', class_="_1xHGtK _373qXS")

productsFlipkart = {}

for productFlipkart in products_flipkart:
    product_name_flipkart = productFlipkart.find('a', class_="IRpwTa").text
    product_price_flipkart = int(productFlipkart.find('div', class_="_30jeq3").text[1:].replace(",",""))
    productsFlipkart[product_name_flipkart] = product_price_flipkart

sorted_products_flipkart = dict(sorted(productsFlipkart.items(), key=lambda item: item[1]))

max_key_length = max(len(key) for key in sorted_products_flipkart)

for key, value in sorted_products_flipkart.items():
    print(f"{key:<{max_key_length}} : {value}")


# https://www.snapdeal.com/products/mens-footwear?sort=plrty
# https://www.flipkart.com/footwear/pr?sid=osp