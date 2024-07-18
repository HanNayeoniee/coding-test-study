"""
<팩토리얼>

N! = N * (N-1) * (N-2) * ... 3 * 2 * 1
factorial(N) = N * factorial(N-1)
"""

### 풀이1. 재귀함수 사용
def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n-1) * n


### 풀이2. 반복문 사용
def fac(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans
    

## 풀이3. 메모이제이션 사용
cache = {}
def fac(n):
    global cache

    if n in cache:
        return cache[n]
    elif n <= 1:
        cache[1] = 1
        return 1
    else:
        cache[n] = fac(n-1) * n
        return cache[n]

if __name__ == "__main__":
    print(fac(3))
    print(fac(10))