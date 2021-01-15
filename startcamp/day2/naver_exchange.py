import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
#print(response)

data = BeautifulSoup(response, 'html.parser')
#parser 이름이 기억이 안난다면?
#Beautiful Soup Documentation 공식문서에서 확인
print(type(data))

result = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(result)