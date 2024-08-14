# 3079. 입국심사
# https://www.acmicpc.net/problem/3079

import sys


### 풀이 1
N, M = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

start = arr[0]
end = arr[-1] * M
ans = float('inf')

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for num in arr:
        cnt += mid // num

    if cnt >= M:
        end = mid - 1
        ans = min(ans, mid)
    else:
        start = mid + 1

print(ans)



### 풀이 2
# 문제 입력
N, M = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

def binary_search():
    start = arr[0]
    end = arr[-1] * M
    ans = float('inf')

    while start <= end:
        mid = (start + end) // 2

        # 주어진 시간으로 심사 가능한 사람 수 구하기
        cnt = 0
        for num in arr:
            cnt += mid // num

        # 모든 사람을 심사했다면 최소 시간 업데이트, 왼쪽 절반 탐색
        if cnt >= M:
            end = mid - 1
            ans = min(ans, mid)
        # 오른쪽 절반 탐색
        else:
            start = mid + 1

    return ans

ans = binary_search()
print(ans)