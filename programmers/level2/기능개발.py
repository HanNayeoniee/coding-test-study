# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    # 각 기능이 며칠 후에 배포되는지 계산
    days = []
    for p, s in zip(progresses, speeds):
        day, remain = divmod(100-p, s)
        if remain != 0:
            day += 1
        days.append(day)

    i = 1
    answer = []
    while True:
        flag = days[0]
        if len(days) > i and days[i] <= flag:
            i += 1
        elif len(days) > i and days[i] > flag:
            answer.append(i)
            days = days[i:]
            i = 1
        else:
            answer.append(i)
            break
    
    return answer
    
    
progresses = [93, 30, 55]
speeds = [1, 30, 5]
answer = solution(progresses, speeds)
print(answer)