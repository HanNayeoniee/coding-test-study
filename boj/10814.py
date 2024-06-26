# 나이순 정렬
# https://www.acmicpc.net/problem/10814


import sys
from collections import defaultdict

def sol1():
    N = int(input())
    output = defaultdict(list)

    # (나이, 이름) 입력받아 딕셔너리에 {나이: [이름1, 이름2]} 형태로 저장
    for _ in range(N):
        age, name = sys.stdin.readline().split()
        output[int(age)].append(name)

    # 나이 순서대로 정렬 후 (나이, 이름) 형태로 출력
    for key in sorted(output.items()):
        for i in range(len(key[1])):
            print(key[0], key[1][i])


def sol2():
    # 정답 풀이
    N = int(sys.stdin.readline())
    output = []

    for _ in range(N):
        age, name = sys.stdin.readline().split()
        output.append([age, name])

    output.sort(key=lambda x: x[0])
    for num in output:
        print(num[0], num[1])