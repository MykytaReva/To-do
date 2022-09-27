import requests
from bs4 import BeautifulSoup
import os
url = requests.get('https://www.universalbank.com.ua/')
a = os.environ
soup = BeautifulSoup(url.content, 'html.parser')

al = soup.find_all('td')
n = len(al)

rate_list = []
rate_dict = {}

for i in range(n):
    rate = soup.find_all('td')[i].get_text()
    rate_list.append(rate.replace(' ', '').replace('\n', ''))

for US in rate_list:
    if US == 'USD':
        rate_dict[US] = {'Buy': rate_list[rate_list.index(US) + 1], 'Sale': rate_list[rate_list.index(US) + 2]}
    elif US == 'EUR':
        rate_dict[US] = {'Buy': rate_list[rate_list.index(US) + 1], 'Sale': rate_list[rate_list.index(US) + 2]}

print(rate_dict)
print('-----------------')
print(a)
