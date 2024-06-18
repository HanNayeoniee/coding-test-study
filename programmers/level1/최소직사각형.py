# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    max_w, max_h = 0, 0
    for w, h in sizes:
        if w > h:
            max_w = max(max_w, w)
            max_h = max(max_h, h)
        else:
            max_w = max(max_w, h)
            max_h = max(max_h, w)
    
    return max_w * max_h