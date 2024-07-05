# 2828. 사과 담기 게임
# https://www.acmicpc.net/problem/2828


import sys

N, M = map(int, sys.stdin.readline().split())
num = int(sys.stdin.readline())
left, right = 1, M
total = 0

for _ in range(num):
    target = int(sys.stdin.readline())
    # 사과가 바구니 범위 안에있는 경우
    if left<=target and target<=right:
        continue
    # 사과가 바구니 오른쪽에 떨어지는 경우
    elif target > right:
        diff = target - right
        total += diff
        left, right = left+diff, right+diff
    # 사과가 바구니 왼쪽에 떨어지는 경우
    elif target < left:
        diff = left - target
        total += diff
        left, right = left-diff, right-diff
print(total)