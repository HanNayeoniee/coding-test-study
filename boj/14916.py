# 14916. 거스름돈
# https://www.acmicpc.net/problem/14916

import sys

price = int(sys.stdin.readline())
coin5, remain = divmod(price, 5)

# 5의 배수인 경우
if remain == 0:
    print(coin5)
else:
    # 5원짜리 동전 개수를 1개씩 줄여가면서 거스름돈을 만들 수 있는지 확인
    while True:
        coin2, remain = divmod(price-(coin5*5), 2)
        # 가진 동전으로 잔돈을 줄 수 없는 경우
        if coin5 == 0 and remain != 0:
            print(-1)
            break
        # 거스름돈을 만들 수 있는 경우
        elif remain == 0:
            print(coin5 + coin2)
            break
        else:
            coin5 = coin5 - 1