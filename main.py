# scraping data from a weather forcast website.
# date: 14 December

import bs4
import pprint
import requests
import csv
import time
import pandas as pd
from bs4 import BeautifulSoup


with open('index.html','r') as parsefile:
    soup = BeautifulSoup(parsefile, 'html.parser')

Database = {}

 
forecast_list = soup.find('ul', id="seven-day-forecast-list")

Short_description = []
Temperature = [] 
Day = []
Full_description = []

# looping
for insidelist in forecast_list.find_all('li' ,class_='forecast-tombstone'):


    # instantiating desc and temp
    desc = insidelist.find('p',class_='short-desc').get_text().strip()
    temp = insidelist.find('p', class_='temp').get_text().strip()
    day = insidelist.find('p', class_='period-name').get_text().strip()
    #getting full description from images alt, because it contains
    #  extensive information about the weather 
    fd = insidelist.find('img').get('alt').strip()

    

        
    Short_description.append(desc)
    Temperature.append(temp)
    Day.append(day)
    Full_description.append(fd)

# function for removing "escape char"
def remove_line(target):

    new_Day = []
    for i in target:
        splitting = i.split()
        joining_day = (" ").join(splitting)
        new_Day.append(joining_day)
    return new_Day
real_day= remove_line(Day)
sh_desc = remove_line(Short_description)


Database['Short-description'] = sh_desc  
Database['Temperature'] = Temperature
Database['Day'] = real_day
Database['Full-description'] = Full_description

# pprint.pprint(Database)


with open("data.csv",'w') as fileopen:
    new = csv.writer(fileopen,Database)





