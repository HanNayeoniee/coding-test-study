# 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667


import sys

def bfs(i, j):
    q = [(i, j)]
    visited[i][j] = True
    cnt = 0

    while q:
        ci, cj = q.pop()
        cnt += 1

        # 4방향으로 집에 위치하는 곳 탐색
        for di, dj in ((0,1), (0,-1), (1,0), (-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == '1' and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = True
    return cnt


# 지도 입력 받기
N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]  # 집 방문 여부 표시


# 집이 있는 곳 찾아서 탐색 시작
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            cnt = bfs(i, j)
            result.append(cnt)

# 정렬 후 출력
result.sort()
print(len(result))
for res in result:
    print(res)