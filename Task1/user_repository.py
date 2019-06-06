from Task1 import user_module
from functools import reduce
import sys


class UserRepository:

    HEADER = "id,name,mail,phone_number\n"

    def __init__(self):
        try:
            f = open("User.csv", "r", encoding="utf_8")
            f.__next__()
            lines = f.readlines()
            f.close()
            self.__users_list = list(map(self.string_to_object, lines))
        except FileNotFoundError:
            print("User.csvファイルが存在しません。")
            sys.exit()
        except IOError:
            print("ファイルの読み込みに失敗しました。")
            sys.exit()

    def add_user(self, name: str, mail: str, phone_number: int):
        """
        :param name: 追加するユーザ名
        :param mail: 追加するユーザのメールアドレス
        :param phone_number: 追加するユーザの電話番号
        :return: 戻り値なし
        """
        new_id = self.get_new_id()
        user = user_module.User(new_id, name, mail, phone_number)
        self.__users_list.append(user)

    def get_new_id(self) -> int:
        """
        :return: いままで使われていないid番号
        """
        line_count = len(self.__users_list)
        now_max_id = self.__users_list[line_count - 1].id_num if line_count != 0 else 0
        new_id = now_max_id + 1
        return new_id

    def get_user_by_id(self, key_id: int) -> user_module.User:
        """
        :param key_id: 取得したいUserインスタンスのID
        :return: 取得したUserインスタンス
        """
        try:
            result = list(filter(lambda x: x.id_num == key_id, self.__users_list))
            return result[0]
        except IndexError:
            print("そのIDのユーザは存在しません。")
            sys.exit()

    def write_csv(self):
        """
        :return: 戻り値なし
        """
        try:
            users_string_list = map(self.object_to_string, self.__users_list)
            users_string = reduce(lambda x, y: x + y, users_string_list)
            f = open("User.csv", "w", encoding="utf_8")
            f.write(self.HEADER)
            f.write(users_string)
            f.close()
        except IOError:
            print("ファイルの書き込みに失敗しました。")
            sys.exit()

    def output_one_user(self, key_id: int):
        """
        :param key_id: コンソールに出力するユーザインスタンス
        :return: 戻り値なし
        """
        user = self.get_user_by_id(key_id)
        print("ID:{}".format(user.id_num))
        print("名前:{}".format(user.name))
        print("メールアドレス:{}".format(user.mail))
        print("電話番号:{}".format(user.phone_number))

    @staticmethod
    def string_to_object(line: str) -> user_module.User:
        """
        :param line: カンマ区切りのユーザパラメータ文字列
        :return: 読み込んだ結果のユーザインスタンス
        """
        user_param_list = line.rstrip("\n").split(",")
        user_id = int(user_param_list[0])
        name = user_param_list[1]
        mail = user_param_list[2]
        phone_number = int(user_param_list[3])
        user = user_module.User(user_id, name, mail, phone_number)
        return user

    @staticmethod
    def object_to_string(user: user_module.User) -> str:
        """
        :param user: 文字列にしたいユーザインスタンス
        :return: カンマ区切りのユーザパラメータ文字列
        """
        return "{},{},{},{}\n".format(user.id_num, user.name, user.mail, user.phone_number)
