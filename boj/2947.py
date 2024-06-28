# 2947. 나무 조각
# https://www.acmicpc.net/problem/2947


import sys

nums = list(map(int, sys.stdin.readline().split()))

def bubble_sort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)
    return arr
        

while nums != [1, 2, 3, 4, 5]:
    nums = bubble_sort(nums)