import requests
import bs4
from bs4 import BeautifulSoup

# URL
serverUrl = "https://forecast.weather.gov/MapClick.php?lat=38.82253000000003&lon=-77.16239499999995#.X88S0FVKi00"

response  = requests.get(serverUrl)
print(response)

soup = BeautifulSoup(response.content,'html.parser')

# functions that can be used
# soup.select("div p") --- for css selectors . find all div inside p
# soup.find_all(id= , class=, 'tag' )
#soup.find() 
#soup.find_all().get_text() for getting text.

# getting the forcast for next seven days.
# seven = soup.find(id='seven-day-forcast')

# day = seven.find_all(class_="tombstone-container")
# print(soup.prettify(day[0]))

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())


print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

# print(day.get_text())