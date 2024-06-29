# 덩치
# https://www.acmicpc.net/problem/7568

import sys

# 입력 받기
N = int(sys.stdin.readline())
people = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    people.append((x,y))


# arr1보다 arr2가 큰 덩치이면 True를 반환
def check(arr1, arr2):
    return arr1[0] < arr2[0] and arr1[1] < arr2[1]


out = []
for i in range(N):
    cnt = 1
    for j in range(N):
        res = check(people[i], people[j])
        if i != j and check(people[i], people[j]):
            cnt += 1
    
    out.append(cnt)
print(*out)