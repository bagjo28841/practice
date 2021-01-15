# 프로그래밍을 통해 정보 수집하기 - 크롤링
# 요청(정보를 원하는 사람 = Client) -주소(url) -> 응답(정보를 주는 사람)
# 응답자 -> 문서(html, xml,json(제일 많이 씀, javascript때 다룰 예정) 등) 보냄 -> -브라우저(예쁘게 처리) -> (정보를 원하는 사람)

# 파이썬의 가장 중요한 라이브러리! 요청을 보내는 라이브러리 -> requests
'''
<Request로 정보 받아서 BeautifulSoup으로 예쁘게 하자>

import requests
requests.get() -> 주소에 요청 보내서 정보 받아줘!
requests.get().text -> 정보에서 글만 뽑아줘!
requests.get().status_code -> 정보에서 상태만 뽑아줘! ex) 404..

정보 스크랩
원하는 정보가 있는 주소로 요청을 보내, 응답 저장
import requests
response = request.get(url).text 
print(response) 응답이 왔는지 정보 출력하여 확인!!

그럼 3000줄 짜리 코드가 오는데?
예쁘게 바꾸자 
from bs4 import BeautifulSoup
text = BeautifulSoup(response) -> 예쁘게 만들어줘
text.select(response) -> 특정 내용을 뽑아줘
text.select_one('정보경로') -> 특정 내용 하나만

scraping
1. 원하는 url로 들어감
2. 크롬에서 개발자도구(Developer Tool) 활성화 1) Ctrl Shift I 2) F12 3) 마우스 우클릭 - 검사
2-2. 왼쪽 위 화살표모양 눌러서 Inspector 활성화하면 화면 블록잡힘 - 누르면 그 위치로 이동
3. 거기서 우클릭 - copy - copy selector
4. 이거를 뷰티풀숲이 구조화 할 것 
'''

# import 여러개면 길이 짧은거를 위로 쓰는게 권장 스타일
import requests
from bs4 import BeautifulSoup # bs4 다 필요없으니 필요한 하나만 가져오는거

# 크롤링을 배워봅시다!
# 1. 주소(url)
url = 'https://finance.naver.com/sise/'

# 2. url로 요청을 보내 응답을 받는다
response = requests.get(url).text
print(type(response)) # <class 'requests.models.Response'> 응답객체

# 3. 받은 응답을 예쁘게 꾸며준다 (여기서부터 bs)
data = BeautifulSoup(response, 'html.parser')
print(type(data)) # <class 'bs4.BeautifulSoup'>
# print(data)

# 4. 꾸민 응답중에서 원하는 데이터를 선택한다 (select, select_one)
#result = data.select_one('#KOSPI_now')
#print(result) # 한줄까지 찾았다!
result = data.select_one('#KOSPI_now').text
print(result) # 완료!

