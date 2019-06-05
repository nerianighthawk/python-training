class User:
    def __init__(self, user_id: int, name: str, mail: str, phone_number: int):
        self.__id = user_id
        self.__name = name
        self.__mail = mail
        self.__phone_number = phone_number

    def output(self):
        print("ID:{}".format(self.__id))
        print("名前:{}".format(self.__name))
        print("メールアドレス:{}".format(self.__mail))
        print("電話番号:{}".format(self.__phone_number))

    def write_csv(self):
        with open("User.csv", "a", encoding="utf_8") as f:
            f.write("{},{},{},{}\n".format(self.__id, self.__name, self.__mail, self.__phone_number))


if __name__ == "__main__":
    user = User(0, "test", "test@test.mail", 1234567890)
    user.output()
