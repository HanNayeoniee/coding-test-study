# https://school.programmers.co.kr/learn/courses/30/lessons/131705

from itertools import combinations

def solution(number):
    combis = list(combinations(number, 3))
    result = [c for c in combis if sum(c) == 0]
    
    return len(result)