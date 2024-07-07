# 1920. 수 찾기
# https://www.acmicpc.net/problem/1920


import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))

### 반복문으로 이분탐색 구현
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start+end) // 2
        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

nums.sort()
for target in nums2:
    ans = binary_search(nums, target)
    print(ans)
