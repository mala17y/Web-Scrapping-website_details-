import pandas as pd
import requests
from bs4 import BeautifulSoup

p_name =[]
p_price=[]
p_reviews = []

url = "https://www.sheglam.com/collections/skin-care"

req = requests.get(url)

bs = BeautifulSoup(req.content , "html.parser")




pn = bs.find_all("div" , class_ = "boost-pfs-filter-product-bottom-inner notranslate")
for i in pn:
    name= i.text.strip()
    p_name.append(name)

print (len(p_name))

pr = bs.find_all("p" , class_ = "boost-pfs-filter-product-item-price")
for i in pr:
    name = i.text.strip()
    p_price.append(name)

print (len(p_price))



#print(len(p_name), len(p_price), len(p_reviews))
df = pd.DataFrame({"product names":p_name , "product prices ": p_price })
#print(df)

df.to_csv(r"C:\Users\lenevo\OneDrive\Desktop\hiskytech IT\task 1.csv")





