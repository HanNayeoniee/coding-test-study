# https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 2024.04.18
"""
X, Y 각 숫자별로 나타나는 숫자의 개수 세기
개수가 작은 쪽을 기준으로 가장 큰 정수 만들기
"""
def solution(X, Y):
    x, y = {}, {}
    for i in range(10):
        x[str(i)] = X.count(str(i))
    for i in range(10):
        y[str(i)] = Y.count(str(i))
        
    common = []
    for i in range(10):
        idx = str(i)
        min_num = min(x[idx], y[idx])
        if min_num > 0:
            common += [idx] * min_num

    if not common:
        return "-1"
    elif set(common) == {"0"}:
        return "0"
    if common:
        return "".join(sorted(common, reverse=True))


if __name__ == "__main__":
    X = "100"
    Y = "2345"

    X = "100"
    Y = "203045"

    X = "100"
    Y = "123450"
    res = solution(X, Y)
    print(res)