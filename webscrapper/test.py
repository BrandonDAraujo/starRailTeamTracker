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

def saveCharacterImages(characterLinks):
    for link in characterLinks:
        img_data = requests.get(link.next.attrs["data-src"]).content
        with open('webscrapper/images/'+link.text.strip(' ')+'.png', 'wb') as handler:
            handler.write(img_data)
    return 
 
def writeCsvHeader():
    with open('webscrapper/character.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'URL'])
    return

def writeNamesAndUrls(characterLinks):
    with open('webscrapper/character.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for link in characterLinks:
            writer.writerow([link.text, link.attrs["href"]])
    return

# main page that we get the character list from
url = 'https://game8.co/games/Honkai-Star-Rail/archives/404256'
soup = getWebPage(url)
# targets the main table in the url that contains the playable character list
tableLinks = getAllPlayableCharacterTableLinks(soup)
characterLinks = []
count = 0
for link in tableLinks:
    if count % 4 == 0:
        characterLinks.append(link)
    count += 1
saveCharacterImages(characterLinks)
writeCsvHeader()
writeNamesAndUrls(characterLinks)