import math
import functools


def probability(a: int, b: int) -> int:
    return 0.5 ** math.ceil(math.log2(b / a)) if a < b else 1


input_str = input().split()
n = int(input_str[0])
k = int(input_str[1])
p = list(map(functools.partial(probability, b=k), range(1, n + 1)))
print(p)
result = sum(iter(p)) / n
print(result)
