import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page=1
    fw = open('crawler.txt', 'w')
    while page<=max_pages:
        url='https://en.wikipedia.org/wiki/List_of_Baby_Steps_episodes'
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html.parser")

        for link in soup.findAll('link'):
            title=link.string
            a = str(title)
            href='https://en.wikipedia.org' +link.get('href')


            fw.write(a+' : '+href+"\n")

            #print(title)
            #print(href)

        page+=1
    fw.close()
    fr=open('crawler.txt','r')
    text=fr.read()
    print(text)
    fr.close()


trade_spider(1)