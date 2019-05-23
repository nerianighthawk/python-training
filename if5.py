age = int(input("年齢を入力してください: "))
message = ("正の整数を入力してください" if age < 0 else
           "無料です" if age < 3 else
           "200円です" if age < 13 else
           "400円です" if age < 65 else
           "無料です")
print(message)
