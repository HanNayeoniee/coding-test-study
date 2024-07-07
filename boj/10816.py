# 10816. 숫자 카드 2
# https://www.acmicpc.net/problem/10816


import sys
from bisect import bisect_left, bisect_right

def count_by_range(arr, right, left):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx


N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cards.sort()
for i in range(M):
    cnt = count_by_range(cards, nums[i], nums[i])
    print(cnt, end=' ')