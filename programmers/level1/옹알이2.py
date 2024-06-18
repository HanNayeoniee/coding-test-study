# https://school.programmers.co.kr/learn/courses/30/lessons/133499
# 2024.04.18
# 주어진 단어의 앞부터 두글자, 세글자가 옹알이에 포함되고, 이전 단어와 다르면 answer += 1

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        prev = ""
        while b:
            if b[:2] in words and prev != b[:2]:
                prev = b[:2]
                b = b[2:]
            elif b[:3] in words and prev != b[:3]:
                prev = b[:3]
                b = b[3:]
            else:
                break
        if b == "":
            answer += 1
    return answer