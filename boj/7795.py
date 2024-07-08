# 7795. 먹을 것인가 먹힐 것인가
# https://www.acmicpc.net/problem/7795

import sys
from bisect import bisect_left


T = int(sys.stdin.readline())
cnt_list = []
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a_nums = list(map(int, sys.stdin.readline().split()))
    b_nums = list(map(int, sys.stdin.readline().split()))

    b_nums.sort()  # 탐색 대상 리스트 정렬
    cnt = 0

    # 오름차순을 정렬을 유지하면서 num을 샵입할 수 있는 인덱스 찾기. num과 같은 숫자가 있다면 삽입할 숫자는 기존 숫자보다 왼쪽에 위치한다.
    # num 보다 작은 숫자의 개수 구하기
    for num in a_nums:
        idx = bisect_left(b_nums, num)
        cnt += idx
    cnt_list.append(cnt)

for cnt in cnt_list:
    print(cnt)