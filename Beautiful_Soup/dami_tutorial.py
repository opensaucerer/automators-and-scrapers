import requests as r
from bs4 import BeautifulSoup as bs


url = "https://www.jumia.com.ng/nokia-x5-5.86-4g-android-8.1-fingerprint-3gb-ram-32gb-rom-octa-core-smartphone-blue-nokia-mpg1196784.html"

res = r.get(url)

response = res.content

# print(response)

pepper = bs(response, "html.parser")

# print(soup.prettify())


price = pepper.find_all("span", class_="-b -ltr -tal -fs24")


product_price = price[0]
product_price = product_price.text

product_price = product_price.strip('₦')
product_price = product_price.strip(' ')
product_price = product_price.split(',')

product_price = int(product_price[0] + product_price[1])


if product_price > 45000:
    f = open('dami.txt', "a")
    f.write("Too Expensive don't by\n")
    f.write(f'price is currently at {product_price}\n')

else:

    f = open('dami.txt', "a")
    f.write("product is now cheap")
    f.write(f'price is currently at {product_price}')
