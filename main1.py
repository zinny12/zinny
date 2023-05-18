import requests
from bs4 import BeautifulSoup as bs
import pprint
import sys
import telegram

num = 0
summary = ""

chat_token = "5638730978:AAErxfMUsSu37fKHFHWMmpmbuig94t1qWQo"
Jinny_id = "5711468830"
  
bot = telegram.Bot(token = chat_token) 

Materials = ['SK머티리얼즈', '한솔케미칼', '솔브레인', '동진쎄미켐', '이엔에프테크놀로지', '덕산테코피아', '백광산업', '경인양행', '디엔에프', '오션브릿지', '와이씨켐', '지오엘리먼트', '엘티씨', '코미코', '후성', '티이엠씨', '레이크머티리얼즈', '원익머티리얼즈', '제이아이테크']


for n in range(1,41,10) : 
    response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=1&pd=7&ds=&query='+"하이닉스"+'&start='+str(n))
    soup = bs(response.text, 'html.parser')
    container = soup.select('ul.list_news > li')
    for i in container:
        num = num + 1
        press = i.select_one('a.info.press').text.strip()
        title = i.select_one('div.news_area > a').text.strip()
        date = i.select_one('span.info').text.strip()
        link = i.select_one('a.news_tit').get('href')
        text = title +"\n" + link
        #bot.sendMessage(chat_id = Jinny_id, text=text)
        response = requests.post('https://api.telegram.org/bot5638730978:AAErxfMUsSu37fKHFHWMmpmbuig94t1qWQo/sendmessage?chat_id=5711468830&text='+text)
        
'''
num = 0
for n in range(1,41,10) : 
    response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=1&pd=7&ds=&query='+"삼성전자"+'&start='+str(n))
    soup = bs(response.text, 'html.parser')
    container = soup.select('ul.list_news > li')
    for i in container:
        num = num + 1
        press = i.select_one('a.info.press').text.strip()
        title = i.select_one('div.news_area > a').text.strip()
        date = i.select_one('span.info').text.strip()
        link = i.select_one('a.news_tit').get('href')
        text = title +"" + link
        bot.sendMessage(chat_id = Jinny_id, text=text)
        
num = 0
for n in range(1,41,10) : 
    response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=1&pd=7&ds=&query='+"반도체"+'&start='+str(n))
    soup = bs(response.text, 'html.parser')
    container = soup.select('ul.list_news > li')
    for i in container:
        num = num + 1
        press = i.select_one('a.info.press').text.strip()
        title = i.select_one('div.news_area > a').text.strip()
        date = i.select_one('span.info').text.strip()
        link = i.select_one('a.news_tit').get('href')
        text = title +"" + link
        bot.sendMessage(chat_id = Jinny_id, text=text)

num = 0
for n in range(1,41,10) : 
    response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=1&pd=7&ds=&query='+"DRAM"+'&start='+str(n))
    soup = bs(response.text, 'html.parser')
    container = soup.select('ul.list_news > li')
    for i in container:
        num = num + 1
        press = i.select_one('a.info.press').text.strip()
        title = i.select_one('div.news_area > a').text.strip()
        date = i.select_one('span.info').text.strip()
        link = i.select_one('a.news_tit').get('href')
        text = title +"" + link
        bot.sendMessage(chat_id = Jinny_id, text=text)
        
num = 0
for n in range(1,41,10) : 
    response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=1&pd=7&ds=&query='+"NAND"+'&start='+str(n))
    soup = bs(response.text, 'html.parser')
    container = soup.select('ul.list_news > li')
    for i in container:
        num = num + 1
        press = i.select_one('a.info.press').text.strip()
        title = i.select_one('div.news_area > a').text.strip()
        date = i.select_one('span.info').text.strip()
        link = i.select_one('a.news_tit').get('href')
        text = title +"" + link
        bot.sendMessage(chat_id = Jinny_id, text=text)
        
num = 0
for n in range(1,41,10) :  
    response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=1&pd=7&ds=&query='+"메모리"+'&start='+str(n))
    soup = bs(response.text, 'html.parser')
    container = soup.select('ul.list_news > li')
    for i in container:
        num = num + 1
        press = i.select_one('a.info.press').text.strip()
        title = i.select_one('div.news_area > a').text.strip()
        date = i.select_one('span.info').text.strip()
        link = i.select_one('a.news_tit').get('href')
        text = title +"" + link
        bot.sendMessage(chat_id = Jinny_id, text=text)
'''

      
