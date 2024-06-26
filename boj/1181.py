# 단어 정렬
# https://www.acmicpc.net/problem/1181

import sys

def sol1():
    """
    내 풀이
    """
    # 단어 입력 받기
    N = int(sys.stdin.readline())
    arr = [sys.stdin.readline().strip() for _ in range(N)]

    # 중복된 단어 삭제
    arr = list(set(arr))
    
    # 1) 단어 길이, 2) 단어 사전순으로 정렬
    arr.sort(key=lambda x: (len(x), x))
    for word in arr:
        print(word)