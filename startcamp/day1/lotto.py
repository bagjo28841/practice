import random

numbers = list(range(1,46))
val = random.sample(numbers, 6) # iterator(반복 가능한 객체)
print(type(val))

# string-interpolation: stirng사이에 값 삽입
# f-string
print(f'오늘의 로또 번호는 {val} 입니다.')

print("1번: {0}".format(val[0]))
print("2번: {0}".format(val[1]))
print("3번: {0}".format(val[2]))
print("4번: {0}".format(val[3]))
print("5번: {0}".format(val[4]))
print("6번: {0}".format(val[5]))
print("축하합니다!!")

# 과제
import datetime