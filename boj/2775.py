# 2775. 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = [[0] * n for _ in range(k+1)]

    for i in range(k+1):
        for j in range(n):
            if i == 0:
                arr[i][j] = j+1
            elif j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = sum(arr[i-1][:j+1])
    print(arr[k][n-1])