"""
<피보나치 수>

첫 번째 피보나치 수는 1, 두 번째 피보나치 수는 1.
그 다음부터는 앞의 수 2개를 더한 값이 된다.

n >= 2 인 경우, 아래 점화식을 따른다.
F(n) = F(n-1) + F(n-2)

n=11일 때 -> 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
"""

### 풀이1. 재귀함수 사용
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

### 풀이2. 반복문 사용 - for문
def fib(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1
    for i in range(1, n):
        a, b = b, a+b
    return a


### 풀이2. 반복문 사용 - while문
def fib(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1
    while a < n:
        a, b = b, a+b
    return a


### 풀이3. Generator(제너레이터) 사용
"""
# 사용법
f = fib()
print(next(f))  # 1
print(next(f))  # 1
print(next(f))  # 2
print(next(f))  # 3
print(next(f))  # 5
print(next(f))  # 8
"""
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b


### 풀이4. Memoization(메모이제이션) 사용
# 반복되는 수는 메모리에 저장해 두고, 반복 계산 대신 저장해둔 값 사용
def fib(n):
    fib_list = [1, 1]
    if n == 1 or n == 2:
        return 1
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n-1]


# ### 풀이5. Lambda (람다)사용
# fib = lambda n: 1 if n<=2 else fib(n-1) + fib(n-2)



if __name__ == "__main__":
    res = fib(10)
    print('res:', res)
