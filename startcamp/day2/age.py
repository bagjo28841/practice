# API 활용하기
'''
API란? Application Programming Interface
응용프로그래밍 간의 대화
ex) 배민 가입 - 소셜로그인(페이스북)
배민이 페이스북에게 가입희망자의 정보 요청 - 페북이 id pw 보내줌(JSON으로)
배민이 받은 정보로 가입시켜서 로그인함
두 어플리케이션 사이의 커뮤니케이션(전체 과정)! = API 
소통을 어떻게 할거냐? - 대표적으로 요청보내고, JSON 파일 받고

JSON JavaScript Object Notation
어플리케이션끼리 데이터를 주고받기 위한 약속(타입)!
파이썬의 Dictionary와 list 구조로 쉽게 변환하여 사용 가능
우리가 했던 Movie 실습 같은 구조
'''

import requests
name = 'harry'
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json() #제이슨 데이터로 받기
# .text / .jason()
# attribute(호출하는게 아니라 속성값) vs method(클래스 안에 속해있는 함수 request.get()) vs function
print(response)
print(type(response)) #딕셔너리로 변환

age = response['age'] # 이걸 추출해오는 과정이 중요한 것!!
print(f'{name}의 나이는 {age}살 입니다.')