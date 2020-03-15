import requests
from bs4 import BeautifulSoup
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId="

response = requests.get(url)
html = BeautifulSoup(response.content, 'lxml')

base_time = html.select_one("p.s_descript").text
print(base_time)

mgt16 = html.select("div.data_table")

title = mgt16[0].select_one("thead").text
patient = mgt16[0].select_one("tbody").text

print(title, patient)
