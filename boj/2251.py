# 2251. 물통
# https://www.acmicpc.net/problem/2251

import sys


def pour(a, b, c, src):
    global res
    global q

    if src == 'a':
        # a -> c
        diff = min(a, C-c)
        new1 = (a-diff, b, c+diff)
        # a -> b
        diff = min(a, B-b)
        new2 = (a-diff, b+diff, c)
    elif src == 'b':
        # b -> a
        diff = min(b, A-a)
        new1 = (a+diff, b-diff, c)
        # b -> c
        diff = min(b, C-c)
        new2 = (a, b-diff, c+diff)
    elif src == 'c':
        # c -> a
        diff = min(c, A-a)
        new1 = (a+diff, b, c-diff)
        # c -> b
        diff = min(c, B-b)
        new2 = (a, b+diff, c-diff)

    # 중복되지 않는 조합이면 추가
    if new1 not in res:
        res.append(new1)
        q.append(new1)
    if new2 not in res:
        res.append(new2)
        q.append(new2)


def bfs():
    global res
    global q

    while q:
        now = q.pop()
        a, b, c = now[0], now[1], now[2]

        # 물 붓기
        if a > 0:
            pour(a, b, c, "a")
        if b > 0:
            pour(a, b, c, "b")
        if c > 0:
            pour(a, b, c, "c")


A, B, C = map(int, sys.stdin.readline().split())
res = [(0, 0, C)]
q = [(0, 0, C)]
bfs()

# 정답 출력
answer = [r[2] for r in res if r[0]==0]
answer.sort()
print(*answer)