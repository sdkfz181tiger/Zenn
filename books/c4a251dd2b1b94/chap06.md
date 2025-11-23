---
title: "第6章: エラーと例外処理を使ってみよう"
---

# Pythonのエラーと例外処理を使ってみよう

今回は、エラーと例外処理について学びます。
特に、エラーログを正しく理解することで、素早くバグを見つけられるようになります。

## エラーとは

"エラー"と聞くとネガティブな印象が強すぎて身構えてしまいますが、
エラーログには沢山の"ヒント"が詰まっています。

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

## 例外処理とは

プログラムを実行したときに検知されるエラーを、特に"例外"と呼ぶときがあります。
大抵の場合、エラーが起きた瞬間、プログラムは強制停止してしまいます。

"例外処理"は、指定したエラーが起こるとパスし、後続の処理を継続させることが可能になります。
記述方法は、次のとおりです。

```python:main.py
try:
    エラーが起きるであろう処理
except ZeroDivisionError:
    エラーが起きてしまったときの処理(ログなど)
```

次の例は、例外処理を実装した上で、"Zero Division Error"をわざと起こしています。
エラーが起きた瞬間、処理は一旦"except"文の箇所を実行(ログを表示)し、
プログラムを停止させずに次の処理へ進みます。

```python:main.py
try:
    print(100 / 0)# Zero Division Error...!!
except ZeroDivisionError:
    print("Zeroで割り算だけは勘弁してください...")
```

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「分岐処理を使ってみよう」です。
お楽しみに!!