from functools import reduce
from functools import partial
from math import floor

ONE_WEEK = 7


def make_day_string(day: int) -> str:
    """
    :param day: 日付
    :return: 日付を文字列にしたもの
    """
    day_string = (
        "    " if day <= 0 else
        " {} ".format(day) if day / 10 >= 1 else
        "  {} ".format(day)
    )
    return day_string


def make_week_string(day: int, day_num: int) -> str:
    """
    :param day: 週末の日付
    :param day_num: 最終日付が来る曜日番号
    :return: 1週間を文字列にしたもの
    """
    week_list = list(map(lambda x: day - x, range(day_num)))
    day_string_list = map(make_day_string, week_list)
    ret = reduce(lambda x, y: y + x, day_string_list)
    return ret


def make_month_string(month: int) -> list:
    """
    :param month: 月番号
    :return: 1ヵ月を文字列にして改行毎にリスト
    """
    days = range(1, days_list[month] + 1)
    initial_day = initial_day_list[month]
    weekend = filter(lambda x: (x + initial_day) % ONE_WEEK == 0, days)
    week_string = list(map(partial(make_week_string, day_num=ONE_WEEK), weekend))
    last_week_day_num = initial_day_list[month + 1]
    week_string_month_end = [make_week_string(days_list[month], last_week_day_num)] if last_week_day_num != 0 else []
    ret = ["{}月".format(month + 1), week] + week_string + week_string_month_end
    return ret


def first_day_of_year(year_num: int) -> int:
    """
    :param year_num: 年数
    :return: 入力の年数の1月1日の曜日番号
    """
    year_num_minus = year_num - 1
    leap = floor(year_num_minus / 4) - floor(year_num_minus / 100) + floor(year_num_minus / 400)
    return (year_num + leap) % 7


year = int(input("西暦を入力してください："))  # 西暦を入力
feb_day = 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28  # 2月の日数を計算
week_of_first_day = first_day_of_year(year)
days_list = [31, feb_day, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 各月の日数
day_sum = map(lambda x: sum(days_list[:x]), range(13))  # その月までの合計日数
initial_day_list = list(map(lambda x: (x + week_of_first_day) % 7, day_sum))  # 上記その月までの合計日数から各月の最初の曜日番号を計算
week = "Sun Mon Tue Wed Thu Fri Sat"  # カレンダーの曜日記載用の文字列
year_string = ["{}年".format(year)]
result_list = year_string + reduce(lambda x, y: x + y, map(make_month_string, range(12)))
result = reduce(lambda x, y: x + "\n" + y, result_list)
print(result)
