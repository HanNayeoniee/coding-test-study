# 1260. DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
import collections

# 노드, 간선 정보 입력받아서 저장
node, edge, start = map(int, sys.stdin.readline().split())
arr = collections.defaultdict(list)
for _ in range(edge):
    n1, n2 = map(int, sys.stdin.readline().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

# 연결된 간선 정보 오름차순 정렬
for i in range(1, node+1):
    arr[i].sort()


def dfs(c):
    ans_dfs.append(c)  # 방문한 노드 표시
    v[c] = 1

    for n in arr[c]:
        if not v[n]:
            dfs(n)
    

def bfs(s):
    q = []
    q.append(s)  # 시작 노드 방문
    ans_bfs.append(s)
    v[s] = 1  # 방문 여부 저장

    while q:
        c = q.pop(0)
        for n in arr[c]:
            if not v[n]:
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1

# DFS 탐색
ans_dfs = []
v = [0] * (node+1)
dfs(start)
print(*ans_dfs)

# BFS 탐색
ans_bfs = []
v = [0] * (node+1)
bfs(start)
print(*ans_bfs)