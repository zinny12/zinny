import requests
from bs4 import BeautifulSoup as bs
import pprint
import sys
import telegram

num = 0

chat_token = "5638730978:AAErxfMUsSu37fKHFHWMmpmbuig94t1qWQo"
Jinny_id = "5711468830"
token = "5638730978:AAErxfMUsSu37fKHFHWMmpmbuig94t1qWQo"  
bot = telegram.Bot(chat_token) 

TestParts = ['리노공업', 'ISC', '오킨스전자', '티에스이', '샘씨엔에스', '타이거일렉', '한미반도체', '이오테크닉스', '프로텍', '유니테스트', '피에스케이홀딩스', '코세스', '네오셈', '디아이', '엑시콘', '테크윙', '인텍플러스', '신성이엔지', '한양이엔지', '원방테크', '에스엠코어']

summary = "[TestParts]" + "\n"
numberofnews = 0
 
for company in TestParts:
    summary = "▶" + company + "\n" 
    for n in range(1,41,10) : 
        response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=0&pd=4&ds=&query='+company+'&start='+str(n))
        soup = bs(response.text, 'html.parser')
        container = soup.select('ul.list_news > li')
        for i in container:
            num = num + 1
            title = i.select_one('div.news_area > a').text.strip()
            link = i.select_one('a.news_tit').get('href')
            #text1 = title + "\n" + link + "\n" + "\n"
            #text1 = '\"<a href=\''+ link + '\'>'+ title + '</a>\"' "\n"
            summary = summary + text1
response = requests.post('https://api.telegram.org/bot5638730978:AAErxfMUsSu37fKHFHWMmpmbuig94t1qWQo/sendmessage?chat_id=5711468830&text='+summary)
#bot.send_message(chat_id = "5711468830", text = summary, parse_mode = 'Markdown')
#bot.send_message(chat_id = update.message.chat_id, text = "<a href='https://www.google.com/'>Google</a>", parse_mode = 'Markdown')

