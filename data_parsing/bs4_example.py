import requests
from bs4 import BeautifulSoup

url = 'https://www.cbr.ru'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')


    lst=soup.findAll('div', class_='main-indicator_value')
    # for header in soup.findAll([ 'div']):
    #     print(header.text.strip())
    # print(lst)
    print("Инфляция ноябрь 2024: ")
    print(lst[1].text)


