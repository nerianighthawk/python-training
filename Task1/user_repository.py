from Task1 import user_module
from functools import reduce


class UserRepository:

    HEADER = "id,name,mail,phone_number\n"

    def __init__(self):
        f = open("User.csv", "r", encoding="utf_8")
        f.__next__()
        lines = f.readlines()
        f.close()
        self.__users_list = list(map(self.string_to_object, lines))

    def add_user(self, name: str, mail: str, phone_number: int):
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

    @staticmethod
    def get_user_by_id(key_id: int) -> user_module.User:
        """
        :param key_id: 取得したいUserインスタンスのID
        :return: 取得したUserインスタンス
        """
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

    def write_csv(self):
        """
        :return: 戻り値なし
        """
        f = open("User.csv", "w", encoding="utf_8")
        f.write(self.HEADER)
        f.close()
        map(self.write_user, self.__users_list)

    @staticmethod
    def output(user: user_module.User):
        """
        :param user: コンソールに出力するユーザインスタンス
        :return: 戻り値なし
        """
        print("ID:{}".format(user.id_num))
        print("名前:{}".format(user.name))
        print("メールアドレス:{}".format(user.mail))
        print("電話番号:{}".format(user.phone_number))

    @staticmethod
    def remove_user_from_csv(user: user_module.User):
        """
        :param user: 削除するユーザインスタンス
        :return: 戻り値なし
        """
        with open("User.csv", "r", encoding="utf_8") as f:
            header = f.readline()
            lines = f.readlines()
        users_string = [header] + list(filter(lambda x: int(x.split(",")[0]) != user.id_num, lines))
        result_string = reduce(lambda x, y: x + y, users_string)
        with open("User.csv", "w", encoding="utf_8"):
            f.write(result_string)

    @staticmethod
    def string_to_object(line: str) -> user_module.User:
        user_param_list = line.rstrip("\n").split(",")
        user_id = int(user_param_list[0])
        name = user_param_list[1]
        mail = user_param_list[2]
        phone_number = int(user_param_list[3])
        user = user_module.User(user_id, name, mail, phone_number)
        return user

    @staticmethod
    def write_user(user: user_module.User):
        f = open("User.csv", "a", encoding="utf_8")
        f.write("{},{},{},{}\n".format(user.id_num, user.name, user.mail, user.phone_number))
        f.close()
