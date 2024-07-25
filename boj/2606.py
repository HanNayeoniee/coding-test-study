# 2606. 바이러스
# https://www.acmicpc.net/problem/2606


import sys
import collections

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

arr = collections.defaultdict(list)
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    arr[n1].append(n2)
    arr[n2].append(n1)


cnt = 0
v = [False] * (N+1)

def dfs(n):
    global cnt
    v[n] = True
    cnt += 1
    for next in arr[n]:
        if not v[next]:
            dfs(next)

dfs(1)
print(cnt-1)