---
title: "第5章: スプライトを動かしてみよう"
---

# スプライトを動かしてみよう

今回は、"スプライトの動き"についてです。
前回作った、DemonSpriteクラスを改良していきます。

## 1, DemonSpriteクラスを改良する

DemonSpriteクラスのコンストラクタに、新たに2つのメンバ変数、"vx"と"vy"を追加します。
これらは、"移動速度"として利用します。

| メンバ変数 | 意味 |
| ---- | ---- |
| self.x | x座標 |
| self.y | y座標 |
| self.r | スプライトの半径 |
| self.vx | x方向の速度 |
| self.vy | y方向の速度 |
| self.oval | 円を描くオブジェクト |

DemonSpriteクラスの"update()"メソッドでは、
"vx"を"x"に、"vy"を"y"座標にそれぞれ加算します。
次のコードを毎フレーム実行する為、鬼スプライトが移動します。

```python:sprite.py(抜粋)
# 座標の更新
self.x = self.x + self.vx
self.y = self.y + self.vy
```

次に、"move()"メソッドを追加します。
このメソッドは、引数の"spd"に速度、"deg"に角度を受け取ります。

これを元にして、x方向の速度、y方向の速度にそれぞれ変換し、"vx"と"vy"を決定します。
(このあたりの解説はまた今度!!)

```python:sprite.py(抜粋)
def move(self, spd, deg):
    radian = deg * math.pi / 180 # 角度をラジアンに変換
    self.vx = spd * math.cos(radian) # x方向の速度を決定
    self.vy = spd * math.sin(radian) # y方向の速度を決定
```

"stop()"メソッドはとてもシンプルです。
速度0、角度0にして"move()"メソッドを間接的に実行します。
(止まるという事ですねw)

```python:sprite.py(抜粋)
def stop(self):
    self.move(0, 0) # 速度0、角度0で実行する(止まる)
```

以上の機能を実装した完成コードは、次の通りです。

```python:sprite.py(完成コード)
import math
import random
import tkinter

# 鬼クラス
class DemonSprite:

    def __init__(self, cvs, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0 # x方向の速度
        self.vy = 0 # y方向の速度
        # 円
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill="white", width=0)

    def update(self, cvs):

        # 座標の更新
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        # 円の座標を更新
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)

    def move(self, spd, deg):
        radian = deg * math.pi / 180 # 角度をラジアンに変換
        self.vx = spd * math.cos(radian) # x方向の速度を決定
        self.vy = spd * math.sin(radian) # y方向の速度を決定

    def stop(self):
        self.move(0, 0) # 速度0、角度0で実行する(止まる)
```

## 2, 改良したDemonSpriteを使ってみる

TODO: 


# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「xxxしてみよう」です。
お楽しみに!!