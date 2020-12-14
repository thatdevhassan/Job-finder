# scraping data from a wether forcast website.
# date: 14 December

import bs4
import requests
from bs4 import BeautifulSoup


with open('index.html','r') as parsefile:
    soup = BeautifulSoup(parsefile, 'html.parser')

# main    
forecast_list = soup.find('ul', id="seven-day-forecast-list")

for insidelist in forecast_list.find_all('li' ,class_='forecast-tombstone'):
    # print(insidelist.text)
    desc = insidelist.find('p',class_='short-desc')
    temp = insidelist.find('p', class_='temp')
    print("description " ,desc.get_text().strip())
    print("temperatire " ,temp.get_text().strip())
    print("\n")
    


