import requests
from pprint import pprint

key = 'rq2kBGp%2BMv32xNqQDrDEw7AoA36%2B5Bjr97JeH%2B%2FxCQjHYx9IV215w1BO4S5MUYfKswQYa2vdyu5%2BVWRfg1bMbA%3D%3D'
return_type = 'json'
num_of_rows = '5'
page_no = '1'
sido_name = '서울'
ver = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_name}&ver={ver}'
response = requests.get(url).json()
#print(type(response))
#pprint(response) # 구글 익스텐션으로 봐도 됨

# sidoName의 미세먼지 농도는 pm10value입니다. 라는 메세지 출력하기

result_name = response['response']['body']['items'][1]['stationName']
result_dust = response['response']['body']['items'][1]['pm10Value']
print(f'{result_name}의 미세먼지 농도는 {result_dust}입니다.')