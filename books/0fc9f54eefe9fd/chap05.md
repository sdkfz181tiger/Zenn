---
title: "第5章: スプライトを動かしてみよう"
---

# スプライトを動かしてみよう

今回は、"スプライトの動き"についてです。
前回作った、DemonSpriteクラスを改良していきます。

## 1, DemonSpriteクラスを改良する

DemonSpriteクラスのコンストラクタに、新たに2つのメンバ変数、"vx"と"vy"を追加します。
これらは、毎フレーム座標を変化させる"移動速度"として利用します。

```python:sprite.py(抜粋)
def __init__(self, cvs, x, y, r):
    self.x = x
    self.y = y
    self.r = r
    self.vx = 0 # x方向の速度
    self.vy = 0 # y方向の速度
    # 円
    self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                fill="white", width=0)
```

DemonSpriteクラスの"update()"メソッドで、
"vx"を"x"に、"vy"を"y"座標にそれぞれ加算します。
具体的には次のコードです。

```python:sprite.py(抜粋)
# 座標の更新
self.x = self.x + self.vx # x座標に、vxを加算する
self.y = self.y + self.vy # y座標に、vyを加算する
```

次に、"move()"メソッドを追加します。
このメソッドは、引数の"spd"に速度、"deg"に角度を受け取ります。

これを元にして、"vx"(x方向の速度)と"vy"(y方向の速度)を決定します。
(このあたりの解説はまた今度!!)

```python:sprite.py(抜粋)
def move(self, spd, deg):
    radian = deg * math.pi / 180 # 角度をラジアンに変換
    self.vx = spd * math.cos(radian) # x方向の速度を決定
    self.vy = spd * math.sin(radian) # y方向の速度を決定
```

最後に"stop()"メソッドを追加します。
このメソッドはとてもシンプルで、速度0、角度0で"move()"メソッドを実行します。
(止まるという事ですね)

```python:sprite.py(抜粋)
def stop(self):
    self.move(0, 0) # 速度0、角度0で実行する(止まる)
```

## 2, 改良したDemonSpriteを使ってみる

"main.py"の、"init()"関数(初期化関数)で、DemonSpriteを生成するタイミングで



## 3, 完成コード

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
        self.x = self.x + self.vx # x座標に、vxを加算する
        self.y = self.y + self.vy # y座標に、vyを加算する
        
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

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「xxxしてみよう」です。
お楽しみに!!