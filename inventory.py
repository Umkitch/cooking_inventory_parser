import requests
from bs4 import BeautifulSoup as bs

url = 'https://mayerboch.com/articles/types-of-pans-by-purpose/'

response = requests.get(url)

soup = bs(response.text, 'lxml')

inventory = soup.find_all('h2')

for item in inventory:
    print(item.text)