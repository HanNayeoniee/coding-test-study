# 16937. 두 스티커
# https://www.acmicpc.net/problem/16937

import sys
import itertools

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

# 스티커 크기 입력받기
stickers = []
for _ in range(N):
    h, w = map(int, sys.stdin.readline().split())
    if (h > H and w > W) or (h > W and w > H):
        continue
    stickers.append((h, w))


# 스티커 2개 선택하기
combis = list(itertools.combinations(stickers, 2))
max_area = 0

# 8가지 경우에서 최댓값 구하기
for combi in combis:
    h1, w1 = combi[0][0], combi[0][1]
    h2, w2 = combi[1][0], combi[1][1]
    
    # 가로로 나란히
    if (h1+h2<=W and max(w1,w2)<=H) or (h1+w2<=W and max(w1,h2)<=H) or (w1+h2<=W and max(h1,w2)<=H) or (w1+w2<=W and max(h1,h2)<=H):
        # 최댓값 업데이트
        max_area = max(max_area, w1*h1 + w2*h2)

    # 세로로
    elif (w1+w2<=H and max(h1,h2)<=W) or (w1+h2<=H and max(h1,w2)<=W) or (h1+w2<=H and max(w1,h2)<=W) or (h1+h2<=H and max(w1,w2)<=W):
        # 최댓값 업데이트
        max_area = max(max_area, w1*h1 + w2*h2)

print(max_area)