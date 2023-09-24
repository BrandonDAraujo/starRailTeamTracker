import requests
import csv
from bs4 import BeautifulSoup

def getWebPage(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    return soup

def getAllPlayableCharacterTableLinks(soup):
    body = soup.find('body')
    col3 = body.find('div', class_= "l-3col")
    centerCol3 = col3.find('div', class_= "l-3colMain")
    mainCenterCol3 = centerCol3.find('div', class_= "l-3colMain__center l-3colMain__center--shadow")
    archiveStyleWrapper = mainCenterCol3.find('div', class_ = "archive-style-wrapper")
    tables = archiveStyleWrapper.find_all('table', class_= "a-table a-table a-table tablesorter")
    a = tables[1].find_all('a')
    return a

def writeCharacterData(urls):
    return null
 
# main page that we get the character list from
url = 'https://game8.co/games/Honkai-Star-Rail/archives/404256'
soup = getWebPage(url)
# targets the main table in the url that contains the playable character list
tableLinks = getAllPlayableCharacterTableLinks(soup)
count = 0
urls = []
with open('webscrapper/character.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for line in tableLinks :
        if count % 4 == 0:
            img_data = requests.get(line.next.attrs["data-src"]).content
            with open('webscrapper/images/'+line.text.strip(' ')+'.png', 'wb') as handler:
                handler.write(img_data)
            writer.writerow([line.text, line.attrs["href"]])
            urls.append(line.attrs["href"])
        count += 1
# soup = getWebPage(urls[1])
# print(soup)