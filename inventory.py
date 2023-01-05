import requests
from bs4 import BeautifulSoup as bs

url = 'https://mayerboch.com/articles/types-of-pans-by-purpose/'

response = requests.get(url)

soup = bs(response.text, 'lxml')

title = soup.title
print(title.text.upper())
print()

inventory = soup.find_all('h2')

for item in inventory:
    print(item.text)