### 최대공약수 구하기
"""
<유클리드 호제법>
숫자 a,b가 있을 때, a를 b로 나눈 나머지와 b의 최대공약수는/ a와 b의 최대공약수와 동일하다.
GCD(a, b) = GCD(b, a%b)
"""

### 풀이1. 반복문 사용
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


### 풀이2. 재귀 사용
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


### 최소공배수 구하기
def lcm(a, b):
    return a*b / gcd(a,b)

a, b = 12, 3
print(gcd(a, b))
print(lcm(a, b))