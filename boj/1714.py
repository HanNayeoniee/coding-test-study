# 1713. 후보 추천하기
# https://www.acmicpc.net/problem/1713


import sys
from collections import defaultdict

# 입력 받기
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

frame = defaultdict(list)  # 사진틀은 {숫자: [추천 횟수, 사진틀에 올라간 시점]} 형태로 저장

for i, num in enumerate(arr):
    if num in frame:
        frame[num][0] += 1
    else:
        element = [1, i]

        if len(frame) == N:
            # 추천 횟수 > 사진틀에 올라간 시점 우선순위로 정렬
            frame_sorted = sorted(frame.items(), key=lambda x: (x[1][0], x[1][1]))
            del_idx = frame_sorted[0][0]
            del frame[del_idx]  # 첫 번째 요소 삭제
        frame[num] = element

print(*sorted(frame.keys()))