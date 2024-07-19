def is_prime(n):
    """
    n까지 확인
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


import math
def is_prime2(n):
    """
    n의 제곱근까지 확인
    math.sqrt(n)은 n의 제곱근
    """
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def is_prime3(n):
    """
    n의 제곱근까지 확인
    n**0.5는 n의 제곱근
    """
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def get_primes(n):
    """
    에라토스테네스의 체 - 1부터 n까지의 수 중 소수 구하기
    """
    a = [False, False] + [True] * (n-1)
    primes = []

    # 첫 번째 i배수는 소수, 그 다음 배수는 합성수이므로 소수가 아님
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

    return primes