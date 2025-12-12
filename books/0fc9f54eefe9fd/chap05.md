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
"update()"メソッドは、30ミリ秒ごとに呼ばれるので、毎回少しずつ座標が変化してスプライトが動いて見えるのです。

```python:sprite.py(抜粋)
# 座標の更新
self.x = self.x + self.vx # x座標に、vxを加算する
self.y = self.y + self.vy # y座標に、vyを加算する
```

次に、"move()"メソッドを追加します。
このメソッドは、引数の"spd"に速度、"deg"に角度を受け取ります。

これを元にして、"vx"(x方向の速度)と"vy"(y方向の速度)を決定します。
これは、いわゆる"速度ベクトル"の成分です。
(難しく聞こえるかもしれませんが、今は"向き付きの速度"くらいの意味で大丈夫です）

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

"main.py"の、"init()"関数(初期化関数)では、DemonSpriteを多数生成しています。
このタイミングで、先ほど作った"move()"メソッドを実行します。
ついでに速度、角度もランダムにしてみます。

```python:main.py(抜粋)
# 鬼軍団
for i in range(TOTAL_DEMONS):
    x = random.random() * W
    y = random.random() * H
    demon = sprite.DemonSprite(cvs, x, y, 20)
    spd = random.randint(1, 4)   # 速度はランダム
    deg = random.randint(0, 360) # 角度もランダム
    demon.move(spd, deg)         # ランダムで移動
    demons.append(demon)
```

この時点で実行すると、DemonSpriteが動き出します。
しかし、しばらく見ていると、全てのスプライトが画面外に出ていってしまいます...
(ここの対応については次回!!)

![](/images/0fc9f54eefe9fd/05_01.gif)

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
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

```python:main.py(完成コード)
import math
import random
import sprite
import tkinter

W, H = 480, 320

FONT = ("Arial", 16)

mx, my = 0, 0

bg_photo, bg_image = None, None

TOTAL_DEMONS = 10

demons = []

def init():
    """ 初期化関数 """
    global bg_photo, bg_image

    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)

    # 鬼軍団
    for i in range(TOTAL_DEMONS):
        x = random.random() * W
        y = random.random() * H
        demon = sprite.DemonSprite(cvs, x, y, 20)
        spd = random.randint(1, 4)   # 速度はランダム
        deg = random.randint(0, 360) # 角度もランダム
        demon.move(spd, deg)         # ランダムで移動
        demons.append(demon)
    
def update():
    """ 更新関数 """
    cvs.delete("hud")

    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    for demon in demons:
        demon.update(cvs)

    root.after(30, update)

def on_mouse_clicked(e):
    #print("Clicked:", e.x, e.y)

def on_mouse_moved(e):
    global mx, my
    mx, my = e.x, e.y

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Button>", on_mouse_clicked) # マウス(Click)
root.bind("<Motion>", on_mouse_moved) # マウス(Motion)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
```
:::

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「スプライトを閉じ込めよう」です。
お楽しみに!!