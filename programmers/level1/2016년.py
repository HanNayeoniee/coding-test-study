# https://school.programmers.co.kr/learn/courses/30/lessons/12901
# 2024.04.16

def solution(a, b):
    month = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    diff = b
    for i in range(a-1):
        diff += month[i+1]  # 1월 1일을 기준으로 a월 b일이 며칠 차이나는지 구하기
    
    answer = (diff-1) % 7  # 7로 나누었을 때 나머지로 금요일을 기준으로 며칠 차이나는지 구하기
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    return days[answer]