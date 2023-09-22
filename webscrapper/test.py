import requests
from bs4 import BeautifulSoup
 
# Making a GET request
r = requests.get('https://game8.co/games/Honkai-Star-Rail/archives/404256')
 
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('table', class_='a-table a-table a-table tablesorter')
content = s.find_all('a')

print(content)