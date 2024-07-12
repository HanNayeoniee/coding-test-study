# 1010. 다리 놓기
# https://www.acmicpc.net/problem/1010

import sys

arr = [[0]*30 for _ in range(30)]
T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    for i in range(N):
        for j in range(M):
            if i == j:
                arr[i][j] = 1
            elif i == 0:
                arr[i][j] = j+1
            else:
                arr[i][j] = sum(arr[i-1][:j])
    print(arr[N-1][M-1])