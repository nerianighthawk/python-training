from Task1 import user_repository
import sys

try:
    input_id = int(input("ユーザIDを入力してください："))
    user_rep = user_repository.UserRepository()
    user_rep.output_one_user(input_id)
except ValueError:
    print("ユーザIDには整数を入力してください。")
    sys.exit()
