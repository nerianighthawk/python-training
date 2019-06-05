from functools import reduce

t = int(input())
n = int(input())
a = list(map(int, input().split(" ")))
m = int(input())
b = list(map(int, input().split(" ")))


def customer(index: int) -> bool:
    """
    :param index: int
    :return: bool
    客ごとに当てはまるたこ焼きを見つけて、bool値を返します。
    """
    takoyaki = list(filter(lambda x: x <= b[index] <= x + t, a))  # filterで当てはまるたこ焼きを抽出
    ret = len(takoyaki) > 0  # たこ焼きが一つでもあればOK
    if ret:
        a.pop(a.index(takoyaki[0]))  # 当てはまったたこ焼きでもっとも時間が小さいものを取り除く
    return ret


check = map(customer, range(m))  # checkは各客に対するたこ焼きを渡せるかのbool値
result = "yes" if reduce(lambda x, y: x and y, check) else "no"
# reduceを使って全てtrueならyes、1つでもfalseならno
print(result)
