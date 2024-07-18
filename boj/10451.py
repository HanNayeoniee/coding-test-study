# 10451. 순열 사이클
# https://www.acmicpc.net/problem/10451

import sys

def dfs(s):
    v[s] = 1
    next = edge[s]
    if not v[next]:
        dfs(next)


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))    
    edge = {i+1:nums[i] for i in range(N)}

    cnt = 0
    v = [0] * (N+1)

    for i in range(1, N+1):
        if not v[i]:
            dfs(i)
            cnt += 1  # 재귀 호출한 dfs 탐색이 모두 끝나면 사이클 개수 1 증가

    print(cnt)