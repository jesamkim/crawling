## 시도별 누적 확진자 수

import requests
from bs4 import BeautifulSoup

# 질본 > 시별 발생 현황 url
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="

response = requests.get(url)
html = BeautifulSoup(response.content, 'lxml')


# 수집 시점 정보
timehtml = html.select("div.timetable")
timeinfo = timehtml[0].select_one('p').text


# 시도별 상세 확진자 현황 table 부분 (data_table)
mgt24 = html.select("div.data_table")

# 테이블의 tbody 태그 범위
table_body = mgt24[0].select_one("tbody")


# 도시명 태그 범위
city_tag = table_body.find_all("th")

# 도시명만 저장할 리스트 생성
city_name = []

# 서울~제주에 대한 도시명 리스트에 append
for th in range(1,18):
   city_name.append(city_tag[th].text)


# 확진자 수 태그 범위
number_tag = table_body.find_all("td")

# 일일 확진자 수만 저장할 리스트 생성
total_patient = []


# 누적 확진자 수를 리스트에 append
for td in range(1,18):
   total_patient.append(number_tag[(td*8)+3].text)


# 일시 / 도시명 / 누적 확진자 리스트 출력
print(timeinfo, "누적확진자 수")
print(city_name)
print(total_patient)
