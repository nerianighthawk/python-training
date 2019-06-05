num_list = [False for i in range(1000000000)]


def turn(num: int) -> bool:
    num_list[num] = not num_list[num]
    return num_list[num]


n: int = int(input())
a: list = []

for i in range(n):
    number = int(input())
    a.append(number)

map(turn, a)
print(len(list(filter(lambda x: x, num_list))))
