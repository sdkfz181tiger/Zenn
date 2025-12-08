---
title: "第4章: スプライトクラスを作ってみよう"
---

# スプライトクラスを作ってみよう

今回は、"スプライト"についてです。
ゲームに登場するキャラクター等のオブジェクトの事を、特別に"スプライト"と呼びます。
ここでは、逃げ惑う鬼を、Demonクラスに定義します。

## 1, スプライトモジュールを用意する

"main.py"と同じフォルダに、新しく"sprite.py"ファイルを作ります。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py <- スプライトモジュール
　└ images/
　 　└ bg_jigoku.png
```

## 2, Demonクラスを定義する

"sprite.py"に、"Demon"クラスを定義します。

```python:sprite.py
import math
import random
import tkinter

# 鬼クラス
class Demon:

    def __init__(self, cvs, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        # 円
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill="gray", width=0)

    def update(self, cvs):
        
        # 円の座標を更新
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)
```



# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「xxxしてみよう」です。
お楽しみに!!