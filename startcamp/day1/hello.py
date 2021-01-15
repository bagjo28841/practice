greeting = "안녕하세요!" # 저장(변수 사용)
# 띄어쓰기 습관을 잘 들입시다

n = 1
while n < 6:
    print(greeting)
    n += 1

print()
for _ in range(1, 6): #안쓰이고 있으니까 i대신 _
    print(greeting)

'''
PSL Python Standard Library
안에 내장함수도 있고,
함수들을 모은 모듈도 있고(내장x), 
모듈들을 모은 것을 패키지라고 함
'''