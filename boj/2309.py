# 일곱 난쟁이 - brute force
# https://www.acmicpc.net/problem/2309


from itertools import combinations

def sol1():
    """
    break문이 빠져서 틀린 풀이
    """
    heights = []
    for i in range(9):
        heights.append(int(input()))

    combis = combinations(heights, 7)
    for c in combis:
        if sum(c) == 100:
            for num in sorted(c):
                print(num)


def sol2():
    """
    break문 추가해 성공!
    """
    heights = []
    for i in range(9):
        heights.append(int(input()))

    combis = combinations(heights, 7)
    for c in combis:
        if sum(c) == 100:
            for num in sorted(c):
                print(num)
            break


def sol3():
    """
    2번 풀이에서 코드를 더 간결하게, 필수적이지 않은 변수 선언 삭제
    """
    # 9명의 키 정보를 입력받는다.
    heights = [int(input()) for _ in range(9)]

    # 9명 중 7명을 선택하는 모든 경우의 수
    for combi in combinations(heights, 7):
        # 7명 키의 합이 100이 되는 경우
        if sum(combi) == 100:
            # 오름차순 정렬해 한 줄씩 출력
            for num in sorted(combi):
                print(num)
            # 여러 경우의 수가 나올 수 있으므로 종료
            break