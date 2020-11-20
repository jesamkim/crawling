## Daily C19 Confirmed Cases => JSON file

import requests
from bs4 import BeautifulSoup

# C19 crawling target url
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="

response = requests.get(url)
html = BeautifulSoup(response.content, 'lxml')

# crawling tag
timehtml = html.select("div.timetable")
timeinfo = timehtml[0].select_one('p').text
mgt24 = html.select("div.data_table")
table_body = mgt24[0].select_one("tbody")
city_tag = table_body.find_all("th")
number_tag = table_body.find_all("td")

# List "city_name" Declaration for name of cities
city_name = []

# Append to list "city_name"
for th in range(1,18):
   city_name.append(city_tag[th].text)

# List "daily_patient" Declaration for Daily C19 Confired Cases
daily_patient = []


# Append to list "daily_patient"
for td in range(1,18):
   daily_patient.append(number_tag[(td*8)].text)


#print(timeinfo, "Daily C19 Confirmed")
#print(city_name)
#print(daily_patient)

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
GYEONGGI = {"lat":37.68382,"lng":126.742401} # Yongin
GANGWON = {"lat":38.078366,"lng":128.228302} # Gangneung
CHUNGBUK = {"lat":36.995972,"lng":127.926178} # Cheongju
CHUNGNAM = {"lat":36.279707,"lng":126.909943} # Boryeong
JEONBUK = {"lat":35.431582,"lng":127.415314}  # Jeonju
JEONNAM = {"lat":36.820279,"lng":127.10495} # Yeosu
KYUNGBUK = {"lat":36.813683,"lng":128.626556} # Gumi
KYUNGNAM = {"lat":35.498692,"lng":128.747406} # Jinju
JEJU = {"lat":33.50000,"lng":126.51667}


temp_str = []
for i in range(0,17):
  for j in range(0,int(daily_patient[i])):
    if i == 0: temp_str.append(SEOUL)
    elif i == 1: temp_str.append(BUSAN)
    elif i == 2: temp_str.append(DAEGU)
    elif i == 3: temp_str.append(INCHEON)
    elif i == 4: temp_str.append(GWANGJU)
    elif i == 5: temp_str.append(DAEJEON)
    elif i == 6: temp_str.append(ULSAN)
    elif i == 7: temp_str.append(SEJONG)
    elif i == 8: temp_str.append(GYEONGGI)
    elif i == 9: temp_str.append(GANGWON)
    elif i == 10: temp_str.append(CHUNGBUK)
    elif i == 11: temp_str.append(CHUNGNAM)
    elif i == 12: temp_str.append(JEONBUK)
    elif i == 13: temp_str.append(JEONNAM)
    elif i == 14: temp_str.append(KYUNGBUK)
    elif i == 15: temp_str.append(KYUNGNAM)
    elif i == 16: temp_str.append(JEJU)

file_data["positions"] = temp_str

#print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

with open('daily_covid.json', 'w', encoding="utf-8") as make_file:
  json.dump(file_data, make_file, indent="  ")

print("daily_covid.json file is generared.")
