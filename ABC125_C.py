import math
from functools import reduce
import functools


def delete_one(index: int, a: list) -> list:
    del a[index]
    return a


def gcd_list(numbers: list) -> int:
    return reduce(math.gcd, numbers)


n = int(input())
a_list = list(map(int, input().split()))

p = list(map(gcd_list, map(functools.partial(delete_one, a=a_list), range(n))))
print(p)
