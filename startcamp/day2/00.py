# 숫자
number = 3
print(type(number))

# 문자열
string = '문자열'
print(type(string))

# 참거짓 boolean
boolean = True
print(type(boolean))

# 형변환(강제)
string_number = '3'
#print(string_number +5) -> error
print(int(string_number) + 5)

# f-string / string interpolation
name = '홍길동'
print(f'{name}입니다. 반갑습니다')