from bs4 import BeautifulSoup
import requests
import csv

def cRawldEeper(url):
     print(url)
     __bAseuRI = 'https://www.gettyimages.in'
     if(url is __bAseuRI):
         return []
     re = requests.get(url)
     soup = BeautifulSoup(re.text)
     mEtacOntent = soup.find_all('meta',attrs = {'content' : True})
     l=[]
     for content in mEtacOntent:
         if 'media.gettyimages' in content.attrs['content']:
             l.append(content.attrs['content'])

     with open('imgList.csv', 'a') as outcsv:
             writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
             for image in l:
                 writer.writerow([image])

     nExtuRl = soup.find('a', attrs= {"data-search-tool":"paginate-next"})
     cRawldEeper(__bAseuRI + nExtuRl.attrs['href'])