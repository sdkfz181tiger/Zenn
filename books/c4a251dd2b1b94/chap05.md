---
title: "第5章: 文字列を使ってみよう"
---

# Python3で文字列を使ってみよう

今回のテーマは"文字列"です。
文字列を使った様々な記述方法について学びます。

## 文字列とは

文字列とは、その名の通り"文字"の"列"の事です。
Python3では、基本的に文字列を、""(ダブルクォーテーション)か、''(シングルクォーテーション)で表現します。
以下の例では、出力結果がどちらも同じになります。

```python:main.py
print("Hello, Python3!!")# Hello, Python3!!
print('Hello, Python3!!')# Hello, Python3!!
```

## 文字列の連結

"\+"を使う事で、文字列と文字列を連結することができます。

```python:main.py
print("Hello, " + "Python3!!")# Hello, Python3!!
```

""と、""を並べるだけでも文字列を連結する事ができます。
こちらは、長い文字列同士を連結したい場合に特に便利です。

```python:main.py
print(
    "Hello, "
    "Python3!!")# Hello, Python3!!
```

## 文字列の繰り返し

"\*"を使う事で、文字列を繰り返して連結させることができます。

```python:main.py
print("Hello, " * 3 + "Python3!!")
# Hello, Hello, Hello, Python3!!
```

## 改行と特殊文字

文字列の中で特殊な意味を持つ記号は、
"\\"(バックスラッシュ)を使って記述します。
これを、「エスケープシーケンス」と呼びます。

```python:main.py
print("Hello, \nPython3!!")# \nは改行
# Hello, 
# Python3!!
print("Hello, \tPython3!!")# \tはタブ
# Hello,     Python3!!
print("Hello, \\Python3!!")# \を表示したいときは2回記述する
# Hello, \Python3!!
```

## 文字列の長さを調べる

文字列の長さ(何文字なのか)を調べたい時は、len関数を使います。

```python:main.py
print(len("Hello, Python3!!"))# 16
```

## 文字列の一部分を取り出す

文字列の一部分だけを抜き出したい時は、スライスを使います。
Python3では、0文字目から数えます。

```python:main.py
message = "Hello, Python3!!"# 文字列を変数に格納します(後の章で解説します)
print(message[0:6])# Hello (0文字目から5文字目まで)
print(message[6:])# , Python3!! (6文字目から最後まで)
print(message[:10])# Hello, Py (最初から9文字目まで)
print(message[-1:])# ! (最後の1文字)
print(message[-3:])# 3!! (最後の3文字)
```

## 文字列フォーマット

最後に、文字列フォーマットという便利な書き方を紹介します。

```python:main.py
lang1 = "Python3"
lang2 = "JavaScript"
lang3 = "C++"
print(f"Hello, {lang1} and {lang2} and {lang3}!!")
# Hello, Python3 and JavaScript and C++!!
```

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「変数を使ってみよう」です。
お楽しみに!!
