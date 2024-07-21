# 2644. 촌수계산
# https://www.acmicpc.net/problem/2644

import sys

# 입력 받기
N = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    arr[n1].append(n2)
    arr[n2].append(n1)


def bfs(start, target):
    # 초기화
    q = []
    v = [0] * (N+1)

    # 방문 표시
    q.append(start)
    v[start] = 1

    while q:
        node = q.pop(0)
        if node == target:
            return v[target] - 1
        
        for next_node in arr[node]:
            if not v[next_node]:
                q.append(next_node)
                v[next_node] = v[node] + 1  # 연결된 노드와 촌수를 1씩 늘려가는 형태
    return -1


print(bfs(start, end))