import requests
from bs4 import BeautifulSoup

res = requests.get("https://mihaaru.com/").text
soup = BeautifulSoup(res, 'lxml')

details = soup.find_all('div', class_="coronavirus-special-coverage-item")[1].find_all('li')
for detail in details:
    name = detail.find('span', class_='clabel').text
    number = detail.find('span', class_='number').text
    print(name, number)
