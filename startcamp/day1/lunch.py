# list(리스트 - 다른 언어들의 array) pythonic 자기들만의 언어
stores = ["a","b","c"] # 다량의 데이터면 변수명을 복수로 하기
print(stores)
print(stores[1])

# random 모듈 및 sample 함수 사용
import random
val = random.sample(stores, 1) 
print(val)