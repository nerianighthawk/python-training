# Python 開発環境構築

## Python のインストール
下記リンクより Python のインストーラをダウンロードできます。  
https://www.python.org/downloads/release/python-373/
（Python3 安定板最新リリース 3.7.3）  
Files の中から自分の環境に適したインストーラをダウンロード

- Windows 64bit の場合  
Windows x86-64 executable installer
- Windows 32bit 場合  
Windows x86 executable installer

インストーラを起動します。  
インストーラの最初の画面にて下部にある "**Add Python 3.x to PATH**" の項目にチェックを入れます（チェックを入れ忘れても、あとで PATH の設定は行うことができます）。  
"**Install Now**" を実行してインストールします。

## PyCharm のインストール
下記リンクより PyCharm のインストーラをダウンロードできます。  
https://www.jetbrains.com/pycharm/download/#section=windows  
Community 版で大丈夫です。  

インストーラを起動します。  
基本的に "next" と "install" を押していれば大丈夫です。  
Windows 32bit 版を使っている場合は "**Download and install JRE x86 by JetBrains**" の項目にチェックを入れてください。

# Python での開発について

## 実行時エラーが起きる理由
言語によらず、バグを作り込んでしまう理由として、開発者が変数の中身を勘違いしているという例が多く挙げられます。特に、チームでの開発では、他人が作ったソースコードを修正し、影響範囲を勘違いしたまま修正完了にしてしまう場合が多いです。  
上記のような状況を作らないために、意識すべきことがいくつかあります。

## 全員に意識して欲しいこと
全員に意識して欲しいこととして、以下の2つが挙げられます。

### 1. 変数の再代入をしない。  
変数の再代入をすると、当然その変数の中身が変わってしまいます。例えば以下のようなコードです。  
```Python
from datetime import datetime
import time
execTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(execTime)
time.sleep(10)
execTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(execTime)
```
上記は現在時刻を出力して、10秒待った後再度現在時刻を出力するコードです。  
短いコードなので気にならないかもしれませんが、長いコードでこういったことをすると後から見た人はその変数に今何が入っているのかを考えながら修正する必要が出てきます。  
以下のような書き方をすることで回避することが可能です。
```Python
from datetime import datetime
import time
startTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(startTime)
time.sleep(10)
endTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(endTime)
```
上記のように変数の再代入が行われないように意識して書かれた実装を "**イミュータブルな実装**" と呼びます。

### 2. 関数を定義する場合は型アノテーションを記載する。

Python は動的型付け言語で、型を記載する必要がありません。  
ローカル変数等を用意する際は型の意識無しに書けるので非常に便利です（イミュータブルな実装が前提となります）が、関数を定義する際は少し厄介な現象が起きます。  
例えば以下のようなコードです。
```Python
def concat(a, b):
    return a + b


hello = "Hello "
world = "World"
print(concat(hello, world))
two = 2
three = 3
print(concat(two, three))
```
上記コードの実行結果は以下の通りです。
```
Hello World
5
```
`concat` という名前は一般的には文字列結合をイメージするのに対して、下の方の実行結果は足し算の結果になってしまっています。  
チームで開発をしていると、関数を定義した人と使う人が異なるということが多々あります。  
上記のように型指定がないと、自分の使い方が正しいのかどうかわからず、定義した人に確認する必要が出てきます。
以下のように型アノテーションをつけることによって、後からその関数を使う人でも読むだけで使い方が理解できます。
```Python
def concat(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    return a + b


hello = "Hello "
world = "World"
print(concat(hello, world))
```

## PyCharm を使う理由

全員に意識して欲しいこととして、"変数の再代入をしない。" と "関数を定義する場合は型アノテーションを記載する。" の2つを挙げましたが、PyCharm での開発を行うことで PyCharm 側が静的解析を実施し、忠告を出してくれます。  
PyCharm の忠告文に従った開発をするだけで、実行時エラーが減るわけです。

## 余裕がある人は実践してみて欲しい事

余裕がある人は変数のスコープを意識してみましょう。  
変数のスコープとは、定義した変数を参照することができる範囲のことを言います。
```Python
data = [0, 1, 1, 0, 1]
count = 0

for val in data:
    if val == 0:
        count += 1
        result = count

print(result)
```
上記のコードは `data` の中の 0 の数を数えるコードですが、`count` や `result` という変数が違う階層で扱われ、結果が上書きされています。Pythonにおいて、`for` や `if` はスコープを作らないため、見た目ではネストされ階層が下がっていても扱えてしまうわけです。  
これもまたチームでの開発では厄介な仕様です。変数の変化を階層が違う部分まで意識して修正を行うのは大変なことです。  
上記コードは `filter` という関数を使うことで、下記のように書くことができます。
```Python
data = [0, 1, 1, 0, 1]
result = list(filter(lambda x: x == 0, data))
print(len(result))
```
たまたま `filter` という関数がうまく当てはまっただけのように見えますが、では次のような例も考えてみましょう。
```Python
result = []
for val in range(1, 10):
    if val % 3 == 1:
        result += [val * 2]

print(result)
```
上記コードでは1から10の数の中で3で割った余りが1のものを2倍して配列に加え、最後に結果の配列を出力します。こちらは以下のように記述できます。
```Python
mod = filter(lambda x: x % 3 == 1, range(1, 10))
result = list(map(lambda x: x * 2, mod))
print(result)
```
前回と同様に、3で割って1余る数は`filter`によって抽出できます。  
また、`map`という関数を使うことによって、配列の全ての数を2倍する処理を実装することができます。  
この2つの関数の組み合わせによって、ほとんどの処理は実装出来てしまいます。  
また、どちらも第一引数は関数であるため、明確なスコープが存在します。そのため、変数の階層を勘違いしてもコンパイルエラーとなり、そのまま放置されるということがありません。  

## 最後に

上記内容をチーム全員が意識して開発を行うと、Python はとても優秀な良い言語です。しかし、こういった意識無しに、各々が動けばいい精神で開発を行ってしまうと、他の人が見てもわからないコードが簡単に出来上がってしまいます。Python で開発を行う場合は上記事項を意識して見てください。
