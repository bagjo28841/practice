import requests
from bs4 import BeautifulSoup

KEY = 'rq2kBGp%2BMv32xNqQDrDEw7AoA36%2B5Bjr97JeH%2B%2FxCQjHYx9IV215w1BO4S5MUYfKswQYa2vdyu5%2BVWRfg1bMbA%3D%3D'
URL = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=xml'

response = requests.get(URL).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[0]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')



# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
# 괄호는 기본적으로 안쓰는게 파이썬 공식 스타일

if (dust > 150):
    print('매우 나쁨')
elif (dust > 80 and dust <= 150):
# elif 80 < dust <= 150:
    print('나쁨')
elif (dust > 30 and dust <= 80):
    print('보통')
else:
    print('좋음')