# 5212. 지구 온난화
# https://www.acmicpc.net/problem/5212


import sys

# 지도 입력받기
R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]

# 4방향 탐색
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

sink = []  # 잠기게 되는 좌표
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'X':
            cnt = 0

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0<=nr<R and 0<=nc<C:
                    if arr[nr][nc] == '.':
                        cnt += 1
                else:
                    cnt += 1
                    continue
            
            if cnt >= 3:
                sink.append((r, c))

# 잠기는 좌표 바다로 바꾸기
if len(sink) > 0:
    for r, c in sink:
        arr[r][c] = '.'

# 지도 범위 구하기
min_r, max_r, min_c, max_c = 0, 0, C-1, 0

# row 범위 구하기
for r in range(R):
    if 'X' in arr[r]:
        min_r = r
        break
for r in range(R-1, -1, -1):
    if 'X' in arr[r]:
        max_r = r
        break

# column 범위 구하기
for r in range(min_r, max_r+1):
    for c in range(C):
        if arr[r][c] == 'X':
            min_c = min(min_c, c)
            max_c = max(max_c, c)

# 정답 출력하기
for r in range(min_r, max_r+1):
    for c in range(min_c, max_c+1):
        print(arr[r][c], end='')
    print()