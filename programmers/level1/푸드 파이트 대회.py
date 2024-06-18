# https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 2024.04.15
# (칼로리가 낮은 순서대로, 가진 개수//2 배치) 문자열을 만들고 뒤집어서 붙이기

def solution(food):
    answer = ''
    for i, f in enumerate(food):
        if f//2 > 0:
            answer += str(i) * (f//2)
    
    return answer + '0' + answer[::-1]