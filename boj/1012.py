# 1012. 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys

def bfs(si, sj):
        q = []
        q.append((si, sj))
        v[si][sj] = 1

        while q:
            i, j = q.pop()
            for di, dj in ((0,1), (0,-1), (1,0), (-1,0)):
                ni, nj = i+di, j+dj
                
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj]==0:
                    q.append((ni, nj))
                    v[ni][nj] = 1
        result.append(1)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    v = [[0]*M for _ in range(N)]

    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1
        
    result = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and v[i][j] == 0:
                bfs(i, j)
    print(sum(result))