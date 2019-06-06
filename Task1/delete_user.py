from Task1 import user_repository
import sys

try:
    input_id = int(input("ユーザIDを入力してください："))
    user_rep = user_repository.UserRepository()
    key_user = user_rep.get_user_by_id(input_id)
    user_rep.remove_user_from_csv(key_user)
#except ValueError:
 #   print("ユーザIDには整数を入力してください。")
  #  sys.exit()
except IndexError:
    print("指定されたIDのユーザは存在しません。")
    sys.exit()
except FileNotFoundError:
    print("User.csvファイルが見つかりません。")
