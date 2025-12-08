---
title: "第4章: スプライトクラスを作ってみよう"
---

# スプライトクラスを作ってみよう

今回は、"スプライト"についてです。
ゲームに登場するキャラクター等のオブジェクトを、特別に"スプライト"と呼びます。
ここでは、新たにスプライトモジュールを追加し、そこにDemonSpriteクラスを定義します。

## 1, スプライトモジュールを用意する

"main.py"と同じフォルダに、新しく"sprite.py"ファイルを作ります。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py <- スプライトモジュール
　└ images/
　 　└ bg_jigoku.png
```

## 2, DemonSpriteクラスを定義する

"sprite.py"に、"DemonSprite"クラスを定義します。(鬼スプライト!!)
ここでは、ただ"円"を描画するだけのシンプルなクラスです。

スプライトクラスのコンストラクタでは、次のメンバ変数を定義しておきます。

| メンバ変数 | 意味 |
| ---- | ---- |
| self.x | x座標 |
| self.y | y座標 |
| self.r | スプライトの半径 |
| self.oval | 円を描くオブジェクト |

"self.oval"には、円を描くオブジェクトを格納します。(鬼の画像はしばらく後で登場します)
"cvs.create_oval()"メソッドの引数にはそれぞれ、
円の左上座標(x, y)、円の右下座標(x, y)、"fill"にはカラー、"width"には線の太さ(ここでは0)を指定します。

そして、"update()"メソッドでは、"self.oval"オブジェクトの座標を設定しています。

```python:sprite.py
import math
import random
import tkinter

# 鬼クラス
class DemonSprite:

    def __init__(self, cvs, x, y, r):
        self.x = x # x座標
        self.y = y # y座標
        self.r = r # 円の半径
        # 円
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill="white", width=0)

    def update(self, cvs):
        
        # 円の座標を更新
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)
```

## 3, スプライトクラスを使う

spriteモジュールをインポートすることで、"DemonSprite"クラスを使えるようになります。

```python:main.py(抜粋)
import sprite
```

"DemonSprite"は、次のようにインスタンス化して利用します。
第一引数から、キャンバス、x座標、y座標、円の半径です。

```python:main.py(抜粋)
demon = sprite.DemonSprite(cvs, 0, 0, 10)
```

## 4, 





# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「xxxしてみよう」です。
お楽しみに!!