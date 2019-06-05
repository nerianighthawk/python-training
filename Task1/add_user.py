from Task1 import user_module
import sys


def get_new_id() -> int:
    with open("User.csv", "r", encoding="utf_8") as f:
        new_id = len(f.readlines())
        return new_id


try:
    name = input("名前を入力してください：")
    mail = input("メールアドレスを入力してください：")
    phone_number = int(input("電話番号を入力してください："))
    user_id = get_new_id()
    user = user_module.User(user_id, name, mail, phone_number)
    user.write_csv()
except ValueError:
    print("電話番号には数値を入力してください。")
    sys.exit()
except FileNotFoundError:
    print("User.csvファイルが見つかりません。")
    sys.exit()
