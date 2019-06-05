import fractions
import functools
from functools import reduce


def shift(index: int, l: list) -> list:
    return l[index:] + l[:index]


def not_see_one(index: int, a: list) -> iter:
    ret = shift(index, a)
    return ret[1:]


def gcd_list(numbers: list) -> int:
    return reduce(fractions.gcd, numbers)


n = int(input())
a_list = list(map(int, input().split()))

result = max(map(gcd_list, map(functools.partial(not_see_one, a=a_list), range(n))))
print(result)
