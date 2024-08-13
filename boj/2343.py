# 2343. 기타 레슨
# https://www.acmicpc.net/problem/2343


import sys

"""
### 틀린 풀이
def binary_search_1(arr, start, end):
    min_diff = 0

    while start <= end:
        mid = (start + end) // 2
        left = sum(arr[:mid+1])
        right = sum(arr[mid+1:])

        if left*2 == right:
            return mid
        else:
            if min_diff > abs(left - right):
                if left*2 < right:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                return mid

def binary_search_2(arr, start, end):
    min_diff = 0

    while start <= end:
        mid = (start + end) // 2
        left = sum(arr[:mid+1])
        right = sum(arr[mid+1:])

        if left == right:
            return mid
        else:
            if min_diff > abs(left-right):
                if left < right:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                return mid

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 이분 탐색
idx1 = binary_search_1(arr, 0, len(arr)-1)
idx2 = binary_search_2(arr, idx1+1, len(arr)-1)
print(max(sum(arr[:idx1+1]), sum(arr[idx1+1:idx2+1]), sum(arr[idx2+1:])))
"""


# 입력 받기
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

N, M = 5, 2
arr = [1, 1, 1, 1, 100]

answer = 0
start, end = max(arr), sum(arr)
while start <= end:
    mid = (start + end) // 2
    
    # 블루레이에 강의 넣기
    cnt, total = 0, 0
    for i in range(N):
        if total + arr[i] > mid:
            cnt += 1  # 다음 블루레이에 넣기
            total = 0  # 현재 블루레이에 저장한 동영상 초기화        
        total += arr[i]
    
    # 일단 하나 사용했으므로
    if total:
        cnt += 1

    # 블루레이 개수가 더 필요하면 기준값을 늘린다.
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)