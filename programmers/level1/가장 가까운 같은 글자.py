# https://school.programmers.co.kr/learn/courses/30/lessons/142086

from collections import defaultdict

def solution(s):
    answer = []
    
    vocab = defaultdict(int)  # 같은 문자 위치 저장
    for idx, char in enumerate(s):
        if char not in vocab:
            answer.append(-1)
        else:
            answer.append(idx - vocab[char])
        vocab[char] = idx  # 같은 문자 위치를 가장 가깝도롣 업데이트
    
    return answer