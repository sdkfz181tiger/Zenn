---
title: "第7章: スプライトをクリックで止めよう"
---

# スプライトをクリックで止めよう

今回は、スプライトに対するクリック判定と、状態管理を実装します。

## 1, DemonSpriteクラスを改良する

DemonSpriteクラスのコンストラクタに、新たにメンバ変数、"dead"を追加します。
これは、スプライトの生死を管理するフラグとして利用します。
初期値は"False"(生きている)とし、鬼スプライトをクリックしたタイミングで"True"(死んでいる)にします。

```python:sprite.py(抜粋)
def __init__(self, cvs, x, y, r):
    self.x = x
    self.y = y
    self.r = r
    self.vx = 0
    self.vy = 0
    self.dead = False # 死亡フラグ
    # 円
    self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                fill="white", width=0)
```

次に、スプライトを死亡状態に変更する"die()"メソッドを追加します。
ここでは、"dead"フラグをTrueに変更して停止、そして円を"赤"に変更します。

```python:sprite.py(抜粋)
def die(self, cvs):
    self.dead = True # 死亡フラグをTrueに
    self.stop() # 停止する
    # 円の色を更新
    cvs.itemconfig(self.oval, fill="red")
```

次に、スプライトの死亡状態を返す、"is_dead()"メソッドを追加します。
返り値が"False"であれば、生きている状態、"True"であれば、死んでいる状態とします。

```python:sprite.py(抜粋)
def is_dead(self):
    return self.dead # 死亡フラグを返す
```

最後に、クリックした座標を受け取り、スプライトの座標との距離を計算する、"is_hit()"メソッドを追加します。
計算された距離"dist"が、半径"r"より小さい時は"True"を、大きい時は"False"を返します。
(円と、クリックされた座標が"重なっているか"を確認しているだけです)

```python:sprite.py(抜粋)
def is_hit(self, x, y):
    dist_x = (self.x - x) ** 2 # スプライトの水平方向の距離
    dist_y = (self.y - y) ** 2 # スプライトの垂直方向の距離
    dist = (dist_x + dist_y) ** 0.5 # スプライトとの距離
    return dist < self.r # スプライトとの距離が半径以内ならヒット(True)
```

## 2, main.pyを改良する

"main.py"に実装した、"on_mouse_clicked()"関数では、クリックした座標を取得することができます。
このタイミングで、スプライトそれぞれと距離を計算してクリック判定を行います。

ここで、死亡フラグが"True"になっているスプライトに対して判定を行う必要が無いので、
"is_dead()"を使って死亡フラグを確認します。
死亡フラグが"True"の時は、"continue"でキャンセルし、次のスプライトを調べていきます。

```python:main.py(抜粋)
def on_mouse_clicked(e):
    print("Clicked:", e.x, e.y)

    # 鬼軍団
    for demon in demons:
        if demon.is_dead(): continue # 既に死んでいたら次のスプライトへ
        if demon.is_hit(e.x, e.y): # クリック座標がヒットしていたら
            demon.die(cvs) # 死亡フラグをOnにする
            break # 繰り返し処理を終了
```

ここまでの処理を実装すると、スプライトをクリックで止めることができるようになります。

![](/images/0fc9f54eefe9fd/07_01.gif)

## x, 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

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
        self.vx = 0
        self.vy = 0
        self.dead = False # 死亡フラグ
        # 円
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill="white", width=0)

    def update(self, cvs):

        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def move(self, spd, deg):
        radian = deg * math.pi / 180
        self.vx = spd * math.cos(radian)
        self.vy = spd * math.sin(radian)

    def stop(self):
        self.move(0, 0)

    def die(self, cvs):
        self.dead = True # 死亡フラグをTrueに
        self.stop() # 停止する
        # 円の色を更新
        cvs.itemconfig(self.oval, fill="red")

    def is_dead(self):
        return self.dead # 死亡フラグを返す

    def is_hit(self, x, y):
        dist_x = (self.x - x) ** 2 # スプライトの水平方向の距離
        dist_y = (self.y - y) ** 2 # スプライトの垂直方向の距離
        dist = (dist_x + dist_y) ** 0.5 # スプライトとの距離
        return dist < self.r # スプライトとの距離が半径以内ならヒット(True)
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
        spd = random.randint(1, 4)
        deg = random.randint(0, 360)
        demon.move(spd, deg)
        demons.append(demon)
    
def update():
    """ 更新関数 """
    cvs.delete("hud")

    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    for demon in demons:
        overlap_area(demon)
        demon.update(cvs)

    root.after(30, update)

def overlap_area(obj):
    if obj.x < 0: obj.set_x(W)
    if W < obj.x: obj.set_x(0)
    if obj.y < 0: obj.set_y(H)
    if H < obj.y: obj.set_y(0)

def on_mouse_clicked(e):
    print("Clicked:", e.x, e.y)

    # 鬼軍団
    for demon in demons:
        if demon.is_dead(): continue # 既に死んでいたら次のスプライトへ
        if demon.is_hit(e.x, e.y): # クリック座標がヒットしていたら
            demon.die(cvs) # 死亡フラグをOnにする
            break # 繰り返し処理を終了

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

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「スプライトを鬼スプライトにしよう」です。
お楽しみに!!