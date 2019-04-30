x = [[i for i in range(100)] for j in range(10001)]


def next_array(t):
    """
    :type t: int
    :rtype: List[float]
    """
    x[t] = list(map(lambda i: (x[t-1][(i - 1) % 100] + x[t-1][(i + 1) % 100]) / 2, range(100)))
    return x[t]


result = list(map(next_array, range(1, 10001)))
print(x[10000])
