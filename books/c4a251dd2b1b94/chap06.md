---
title: "第6章: 変数を使ってみよう"
---

# Python3で変数を使ってみよう

今回のテーマは"変数"です。
変数を使う事で、特定の値を再利用する事ができます。

## 変数とは

"変数"とは、値に名前をつけて再利用できるようにする仕組みです。
Pythonでは、値に「ラベル」を貼るイメージで使います。

変数名は自由に決められますが、命名規則があります。

- 先頭に数字は使えない
- 英字・数字・アンダースコアで構成する
- 大文字と小文字は区別される(msg と Msg は別物)
- Python3の予約語(プログラム的な意味がある単語)は使えない

変数に値を代入する時は、"="を使います。

```python:main.py
変数名 = 値
```

以上を踏まえたサンプルコードは下記の通りです。

```python:main.py
msg1 = "Hello"   # これはOK
msg2 = "Python3" # これはOK
2msg = "Python3" # これはNG (先頭に数字を使っている)
if = "Python3"   # これはNG (予約語を使っている)
print(msg1)      # Hello
print(msg2)      # Python3
```

## 変数を使う

変数の値が数値であれば、計算に利用することができます。

```python:main.py
num1 = 100
num2 = 10
num3 = 1
print(num1 + num2) # 110
print(num2 + num3) # 11
print(num1 - num2) # 90
print(num1 * num2) # 1000
print(num1 / num2) # 10.0 (割り算の時は小数になります)
```

変数の値が文字列の場合は、"+"を使って連結することができます。

```python:main.py
str1 = "Hop"
str2 = "Step"
str3 = "Jump"
print(str1 + str2 + str3) # HopStepJump
```

変数の値が数値の場合は、str()関数で文字列に変換してから連結します。

```python:main.py
famicom = "ファミコンの誕生日:"
birth = 1983
print(famicom + str(birth))
# ファミコンの誕生日:1983
```

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「分岐処理を使ってみよう」です。
お楽しみに!!
