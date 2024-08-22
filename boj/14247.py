# 14247. 나무 자르기
# https://www.acmicpc.net/problem/14247


import sys

N = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
speed = list(map(int, sys.stdin.readline().split()))

# 나무 자라는 길이를 기준으로 오름차순 정렬
trees = [[speed[i], tree[i]] for i in range(N)]
trees.sort(key=lambda x: x[0])

total = 0
for i in range(N):
    total += trees[i][1] + trees[i][0] * i
print(total)