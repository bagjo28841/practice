# 조건문

# 주어진 양수 n이 홀수, 짝수인지 판별하여 출력하는 코드
n = 10
if n % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 반복문
numbers = list(range(1,10))
new_list = []
for number in numbers: #복수형 리스트 중 단수형 원소
    if number % 2 == 0:
        continue
    else:
        new_list.append(number)
        print(f'{number}는 홀수입니다.')
        #print('{0} 는 홀수입니다.'.format(number))
print(f'{new_list}는 홀수입니다.')