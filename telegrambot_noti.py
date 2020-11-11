import requests
from bs4 import BeautifulSoup

# 질본 > 시별 발생 현황 url
url = "https://www.seoul.go.kr/coronaV/coronaStatus.do"
response = requests.get(url)
html = BeautifulSoup(response.content, 'lxml')
statushtml = html.select("table.tstyle-status")
statustable = statushtml[0]

# 수집 시점 정보
timehtml = html.select("p.txt-status")
timeinfo = timehtml[0].text
timeinfo = timeinfo.replace('(','').replace(')','')
table_body = statustable.select_one("tbody")
name_tag = table_body.find_all("th")
cnt_tag = table_body.find_all("td")
message="수집시점: "+timeinfo+'\n'+"서울 구: "+name_tag[15].text+'\n'+"누적확진자: "+cnt_tag[28].text+'\n'+"일일확진자: "+cnt_tag[41].text
#print(message)


# 텔레그램으로 보냄

import telepot

API_KEY = '1433312946:AAF5TB48dfsLG246KlAGrX80z2wdus7ReNM'
bot = telepot.Bot(token = API_KEY)
chat_id = "18794449"
bot.sendMessage(chat_id = chat_id, text = message)
