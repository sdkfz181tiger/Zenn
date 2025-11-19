---
title: "第12章: エラーパターンを知ろう"
---

# Pythonのエラーパターンを知ろう

今回は、エラーのパターンについて学びます。

## エラーとは

エラーのパターンを正しく理解することで、素早くバグを見つけることができます。

以下の例は、エラーのパターン例です。
次の箇所に注目すると、エラーのファイル名、行番号、種類を簡単に知る事ができるので覚えておきましょう。

```command:エラーのパターン
Traceback (most recent call last):
    File エラーが出たファイル名, line エラーが出た行番号, in <module>
    エラーが起きた(と)思われる箇所
エラーの種類: エラーの詳細 (detected at line エラーが出た行番号)
```

### Syntax Error(構文エラー)

単純な記述ミスによるエラーです。

次の例では、
エラーが出たファイル名は、"main.py"、
エラーが出た行番号は、"1行目"、
エラーの種類は、"Syntax Error"だとわかります。

以上の情報を元にして、1行目に注目し"記述ミス"を探します。

```python:main.py
print("Hello, Python!!)

Traceback (most recent call last):
    File "/Users/xxx/main.py", line 1, in <module>
    print("Hello, Python!!)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

ありがちなSyntax Errorのパターンは次の通りです。

| エラー例 | エラーの内容 |
| ---- | ---- |
| ```print("Hello, Python!!)``` | クォート閉じ忘れ |
| ```print("Hello, Python!!"``` | ")"閉じ忘れ |
| ```if a in range(10)``` | ":"忘れ |

### Name Error(名前エラー)

Pythonに定義されていない名前を使おうとすると出るエラーです。

次の例では、1行目の"prent"が怪しいと直ぐに気づく事ができます。
最後の行では、「"prent"じゃなくて、"print"では...?」と教えてくれています。

```python:main.py
prent("Hello, Python!!") # prentという定義は無い...(自分で定義していれば別!!)

Traceback (most recent call last):
    File "/Users/xxx/main.py", line 1, in <module>
    prent("Hello, Python!!")
    ^^^^^
NameError: name 'prent' is not defined. Did you mean: 'print'?
```

### Type Error(型エラー)

データの"型"に関連するエラーです。

次の例では、"Hello, "という文字列と、100という数値を繋げようとしてエラーが起きています。
最後の行では、「文字列は数値と連結できません...」と教えてくれています。

```python:main.py
print("Hello, " + 100) # "Hello, " と、 100を連結させ...!?

Traceback (most recent call last):
    File "/Users/xxx/main.py", line 1, in <module>
    print("Hello, " + 100)
          ~~~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
```

この場合は、100を文字列としてキャストする必要があります。

```python:main.py
print("Hello, " + str(100)) # 文字列にキャストしてから連結する
# Hello, 100
```

### Zero Division Error(0除算エラー)

0で割り算をしてしまった時に出るエラーです。
(無限になってしまいますね...)

次の例では、実際に100を0で割り算し、エラーを起こしています。

```python:main.py
print(100 / 0) # 100を0で割り算...!?

Traceback (most recent call last):
    File "/Users/xxx/main.py", line 1, in <module>
    print(100 / 0)
          ~~~~^~~
ZeroDivisionError: division by zero
```

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「例外処理を使ってみよう」です。
お楽しみに!!