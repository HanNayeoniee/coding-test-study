# 2570. 계단 오르기
# https://www.acmicpc.net/problem/2579

import sys

N = int(sys.stdin.readline())
p = [int(sys.stdin.readline()) for _ in range(N)]

# 계단 개수가 3개 미만인 경우는 모두 밟는 것이 최대값
if N < 3:
    print(sum(p))
else:
    # dp 배열 초기화
    dp = [0] * N
    dp[0] = p[0]
    dp[1] = p[0] + p[1]
    dp[2] = max(p[0]+p[2], p[1]+p[2])

    # 점화식 계산
    for i in range(3, N):
        dp[i] = max(dp[i-3]+p[i-1]+p[i], dp[i-2]+p[i])
    print(dp[-1])