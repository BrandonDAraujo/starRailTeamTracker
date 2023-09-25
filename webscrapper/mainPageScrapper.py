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

def getGuideTable(url):
    soup = getWebPage(url)
    tab = soup.find('div', class_="a-tabContainer")
    a = tab.find_all('a')
    return a

def getGuideMainStats(url):
    soup = getWebPage(url)
    tabContainer = soup.find('div', class_="a-tabContainer")
    tr = tabContainer.find_all('tr')
    mainStats = tr[4].find_all('b')
    return mainStats

def getSilverWolfTable(url):
    soup = getWebPage(url)
    tab = soup.find('table', class_="a-table a-table")
    a = tab.find_all('a')
    count = 0
    # for line in a:
    #     print(count,line.text)
    #     count += 1
    return a

def getSilverWolfMainStats(url):
    soup = getWebPage(url)
    tab = soup.find('table', class_="a-table a-table")
    silverWolfMainStats = tab.find_all('b')
    return silverWolfMainStats

def saveCharacterImages(characterLinks):
    for link in characterLinks:
        img_data = requests.get(link.next.attrs["data-src"]).content
        with open('webscrapper/images/'+link.text.strip(' ')+'.png', 'wb') as handler:
            handler.write(img_data)
    return 
 
def writeCsvData(characterLinks):
    with open('webscrapper/character.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','LightCone','Head','Gloves','Body','Feet','Sphere','Rope','BodyMainStat','FeetMainStat','SphereMainStat','RopeMainStat'])
        for link in characterLinks:
            name = link.text.strip(' ')
            print('Writing',name,'data...')
            lightCone = ''
            head = ''
            gloves = ''
            body = ''
            feet = ''
            sphere = ''
            rope = ''
            bodyMainStat = ''
            feetMainStat = ''
            sphereMainStat = ''
            ropeMainStat = ''
            if name == 'Silver Wolf':
                # TODO combine these two functions so they don't make to seprate calls to the same web page
                silverWolfInfo = getSilverWolfTable(link.attrs["href"])
                silverWolfMainStats = getSilverWolfMainStats(link.attrs["href"])
                lightCone = silverWolfInfo[0].text.strip(' ')
                head = silverWolfInfo[4].text.strip(' ')
                gloves = silverWolfInfo[4].text.strip(' ')
                body = silverWolfInfo[4].text.strip(' ')
                feet = silverWolfInfo[4].text.strip(' ')
                sphere = silverWolfInfo[5].text.strip(' ')
                rope = silverWolfInfo[5].text.strip(' ')
                bodyMainStat = silverWolfMainStats[3].nextSibling.strip(' ') 
                feetMainStat = silverWolfMainStats[4].nextSibling.strip(' ')
                sphereMainStat = silverWolfMainStats[5].nextSibling.strip(' ')
                ropeMainStat = silverWolfMainStats[6].nextSibling.strip(' ')
                writer.writerow([name,lightCone,head,gloves,body,feet,sphere,rope,bodyMainStat,feetMainStat,sphereMainStat,ropeMainStat]) 
            else:
                # TODO combine these two functions so they don't make to seprate calls to the same web page
                guideInfo = getGuideTable(link.attrs["href"])
                mainStats = getGuideMainStats(link.attrs["href"])
                lightCone = guideInfo[0].text
                if len(guideInfo) == 8:
                    head = guideInfo[1].text
                    gloves = guideInfo[1].text
                    body = guideInfo[1].text
                    feet = guideInfo[1].text
                    sphere = guideInfo[2].text
                    rope = guideInfo[2].text
                elif len(guideInfo) == 9:
                    head = guideInfo[1].text + "/" + guideInfo[2].text
                    gloves = guideInfo[1].text + "/" +  guideInfo[2].text
                    body = guideInfo[1].text + "/" +  guideInfo[2].text
                    feet = guideInfo[1].text + "/" +  guideInfo[2].text
                    sphere = guideInfo[3].text
                    rope = guideInfo[3].text
                bodyMainStat = mainStats[0].nextSibling.strip(':').strip(' ')
                feetMainStat = mainStats[1].nextSibling.strip(':').strip(' ')
                sphereMainStat = mainStats[2].nextSibling.strip(':').strip(' ')
                ropeMainStat = mainStats[3].nextSibling.strip(':').strip(' ')
                writer.writerow([name,lightCone,head,gloves,body,feet,sphere,rope,bodyMainStat,feetMainStat,sphereMainStat,ropeMainStat])
    return


# main page that we get the character list from
url = 'https://game8.co/games/Honkai-Star-Rail/archives/404256'
soup = getWebPage(url)
# targets the main table in the url that contains the playable character list
tableLinks = getAllPlayableCharacterTableLinks(soup)
characterLinks = []
count = 0
#store the characater links alone
for link in tableLinks:
    if count % 4 == 0:
        characterLinks.append(link)
    count += 1
# saveCharacterImages(characterLinks)
writeCsvData(characterLinks)