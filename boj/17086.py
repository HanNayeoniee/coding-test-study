# 17086. 아기 상어2
# https://www.acmicpc.net/problem/17086


import sys
import itertools

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(i, j):
    global q

    while q:
        ci, cj = q.pop()

        for k in range(8):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                arr[ni][nj] = arr[i][j] + 1

# 문제 입력받기
N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    arr.append(line)


target = 1
q = []
while True:
    if 0 in list(itertools.chain(*arr)):
        for i in range(N):
            for j in range(M):
                if arr[i][j] == target:
                    q.append((i, j))

        si, sj = q[0][0], q[0][1]
        bfs(si, sj)
        print(f'target: {target}')
        print(arr)
        target += 1
    else:
        break

print(max(list(itertools.chain(*arr))) - 1)