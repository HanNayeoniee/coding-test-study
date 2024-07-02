# 5585. 거스름돈
# https://www.acmicpc.net/problem/5585

price = int(input())  # 물건 금액
result = 0  # 거스름돈 개수
change = 1000 - price  # 거스름돈 금액

while change:
    for coin in [500, 100, 50, 10, 5, 1]:
        cnt, remain = divmod(change, coin)
        if cnt > 0:
            result += cnt
            change = remain
print(result)