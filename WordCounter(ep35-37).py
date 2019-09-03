import requests
from bs4 import BeautifulSoup
import operator

Baby_steps="https://en.wikipedia.org/wiki/List_of_Baby_Steps_episodes"


def start(url):
    word_list=[]
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,"html.parser")
    for post_text in soup.findAll('td',{'class':'description'}):
        content = post_text.string
        words=content.lower().split()
        for each_word in words:
            #print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)
    #print(*word_list)

def clean_up_list(word_list):
    clean_word_list=[]
    for word in word_list:
        symbols="!@#$%^&*()_+{}|:\"<>?-=[];',./0123456789~`"
        for i in range(0, len(symbols)):
            word=word.replace(symbols[i],"")
        if len(word)>0:
            #print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key= operator.itemgetter(1)):
        print(key, value )




start(Baby_steps)
