# https://school.programmers.co.kr/learn/courses/30/lessons/138477
# 2024.04.15

def solution(k, score):
    answer = []
    winner = []
    
    # 점수를 하나씩 순회하면서
    for i, s in enumerate(score):
        # k개 미만인 경우에는 명예의 전당에 무조건 추가
        if i < k:
            winner.append(s)
        else:
            if winner[-1] < s:
                winner.append(s)

        # 내림차순 정렬해 최하점 구하기
        winner = sorted(winner, reverse=True)[:k]
        answer.append(winner[-1])
    
    return answer