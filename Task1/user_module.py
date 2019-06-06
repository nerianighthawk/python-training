class User:
    def __init__(self, user_id: int, name: str, mail: str, phone_number: int):
        self.__id = user_id
        self.__name = name
        self.__mail = mail
        self.__phone_number = phone_number

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_mail(self) -> str:
        return self.__mail

    def get_phone_number(self) -> int:
        return self.__phone_number

    id_num = property(get_id)
    name = property(get_name)
    mail = property(get_mail)
    phone_number = property(get_phone_number)


if __name__ == "__main__":
    user = User(0, "test", "test@test.mail", 1234567890)
    print("ID:{}".format(user.id_num))
    print("名前:{}".format(user.name))
    print("メールアドレス:{}".format(user.mail))
    print("電話番号:{}".format(user.phone_number))
