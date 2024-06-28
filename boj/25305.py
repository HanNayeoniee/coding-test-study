# 25305. 커트라인
# https://www.acmicpc.net/problem/25305

import sys

N, k = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))
print(sorted(scores, reverse=True)[k-1])