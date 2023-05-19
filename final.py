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

async def main():
    await bot.send_message(chat_id = "5711468830", text = value_chain, disable_web_page_preview= True, parse_mode = 'Markdown')


Materials = ['SK머티리얼즈', '한솔케미칼', '솔브레인', '동진쎄미켐', '이엔에프테크놀로지', '덕산테코피아', '백광산업', '경인양행', '디엔에프', '오션브릿지', '와이씨켐', '지오엘리먼트', '엘티씨', '코미코', '후성', '티이엠씨', '레이크머티리얼즈', '원익머티리얼즈', '제이아이테크']

value_chain = "[Materials]" + "\n"

for company in Materials:
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
    
asyncio.run(main())

#await bot.send_message(chat_id = "5711468830", text = value_chain, disable_web_page_preview= True, parse_mode = 'Markdown')


Parts = ['티씨케이', '하나머티리얼즈', '윌덱스', '비씨엔씨', '케이엔제이', '에스앤에스텍', '에프에스티', '아스플로', '한솔아이원스', '뉴파워프라즈마', '원익QnC', '메카로', '미코']

value_chain = "[Parts]" + "\n"

for company in Parts:
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
    
asyncio.run(main())
#await bot.send_message(chat_id = "5711468830", text = value_chain, disable_web_page_preview= True, parse_mode = 'Markdown')


Equipment = ['원익IPS', '유진테크', '주성엔지니어링', '테스', 'HPSP', '파크시스템스', '넥스틴', '오로스테크놀로지', '케이씨텍', '피에스케이', '에이피티씨', '와이아이케이', '엘오티베큠', '싸이맥스', '제우스', '디바이스이엔지', '저스템', '원익홀딩스', '케이씨텍', '에스티아이', '씨앤지하이테크', 'GST', '유니셈', '지앤비에스엔지니어링']

value_chain = "[Equipment]" + "\n"

for company in Equipment:
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

asyncio.run(main())
#await bot.send_message(chat_id = "5711468830", text = value_chain, disable_web_page_preview= True, parse_mode = 'Markdown')


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

asyncio.run(main())
#await bot.send_message(chat_id = "5711468830", text = value_chain, disable_web_page_preview= True, parse_mode = 'Markdown')



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

asyncio.run(main())
#await bot.send_message(chat_id = "5711468830", text = value_chain, disable_web_page_preview= True, parse_mode = 'Markdown')

