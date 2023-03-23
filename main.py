import requests
from bs4 import BeautifulSoup as bs
import openpyxl
import pprint
import sys
import telegram
import ccxt

if __name__ == '__main__':
  chat_token = sys.argv[1]
  
bot = telegram.Bot(token = chat_token) 

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['순번','언론사','제목','날짜','링크'])

num = 0
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
        text = title +"" + link
        bot.sendMessage(chat_id = 5711468830, text=text)

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
        bot.sendMessage(chat_id = 5711468830, text=text)
        
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
        bot.sendMessage(chat_id = 5711468830, text=text)

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
        bot.sendMessage(chat_id = 5711468830, text=text)
        
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
        bot.sendMessage(chat_id = 5711468830, text=text)
        
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
        bot.sendMessage(chat_id = 5711468830, text=text)


      
