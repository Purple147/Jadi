# Regex in web -> API -> requetst -> inspector element -> beautiful soup library in python 
# by inspector element we can change web, using regex to find what we want in a web is hard so we use beautiful soup library
# bs4, beautifulsoup, text, find("X"), x.attrs
import requests
from bs4 import BeautifulSoup

url = "https://bama.ir/car/all-brands/all-models/all-trims?price=30-40"
res = requests.get(url)
Text = res.text()
soup = BeautifulSoup(Text, "html.parser")
print(soup)
res = soup.find("h2")
print(res)
res2 = soup.find_all("h2")
print(res2)
res3 = res2[1]
print(res3)
print(res3.attrs)
