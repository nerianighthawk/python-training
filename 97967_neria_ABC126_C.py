import math
import functools


def probability(a: int, b: int) -> int:
    return 0.5 ** math.ceil(math.log2(b) - math.log2(a)) if a < b else 1


input_str = input().split()
n = int(input_str[0])
k = int(input_str[1])
result = sum(map(functools.partial(probability, b=k), range(1, n + 1))) / n
print(result)
