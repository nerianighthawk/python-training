from functools import reduce

t = int(input())
n = int(input())
a = list(map(int, input().split(" ")))
m = int(input())
b = list(map(int, input().split(" ")))


def customer(cmr: int) -> bool:
    takoyaki = list(filter(lambda x: x <= cmr <= x + t, a))
    ret = len(takoyaki) > 0
    if ret:
        a.pop(a.index(takoyaki[0]))
    return ret


check = map(customer, b)
result = "yes" if reduce(lambda x, y: x and y, check) else "no"
print(result)
