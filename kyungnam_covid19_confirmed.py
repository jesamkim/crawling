## 경남 확진자 현황

import requests
from bs4 import BeautifulSoup

# 경상남도 현황 url
url = "http://xn--19-q81ii1knc140d892b.kr/main/main.do"

response = requests.get(url)
html = BeautifulSoup(response.content, 'lxml')


# 수집 시점 정보
timehtml = html.select("p.exp")
timeinfo = timehtml[0].text
timeinfo = timeinfo.replace('\t','').replace('\r','').replace('\n','').replace('(','').replace(')','')


# 현황 table 부분
mt20 = html.select("div.city_board")

# 테이블의 thead 태그 범위 (column)
table_head = mt20[0].select_one("thead")

# 테이블의 tbody 태그 범위 (row)
table_body = mt20[0].select_one("tbody")

# 테이블 컬럼 이름(경남 시/군) 태그 범위
col_tag = table_head.find_all("th")

# 테이블 컬럼 이름(경남 시/군)을 저장할 리스트 생성
col_name = []

# 경남 시/군 명을 리스트에 append
for th in range(0,18):
   col_name.append(col_tag[th].text)


# 확진자 수 태그 범위
number_tag = table_body.find_all("td")

# 경남 시/군별 확진자 정보 저장할 리스트 생성
kyungnam_numbers = []

# 경남 시/군별 확진자 정보를 리스트에 append
for td in range(0,18):
   kyungnam_numbers.append(number_tag[td].text)



# 리스트 출력
print(timeinfo, "경남 시/군별 확진자 수")
print(col_name)
print(kyungnam_numbers)