# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys

# 좌표 입력받기
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x, y = sys.stdin.readline().split()
    arr.append([int(x), int(y)])

# x좌표, y좌표 오름차순 순서대로 정렬
arr.sort(key=lambda x: (x[0], x[1]))

# 출력
for i in range(N):
    print(arr[i][0], arr[i][1])