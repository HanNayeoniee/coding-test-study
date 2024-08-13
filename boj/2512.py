# 2512. 예산
# https://www.acmicpc.net/problem/2512


import sys
import bisect


def binary_search(arr, limit):
    global max_total

    start = 0
    end = len(arr) - 1

    while True:
        mid = (start+end) // 2
        idx = bisect.bisect_left(nums, arr[mid])
        total = sum(nums[:idx]) + arr[mid] * (N-idx)  # 상한액 이하에서 각 지방의 예산요청 총합 구하기

        # 예산요청액 > 예산 이면 상한액 줄이기
        if total > limit:
            end = mid - 1
        else:
            # 전체 요청액이 늘어나면 업데이트
            if max_total < total:
                max_total = total
                start = mid + 1
            # 더 이상 늘어나지 않으면 탐색 종료
            else:
                return arr[mid]


# 입력 받기
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
limit = int(sys.stdin.readline())
nums.sort()

# 가능한 상한액을 리스트로 만들어 저장
flags = [i for i in range(1, max(nums)+1)]
max_total = 0


# 최대 상한액 구하기
ans = 0
# 예산요청의 총 합보다 국가예산이 큰 경우
if sum(nums) <= limit:
    ans = max(nums)  # O(N)
else:
    ans = binary_search(flags, limit)
print(ans)