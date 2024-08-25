# 13164. 행복 유치원
# https://www.acmicpc.net/problem/13164


import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


diff = []
for i in range(N-1):
    diff.append(arr[i+1] - arr[i])

diff.sort()
print(sum(diff[:N-K]))