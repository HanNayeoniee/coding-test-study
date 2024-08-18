# 11722. 가장 긴 감소하는 부분 수열
# https://www.acmicpc.net/problem/11722


import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))