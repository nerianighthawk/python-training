mod = filter(lambda x: x % 3 == 1, range(1, 10))
result = list(map(lambda x: x * 2, mod))
print(result)
