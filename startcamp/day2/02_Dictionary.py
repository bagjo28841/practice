# Dictionary (딕셔너리) - 궁극의 자료형

# 인덱스X(순서 의미 없음!) 딕셔너리는 key값으로 접근
my_home = {
    'location' : 'seoul',
    'area-code' : '02'
}

# 딕셔너리 원소 접근 1번
# 없는 key로 접근하려고 하면 KeyError
print(my_home['location'])
print(my_home['area-code'])
# print(my_home['name'])

# 딕셔너리 원소 접근 2번
# 딕셔너리 클래스가 가지고 있는 함수들 이용
print(my_home.get('location'))
print(my_home.get('area-code'))
print(my_home.get('name'))
# 이 방식은 에러로 종료되지 않고, None으로 나오고 진행됨!