---
title: "第8章: スプライトに鬼画像を付けよう"
---

# スプライトに鬼画像を付けよう

今回は、スプライトに鬼の画像を適用します。

## 1, 鬼の画像を用意する

ゲームに登場する鬼の画像は、次のものをコピーしてお使いください。

| タイプ | 生き | ファイル名 | 死に | ファイル名 |
| ---- | ---- | ---- | ---- | ---- |
| 青鬼ちゃん | ![](/images/0fc9f54eefe9fd/dmn_alive_b.png) | dmn_alive_b.png | ![](/images/0fc9f54eefe9fd/dmn_dead_b.png) | dmn_dead_b.png |
| 緑鬼ちゃん | ![](/images/0fc9f54eefe9fd/dmn_alive_g.png) | dmn_alive_g.png | ![](/images/0fc9f54eefe9fd/dmn_dead_g.png) | dmn_dead_g.png |
| 赤鬼ちゃん | ![](/images/0fc9f54eefe9fd/dmn_alive_r.png) | dmn_alive_r.png | ![](/images/0fc9f54eefe9fd/dmn_dead_r.png) | dmn_dead_r.png |


画像ファイルは、"images"フォルダにまとめて配置します。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py
　└ images/
　 　├ bg_jigoku.png
　 　├ dmn_alive_b.png <- 青鬼(生き)
　 　├ dmn_alive_g.png <- 緑鬼(生き)
　 　├ dmn_alive_r.png <- 赤鬼(生き)
　 　├ dmn_dead_b.png  <- 青鬼(死に)
　 　├ dmn_dead_g.png  <- 緑鬼(死に)
　 　└ dmn_dead_r.png  <- 赤鬼(死に)
```

## 2, DemonSpriteクラスを改良する

DemonSpriteクラスのコンストラクタで、画像を読み込むコードを追加します。

画像オブジェクトは、"tkinter.PhotoImage()"メソッドと、
"create_image()"メソッドとを組み合わせて生成します。

ここでは、ファイル名にはランダムを利用して、
"b(青鬼)"、"g(緑鬼)"、"r(赤鬼)"をランダムで選び、ファイル名を準備します。

次に、鬼が生きている状態の画像は"self.photo_alive"として、
死んでいる状態の画像は"self.photo_dead"に格納します。

最終的に表示される画像は、"self.image"に格納します。
初期状態は、生きている状態なので、引数"image"には、"self.photo_alive"を指定しておきます。

```python:sprite.py(抜粋)
def __init__(self, cvs, x, y, r):
    self.x = x
    self.y = y
    self.r = r
    self.vx = 0
    self.vy = 0
    self.dead = False
    # 円
    self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                fill="white", width=0)
    # r, g, bからランダムで一つ選ぶ
    self.type = random.choice(("r", "g", "b"))
    
    file_alive = "images/dmn_alive_{}.png".format(self.type) # 生き
    self.photo_alive = tkinter.PhotoImage(file=file_alive)
    
    file_dead = "images/dmn_dead_{}.png".format(self.type) # 死に
    self.photo_dead = tkinter.PhotoImage(file=file_dead)

    self.image = cvs.create_image(x, y, image=self.photo_alive)
```

最後に、"die()"メソッドで、"cvs.itemconfig()"メソッドを実行して画像を変更します。

```python:sprite.py(抜粋)
def die(self, cvs):
    self.dead = True
    self.stop()
    # 円の色を更新
    cvs.itemconfig(self.oval, fill="red")
    # イメージの画像を更新
    cvs.itemconfig(self.image, image=self.photo_dead)
```

ここまでの処理を実装すると、スプライトをクリックで止めることができるようになります。

![](/images/0fc9f54eefe9fd/08_01.gif)

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
        self.vx = 0
        self.vy = 0
        self.dead = False
        # 円
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill="white", width=0)
        # r, g, bからランダムで選ぶ
        self.type = random.choice(("r", "g", "b"))
        
        file_alive = "images/dmn_alive_{}.png".format(self.type) # 生き
        self.photo_alive = tkinter.PhotoImage(file=file_alive)
        
        file_dead = "images/dmn_dead_{}.png".format(self.type) # 死に
        self.photo_dead = tkinter.PhotoImage(file=file_dead)

        self.image = cvs.create_image(x, y, image=self.photo_alive)

    def update(self, cvs):

        # 座標の更新
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        # 円の座標を更新
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)
        
        # イメージの座標を更新
        cvs.coords(self.image, self.x, self.y)

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
        self.dead = True
        self.stop()
        # 円の色を更新
        cvs.itemconfig(self.oval, fill="red")
        # イメージの画像を更新
        cvs.itemconfig(self.image, image=self.photo_dead)

    def is_dead(self):
        return self.dead

    def is_inside(self, x, y):
        dist_x = (self.x - x) ** 2
        dist_y = (self.y - y) ** 2
        dist = (dist_x + dist_y) ** 0.5
        return dist < self.r
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

    # 鬼軍団
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
    global counter
    print("Clicked:", e.x, e.y)

    # 鬼軍団
    for demon in demons:
        if demon.is_inside(e.x, e.y):
            if demon.is_dead(): continue
            demon.die(cvs)
            break

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
次回のタイトルは「xxx」です。
お楽しみに!!