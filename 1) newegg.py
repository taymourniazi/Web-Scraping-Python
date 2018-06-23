import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
uClient= uReq(myurl) # open webpage, download content
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser") # html parsing
page_soup.h1
#grabs each product information
containers = page_soup.findAll("div",{"class":"item-container"})
contain = containers[0]
container = containers[0]

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()


	print("brand:  " + brand)
	print("product_name:  " + product_name)
	print("shipping:  " + shipping)

	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
f.close()