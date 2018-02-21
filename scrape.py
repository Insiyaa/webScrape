from bs4 import BeautifulSoup as soup # to parse the HTML
from urllib.request import urlopen as uReq # to grab the page

# URL I want to scrap
myurl = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

# Open the url
client = uReq(myurl)

# Store the HTML of the URL
page_html = client.read()

# Close the client
client.close()

# Parse the HTML
page_soup = soup(page_html, "html.parser")

# Grab all the products
containers = page_soup.findAll("div", {"class":"item-container"})

# Open a CSV file
filename = 'prod.csv'
f = open(filename,"w") 

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers[:-1]:
    brand = container.div.div.a.img["title"]
    # print(brand)
    product_name = container.findAll("a",{"class":"item-title"})[0].text
    # print(product_name)
    shipping = container.findAll("li",{"class":"price-ship"})[0].text.strip()
    # print(shipping)
    f.write(brand + ", " + product_name.replace(",","|") + ", " + shipping + "\n")
f.close()