import sys
import bisect


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    b.sort()

    c = []
    for i in range(N):
        idx = bisect.bisect_left(b, a[i])

        # 맨 앞, 뒤에 삽입하는 경우
        if idx == 0:
            c.append(b[0])
        elif idx == len(b):
            c.append(b[-1])
        # 중간에 삽입하는 경우에는 차이가 작은 숫자 찾기
        else:
            diff1 = abs(a[i]-b[idx])
            diff2 = abs(a[i]-b[idx-1])

            if diff1 < diff2:
                c.append(b[idx])
            else:
                c.append(b[idx-1])
                    
    print(sum(c))