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

# 테이블의 thead 태그 범위 (column)
table_head = mgt24[0].select_one("thead")

# 테이블의 tbody 태그 범위 (row)
table_body = mgt24[0].select_one("tbody")



# 테이블 컬럼 이름 범위
col_tag = table_head.find_all("th")

# 테이블 컬럼 이름을 저장할 리스트 생성
col_name = []

# 컬럼명을 리스트에 append
for th in range(3,11):
   col_name.append(col_tag[th].text)



# 도시명 태그 범위
city_tag = table_body.find_all("th")

# 도시명만 저장할 리스트 생성 -> 울산[7]
city_name = []

# 울산시에 대한 도시명을 리스트에 append
city_name.append(city_tag[7].text)



# 확진자 수 태그 범위
number_tag = table_body.find_all("td")

# 울산시 확진자 관련 정보 저장할 리스트 생성
ulsan_daily = []

# 울산시에 대한 확진자 수 정보를 리스트에 append
for td in range(56,64):
   ulsan_daily.append(number_tag[td].text)



# 리스트 출력
print(timeinfo)
print(city_name)
print(col_name)
print(ulsan_daily)