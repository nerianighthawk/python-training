from Task1 import user_module
import sys


def get_by_id(key_id: int) -> user_module.User:
    with open("User.csv", "r", encoding="utf_8") as f:
        f.__next__()
        lines = f.readlines()
    user_string = list(filter(lambda x: int(x.split(",")[0]) == key_id, lines))
    user_param_list = user_string[0].rstrip("\n").split(",")
    user_id = int(user_param_list[0])
    name = user_param_list[1]
    mail = user_param_list[2]
    phone_number = int(user_param_list[3])
    user = user_module.User(user_id, name, mail, phone_number)
    return user


try:
    input_id = int(input("ユーザIDを入力してください："))
    key_user = get_by_id(input_id)
    key_user.output()
except ValueError:
    print("ユーザIDには整数を入力してください。")
    sys.exit()
except IndexError:
    print("指定されたIDのユーザは存在しません。")
    sys.exit()
except FileNotFoundError:
    print("User.csvファイルが見つかりません。")
