import requests
from bs4 import BeautifulSoup

page = requests.get('https://paramsaluja.ml/')
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('h1').string)
ll = soup.find_all('li')

for item in ll:
    if item.string:
        print(item.string)