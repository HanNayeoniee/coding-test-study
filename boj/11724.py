# 11724. 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
from collections import defaultdict

# 파이썬의 재귀 최대 깊이는 기본 설정이 1000회 이기 때문에 늘려줘야 함
sys.setrecursionlimit(10**6)


# 그래프 정보 저장
arr = defaultdict(list)
N, M = map(int, sys.stdin.readline().split())
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    arr[n1].append(n2)
    arr[n2].append(n1)


cnt = 0
v = [False] * (N+1)
start = 0

def dfs(n):
    v[n] = True
    for next in arr[n]:
        if not v[next]:
            dfs(next)

# 아직 방문하지 않은 노드이면 연결된 노드를 모두 방문
for start in range(1, N+1):
    if not v[start]:
        dfs(start)
        cnt += 1  # 연결 요소 호출이 끝나면 개수 1 증가
print(cnt)