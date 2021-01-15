# 함수: 특정 역할을 하는 코드의 집합
# 하나의 함수는 하나의 역할만 해야한다.
# 함수를 왜 만드나요? 재사용성!

# 함수 정의
def funcname(parameter_list):
    """
    docstring
    함수의 설명서 - 하는 역할
    """
    pass

def add(a, b):
    result = a + b
    print(result) # 얘는 반환값 None
    return result # 반환값!
    # 함수는 return을 만나면 반환값을 뱉고 종료됨 - 그 이후 실행X

# 함수 실행(호출)
add(1, 2)
print(add(2, 3))

# 함수 실행 결과(return)값 변수에 할당
result = add(1, 2)
print(result)

# 미니 실습) 주어진 양수 n