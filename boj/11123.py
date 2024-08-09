# 11123. 양 한마리... 양 두마리...
# https://www.acmicpc.net/problem/11123


import sys

def bfs(i, j):
    global cnt
    q = [(i, j)]
    visited[i][j] = True

    # 4방향으로 탐색하면서 아직 방문하지 않은 곳에 양이 있으면 q에 추가하기
    while q:
        ci, cj = q.pop()
        for di, dj in ((0,1), (0,-1), (1,0), (-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<H and 0<=nj<W and not visited[ni][nj] and arr[ni][nj]=="#":
                q.append((ni, nj))
                visited[ni][nj] = True


T = int(sys.stdin.readline())
for _ in range(T):
    # 문제 입력받기
    H, W = map(int, sys.stdin.readline().split())
    arr = []
    for h in range(H):
        arr.append(list(sys.stdin.readline()))   


    cnt = 0
    visited = [[False]*W for _ in range(H)]

    # 양이 위치한 부분에서 탐색 시작
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)