# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 2024.04.15

from itertools import combinations

def solution(numbers):
    answer = []
    
    combis = list(combinations(numbers, 2))  # 주어진 숫자 중 2개를 고르는 모든 조합
    for n1, n2 in combis:
        answer.append(n1+n2)
    answer = sorted(list(set(answer)))  # 중복 제거 후 오름차순 정렬
    
    return answer