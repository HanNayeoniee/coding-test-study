# 17204. 죽음의 게임
# https://www.acmicpc.net/problem/17204


import sys

# 입력 받기
N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]


"""
### 첫 번째 풀이 - Recursion Error

def dfs(node):
    global cnt
    cnt += 1
    next_node = arr[node]

    # 0에서 시작해 0으로 돌아오는 사이클만 존재한다고 생각함
    if next_node == 0:
        cnt = -1
        return
    elif next_node == K:
        return
    else:
        dfs(next_node)

cnt = 0
dfs(0)    
print(cnt)
"""

### 두 번째 풀이 - 성공
def dfs(node):
    global cnt
    cnt += 1

    # 이미 방문한 노드이면 사이클
    if v[node]:
        cnt = -1
        return
    else:
        # 방문 표시
        v[node] = 1
        next_node = arr[node]

        # 보성이를 찾으면 종료
        if next_node == K:
            return
        # 보성이를 찾지 못하면 계속 재귀 호출
        else:
            dfs(next_node)

cnt = 0
v = [False] * N
dfs(0)   
print(cnt)