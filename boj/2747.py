# 2747. 피보나치 수
# https://www.acmicpc.net/problem/2747

### 재귀함수 사용 - 시간초과
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

### 메모이제이션 사용 - 성공
def fib(n):
    fib_lsit = [0, 1, 1]
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(3, n+1):
            fib_lsit.append(fib_lsit[i-1] + fib_lsit[i-2])
    return fib_lsit[n]


n = int(input())
print(fib(n))