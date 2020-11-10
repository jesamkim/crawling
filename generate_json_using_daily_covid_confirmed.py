## 시도별 일일 확진자 수 => JSON 출력

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
daily_patient = []


# 일일 확진자 수를 리스트에 append
for td in range(1,18):
   daily_patient.append(number_tag[(td*8)].text)


# 일시 / 도시명 / 일일 확진자 리스트 출력
print(timeinfo, "일일 확진자 수")
print(city_name)
print(daily_patient)


###############################################
# 여기서부터는 daily_patient 의 값으로 JSON 위도 경도 만들기
###############################################

import json
from collections import OrderedDict

file_data = OrderedDict()

SEOUL = {"lat":37.56667,"lng":126.97806}
BUSAN  = {"lat":35.17944,"lng":129.07556}
DAEGU  = {"lat":35.87222,"lng":128.60250}
INCHEON  = {"lat":37.45639,"lng":126.70528}
GWANGJU  = {"lat":35.15972,"lng":126.85306}
DAEJEON  = {"lat":36.35111,"lng":127.38500}
ULSAN = {"lat":35.53889,"lng":129.31667}
SEJONG = {"lat":36.48750,"lng":127.28167}
GYEONGGI = {"lat":37.68382,"lng":126.742401} # 용인 기준
GANGWON = {"lat":38.078366,"lng":128.228302} # 강릉 기준
CHUNGBUK = {"lat":36.995972,"lng":127.926178} # 청주 기준
CHUNGNAM = {"lat":36.279707,"lng":126.909943} # 보령 기준
JEONBUK = {"lat":35.431582,"lng":127.415314}  # 전주 기준
JEONNAM = {"lat":36.820279,"lng":127.10495} # 여수 기준
KYUNGBUK = {"lat":36.813683,"lng":128.626556} # 구미 기준
KYUNGNAM = {"lat":35.498692,"lng":128.747406} # 진주 기준
JEJU = {"lat":33.50000,"lng":126.51667}


temp_str = []
for i in range(1,17):
  for j in range(0,int(daily_patient[i-1])):
    if i == 1: temp_str.append(SEOUL)
    elif i == 2: temp_str.append(BUSAN)
    elif i == 3: temp_str.append(DAEGU)
    elif i == 4: temp_str.append(INCHEON)
    elif i == 5: temp_str.append(GWANGJU)
    elif i == 6: temp_str.append(DAEJEON)
    elif i == 7: temp_str.append(ULSAN)
    elif i == 8: temp_str.append(SEJONG)
    elif i == 9: temp_str.append(GYEONGGI)
    elif i == 10: temp_str.append(GANGWON)
    elif i == 11: temp_str.append(CHUNGBUK)
    elif i == 12: temp_str.append(CHUNGNAM)
    elif i == 13: temp_str.append(JEONBUK)
    elif i == 14: temp_str.append(JEONNAM)
    elif i == 15: temp_str.append(KYUNGBUK)
    elif i == 16: temp_str.append(KYUNGNAM)
    elif i == 17: temp_str.append(JEJU)

file_data["positions"] = temp_str

## JSON 파일 내용 출력
#print(json.dumps(file_data, ensure_ascii=False, indent="  "))

# daily_covid.json 파일 생성
with open('daily_covid.json', 'w', encoding="utf-8") as make_file:
  json.dump(file_data, make_file, ensure_ascii=False, indent="  ")
