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

# Get features
features = page_soup.findAll("ul",{"class":"item-features"})

# Open a CSV file
filename = 'prod.csv'
f = open(filename,"w") 

headers = "brand, product_name, shipping, core_clock, max_res, display_port, DVI, model_no, item_no \n"

f.write(headers)

for (container, feature) in zip(containers[:-1], features):
    brand = container.div.div.a.img["title"]
    product_name = container.findAll("a",{"class":"item-title"})[0].text
    shipping = container.findAll("li",{"class":"price-ship"})[0].text.strip()

    writeup = brand + ", " + product_name.replace(",","|") + ", " + shipping    
    lis = feature.findAll("li")
    for li in lis:
        try:
            rm = li.strong.text
            dt = li.text.replace(rm,"").replace("\n","|").strip()
        except:
            dt = " "
        writeup += ", " + dt 
    
    writeup += "\n"

    f.write(writeup)

f.close()