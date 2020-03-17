import requests
from bs4 import BeautifulSoup

# 질본 > 국내 발생 현황 url
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId="

response = requests.get(url)
html = BeautifulSoup(response.content, 'lxml')

# h4 제목 부분
base_time = html.select_one("p.s_descript").text

# 누적 확진자 현황 table 부분
mgt16 = html.select("div.data_table")

# title는 컬럼 및 patient 는 실제 수치
title = mgt16[0].select_one("thead").text
patient = mgt16[0].select_one("tbody").text

# 텍스트 split
title2 = title.split('\n')
patient2 = patient.split('\n')

# 출력 Test. 여기서 문제가 없으면 이 변수들을 Telegram API로 보냄
message = base_time + '\n' + title2[2] + ":" + patient2[2] + "\n" + title2[3] + ":" + patient2[3] + '\n' + title2[4] + ":" + patient2[4] + '\n' + title2[5] + ":" + patient2[5]
print(message)
