# 10872. 팩토리얼
# https://www.acmicpc.net/problem/10872


N = int(input())

cache = {}
def factorial(n):
    if n in cache:
        return cache[n]
    elif n <= 1:
        cache[1] = 1
        return cache[1]
    else:
        cache[n] = factorial(n-1) * n
    return cache[n]


print(factorial(N))