# 18230. 2xN 예쁜 타일링
# https://www.acmicpc.net/problem/18230


import sys
from collections import deque

# 입력 받기
N, A, B = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# 예쁨 내림차순 정렬
a = deque(sorted(a, reverse=True))
b = deque(sorted(b, reverse=True))
total = 0


# 홀수인 경우 1칸 타일 1개 사용
if N % 2 == 1:
    total += a[0]
    a.popleft()
    N -= 1

# 이후에는 (1칸 타일 2개) (2칸 타일 1개) 중 큰 것 사용
for _ in range(0, N, 2):
    t1, t2 = 0, 0
    if len(a) >= 2:
        t1 = a[0] + a[1]
    if len(b) >= 1:
        t2 = b[0]
    
    if t1 > t2:
        total += t1
        a.popleft()
        a.popleft()
    else:
        total += t2
        b.popleft()
print(total)