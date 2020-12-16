# scraping data from a wether forcast website.
# date: 14 December

import bs4
import requests
import csv
from bs4 import BeautifulSoup


with open('index.html','r') as parsefile:
    soup = BeautifulSoup(parsefile, 'html.parser')

# main    
forecast_list = soup.find('ul', id="seven-day-forecast-list")

for insidelist in forecast_list.find_all('li' ,class_='forecast-tombstone'):
    # print(insidelist.text)
    # instantiating desc and temp
    desc = insidelist.find('p',class_='short-desc')
    temp = insidelist.find('p', class_='temp')
    day = insidelist.find('p', class_='period-name')
    #getting full description
    fd = insidelist.find('img').get('alt')
    print(fd)

    # # this will return the temperature and description
    # print("description " ,desc.get_text().strip())
    # print("temperatire " ,temp.get_text().strip())
    # print('day', day.get_text().strip())
    # print("\n")
    # print(full_discription) 
    print('\n')   


