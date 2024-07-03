# 2810. 컵홀더
# https://www.acmicpc.net/problem/2810

from collections import deque

N = int(input())
s = deque(list(input()))

cnt = 1
while s:
    seat = s.pop()
    if seat == 'S':
        cnt += 1
    else:
        s.pop()
        cnt += 1
print(min(cnt, N))