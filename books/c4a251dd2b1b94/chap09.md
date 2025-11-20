---
title: "第9章: 関数を使ってみよう"
---

# Pythonで関数を使ってみよう

今回は、関数について学びます。
関数を使う事で、特定の処理を使い回すことができるようになります。

## 関数を使ってみる

"def"文を使う事で、関数を定義することができます。
関数は、定義した後、それを"実行"する必要があります。

```python:関数
def 関数名():
    """ 関数の説明 """
    処理

# 関数を実行する
関数名()
```

次の例では、"say_hello"関数を定義し、それを実行するまでの記述例です。

```python:main.py
# 関数を定義する
def say_hello():
    """ 挨拶をする関数 """
    print("Hello, Python!!")

# 関数を実行する
say_hello() # Hello, Python!!

# 定義された関数は、好きなだけ実行できます
say_hello() # Hello, Python!!
say_hello() # Hello, Python!!
say_hello() # Hello, Python!!
```

### 引数を使う

"引数"を使う事で、より柔軟な関数を作ることができます。

```python:引数がある関数
def 関数名(引数):
    """ 関数の説明 """
    処理
```

```python:main.py
# 関数を定義する(引数を1つ用意)
def say_hello(lang):
    """ 挨拶を好きな言語にする関数 """
    print("Hello, " + lang + "!!")

# 関数を実行する
say_hello("Python") # Hello, Python!!

# 色々な言語で挨拶をしてみる
say_hello("Rust") # Hello, Rust!!
say_hello("Kotlin") # Hello, Kotlin!!
say_hello("Swift") # Hello, Swift!!
```

### 引数を複数使う

"引数"は、好きな数だけ定義することができます。

```python:引数が複数ある関数
def 関数名(引数1, 引数2, 引数3, ...):
    """ 関数の説明 """
    処理
```

```python:main.py
# 関数を定義する(引数を2つ用意)
def say_hello(greet, lang):
    """ 好きな挨拶を、好きな言語にする関数 """
    print(greet + ", " + lang + "!!")

# 関数を実行する
say_hello("Hello", "Python") # Hello, Python!!

# 色々な言語で挨拶をしてみる
say_hello("Chao", "C/C++") # Chao, C/C++!!
say_hello("Bonjour", "Java") # Bonjour, Java!!
say_hello("Namaste", "JavaScript") # Namaste, JavaScript!!
```

### 返り値を使う

"return"を使う事で、関数に何かしらの複雑な処理をさせ、その結果を返させることができます。
"return"を書かない関数は、"返り値なし(Noneが返る)"扱いになります。

```python:返り値がある関数
def 関数名(引数1, 引数2, 引数3, ...):
    """ 関数の説明 """
    処理
    return 返り値
```

次は、与えられた数値を2倍にして返す関数の例です。

```python:main.py
# 関数を定義する
def calc_double(num):
    """ 2倍にして返す関数 """
    return num * 2

# 実行する
print(calc_double(10)) # 20
print(calc_double(20)) # 40
print(calc_double(30)) # 60
```

こちらは、与えられた2つの数値の合計を返す関数の例です。

```python:main.py
# 関数を定義する
def calc_total(num1, num2):
    """ 二つの数値の合計を返す関数 """
    return num1 + num2

# 実行する
print(calc_total(10, 20)) # 30
print(calc_total(30, 40)) # 70
print(calc_total(50, 60)) # 110
```

引数と返り値は、セットで使われる事が多いので、ここで押さえておきましょう。

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「モジュールを使ってみよう」です。
お楽しみに!!
