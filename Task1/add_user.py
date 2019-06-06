from Task1 import user_repository
import sys

try:
    name = input("名前を入力してください：")
    mail = input("メールアドレスを入力してください：")
    phone_number = int(input("電話番号を入力してください："))
    user_rep = user_repository.UserRepository()
    user_rep.add_user(name, mail, phone_number)
    user_rep.write_csv()
except ValueError:
    print("電話番号には数値を入力してください。")
    sys.exit()
except FileNotFoundError:
    print("User.csvファイルが見つかりません。")
    sys.exit()
