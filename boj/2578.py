# 빙고
# https://www.acmicpc.net/problem/2578


import sys

arr = []
for _ in range(5):
    arr.extend(list(map(int, sys.stdin.readline().split())))

answer = []
for _ in range(5):
    answer.extend(list(map(int, sys.stdin.readline().split())))


# 빙고 개수 세기
def check(arr):
    cnt = 0
    
    # 가로
    for i in range(5):
        if sum(arr[i]) == 5:
            cnt += 1
    
    # 세로
    for i in range(5):
        if sum(list(zip(*arr))[i]) == 5:
            cnt += 1
    
    # 대각선
    total1, total2 = 0, 0
    for i in range(5):
        total1 += arr[i][i]
        total2 += arr[i][4-i]
    if total1 == 5:
        cnt += 1
    if total2 == 5:
        cnt += 1


v = [[0,0,0,0,0] for _ in range(5)]

for idx, num in enumerate(answer):
    # 사회자가 부른 숫자 방문 표시
    real_idx = arr.index(num)
    i = real_idx // 5
    j = real_idx % 5
    v[i][j] = 1
    

    cnt = check(v)
    if cnt >= 3:
        print(idx+1)
        break
