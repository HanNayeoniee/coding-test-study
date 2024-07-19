
"""
선택정렬 결과
i: 0, arr: [3, 6, 7, 9, 5]
i: 1, arr: [3, 5, 7, 9, 6]
i: 2, arr: [3, 5, 6, 9, 7]
i: 3, arr: [3, 5, 6, 7, 9]
i: 4, arr: [3, 5, 6, 7, 9]
res: [3, 5, 6, 7, 9]
"""

def selection_sort(arr):
    """
    선택정렬
    매번 가장 작은 숫자를 선택할 때 min(), index() 내장함수 사용
    min()의 사간복잡도: O(N)
    index()의 사간복잡도: O(1)
    """
    for i in range(len(arr)):
        min_num = min(arr[i:])
        min_idx = arr[i:].index(min_num) + i

        if arr[i] > min_num:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
        print(f'i: {i}, arr: {arr}')


def selection_sort2(arr):
    """
    선택정렬
    이중 for문을 돌며 최솟값을 찾기 때문에 전체 시간복잡도는 O(N^2)
    """
    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        if arr[i] > arr[min_idx]:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f'i: {i}, arr: {arr}')

"""
삽입정렬 결과
arr = [3, 7, 2, 5, 1, 4]
i: 1, arr: [3, 7, 2, 5, 1, 4]
i: 2, arr: [2, 3, 7, 5, 1, 4]
i: 3, arr: [2, 3, 5, 7, 1, 4]
i: 4, arr: [1, 2, 3, 5, 7, 4]
i: 5, arr: [1, 2, 3, 4, 5, 7]
res: [1, 2, 3, 4, 5, 7]
"""
def insertion_sort(arr):
    """
    삽입정렬 - 내 풀이
    """
    for i in range(1, len(arr)):
        target = arr[i]
        min_idx = i-1  # 왼쪽에서 자신보다 작은 숫자의 인덱스

        # 이미 정렬되어있는 경우
        if arr[i-1] < arr[i]:
            continue
        
        # 왼쪽에서 target보다 작은 숫자의 위치 찾기
        for j in range(i-1, -2, -1):
            # 자기 자신이 가장 작은 경우
            if j == -1:
                min_idx = -1
            # 더 작은 숫자를 찾은 경우 종료
            elif arr[j] < target:
                min_idx = j
                break

        # 찾은 min_idx의 뒤부터 1칸씩 오른쪽으로 이동
        for k in range(i, min_idx, -1):
            arr[k] = arr[k-1]
        arr[min_idx+1] = target
        print(f'i: {i}, min_idx: {min_idx}, arr: {arr}')


def insertion_sort2(arr):
    """
    삽입정렬 - 정답 풀이
    시간복잡도: O(N^2)
    """
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        print(f'i: {i}, arr: {arr}')


def bubble_sort(arr):
    """
    버블정렬
    시간복잡도: O(N^2)
    """
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f'i: {i}, arr: {arr}')


def quick_sort(arr):
    """
    퀵정렬(pivot을 가운데 값으로 설정)
    시간복잡도: O(N*logN)
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    low, high = [], []
    for num in arr:
        if num < pivot:
            low.append(num)
        elif num > pivot:
            high.append(num)

    return quick_sort(low) + [pivot] + quick_sort(high)
