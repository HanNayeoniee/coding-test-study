# https://school.programmers.co.kr/learn/courses/30/lessons/176963
# 2024.04.16

def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for p in photo:
        answer.append(sum([dic[c] if c in dic else 0 for c in p]))
    
    return answer