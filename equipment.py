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

Equipment = ['원익IPS', '유진테크', '주성엔지니어링', '테스', 'HPSP', '파크시스템스', '넥스틴', '오로스테크놀로지', '케이씨텍', '피에스케이', '에이피티씨', '와이아이케이', '엘오티베큠', '싸이맥스', '제우스', '디바이스이엔지', '저스템', '원익홀딩스', '케이씨텍', '에스티아이', '씨앤지하이테크', 'GST', '유니셈', '지앤비에스엔지니어링']
summary = "[Materials]" + "\n"
numberofnews = 0
 
for company in Equipment:
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



'''
OSAT = ['SFA반도체', '하나마이크론', '네패스', '엘비세미콘', '한양디지텍', '아이텍', '시그네틱스', '윈팩', '두산테스나', '네패스아크', '에이팩트', '큐알티', '심텍', '아비코전자', '해성디에스', '엠케이전자', '덕산하이메탈']

value_chain = "[OSAT]" + "\n"

for company in OSAT:
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

please()   
#bot.send_message(chat_id = "5711468830", text = value_chain, disable_web_page_preview= True, parse_mode = 'Markdown')



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

please()       
#bot.send_message(chat_id = "5711468830", text = value_chain, disable_web_page_preview= True, parse_mode = 'Markdown')

'''
