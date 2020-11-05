## 경북 확진자 현황

import requests
from bs4 import BeautifulSoup

# 경상북도 현황 url
url = "http://gb.go.kr/Main/open_contents/section/wel/page.do?mnu_uid=5856&LARGE_CODE=360&MEDIUM_CODE=90"

response = requests.get(url)
html = BeautifulSoup(response.content, 'lxml')


# 수집 시점 정보
timehtml = html.select("h4")
timeinfo = timehtml[0].text


# 현황 table 부분
mt20 = html.select("div.city_corona")

# 테이블의 thead 태그 범위 (column)
table_head = mt20[0].find_all("dt")

# 테이블의 tbody 태그 범위 (row)
table_body = mt20[0].find_all("strong")

# 테이블 컬럼 이름(경북 시/군)을 저장할 리스트 생성
col_name = []

# 경북 시/군 명을 리스트에 append
for dt in range(2,25):
   col_name.append(table_head[dt].text)


# 경북 시/군별 확진자 정보 저장할 리스트 생성
kyungbuk_numbers = []

# 경북 시/군별 확진자 정보를 리스트에 append
for strong in range(2,25):
   kyungbuk_numbers.append(table_body[strong].text)

# 리스트 출력
print(timeinfo)
print(col_name)
print(kyungbuk_numbers)