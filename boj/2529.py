# 2529. 부등호
# https://www.acmicpc.net/problem/2529


import sys

def check(num1, num2, sign):
    if sign == "<":
        return num1 < num2
    else:
        return num1 > num2
    
def dfs(idx, num):
    if idx == k+1:
        ans.append(num)
        return
    
    for i in range(10):
        if not visited[i]:
            if idx==0 or check(num[idx-1], str(i), signs[idx-1]):
                visited[i] = True
                dfs(idx+1, num+str(i))
                visited[i] = False

k = int(sys.stdin.readline())
signs = list(sys.stdin.readline().strip().split(" "))

visited = [False] * 10
ans = []
dfs(0, '')

ans.sort()
print(ans[-1])
print(ans[0])