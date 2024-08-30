# 18352. 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352


import sys
from collections import deque

# 입력 받기
N, M, K, X = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)

# 최단거리 모두 -1로 초기화
dist = [-1] * (N+1)
dist[X] = 0

# BFS로 탐색하면서 X -> 각 도시로의 최단거리 계산
q = deque([X])
while q:
    now = q.popleft()
    for x in arr[now]:
        if dist[x] == -1:
            dist[x] = dist[now] + 1
            q.append(x)

# 최단거리가 K인 도시 출력
if K not in dist:
    print(-1)
else:
    for i in range(N+1):
        if dist[i] == K:
            print(i)