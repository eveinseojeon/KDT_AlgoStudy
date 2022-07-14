import math
import string
tmp = string.digits+string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):  # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True


def solution(n, k):
    x = convert(n, k)
    x = str(x)
    x = list(x.split('0'))

    answer = 0
    for y in x:
        if y != '1' and y != '':
            if is_prime_num(int(y)) == True:
                answer += 1
    return answer
