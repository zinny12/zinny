import requests
from bs4 import BeautifulSoup as bs
import pprint
import sys
import telegram
import asyncio
from telegram.constants import ParseMode



chat_token = "5638730978:AAErxfMUsSu37fKHFHWMmpmbuig94t1qWQo"
Jinny_id = "5711468830"
token = "5638730978:AAErxfMUsSu37fKHFHWMmpmbuig94t1qWQo"  
bot = telegram.Bot(chat_token) 



TestParts = ['리노공업', 'ISC', '오킨스전자', '티에스이', '샘씨엔에스', '타이거일렉', '한미반도체', '이오테크닉스', '프로텍', '유니테스트', '피에스케이홀딩스', '코세스', '네오셈', '디아이', '엑시콘', '테크윙', '인텍플러스', '신성이엔지', '한양이엔지', '원방테크', '에스엠코어']

value_chain = "[Test Parts]" + "\n"

for company in TestParts:
    summary = ""
    for n in range(1,41,10) : 
        response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=0&pd=4&ds=&query='+company+'&start='+str(n))
        soup = bs(response.text, 'html.parser')
        container = soup.select('ul.list_news > li')
        for i in container:
            title = i.select_one('div.news_area > a').text.strip()
            link = i.select_one('a.news_tit').get('href')
            title = title.replace('[', '')
            title = title.replace(']', ' - ')
            text1 = '[' + title + '](' + link + ')' + "\n" + "\n"
            summary = summary + text1
    
    companyname = "▶" + company + "\n" 
    if summary !="":
        value_chain = value_chain + companyname + summary
    else:
        pass

   
bot.send_message(chat_id = "5711468830", text = value_chain, disable_web_page_preview= True, parse_mode = 'Markdown')

