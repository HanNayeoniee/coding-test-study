# 11725. 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725


### DFS 풀이 ###
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

# 그래프 생성
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 저장
visited = [0] * (N+1)

def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:  # 방문한 적이 없으면
            visited[i] = node  # 해당 노드를 부모 노드로 저장
            dfs(i)


dfs(1)
for i in range(2, N+1):
    print(visited[i])


### BFS 풀이 ###
import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

now = 1
q = deque([1])
parent = [0] * (N+1)
parent[1] = 1

while q:
    now = q.popleft()
    for x in graph[now]:
        if parent[x] == 0:
            parent[x] = now
            q.append(x)

for i in range(2, N+1):
    print(parent[i])