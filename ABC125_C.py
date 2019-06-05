import math
from functools import reduce
import functools


def delete_one(index: int, a: list) -> list:
    return (a[index:] + a[:index])[1:]


def gcd_list(numbers: list) -> int:
    return reduce(math.gcd, numbers)


n = int(input())
a_list = list(map(int, input().split()))

p2 = list(map(functools.partial(delete_one, a=a_list), range(n)))
print(p2)
p1 = list(map(gcd_list, p2))
print(p1)
