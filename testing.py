import requests
import bs4
from bs4 import BeautifulSoup
url = 'https://forecast.weather.gov/MapClick.php?lat=38.82253000000003&lon=-77.16239499999995#.X9eewlVKi00'

req = requests.get(url)
print(req.status_code)

soup = BeautifulSoup(req.content, 'html.parser')

data = soup.prettify()
print(data)



newfp = open('index.html','w')
newfp.write(data)
newfp.close()