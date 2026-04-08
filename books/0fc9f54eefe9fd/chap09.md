---
title: "第9章: カウンタを表示しよう"
---

# カウンタを表示しよう

今回は、鬼の残り数を示すカウンターを表示します。

## 1, 変数を用意する

鬼軍団の残りの数をカウントする、"counter"変数を用意します。

```python:main.py(抜粋)
# 鬼カウンタ
counter = TOTAL_DEMONS
```

## 2, カウンターをマイナス1する

"on_mouse_clicked()"関数で、鬼を捕まえる都度、カウンターをマイナス1します。
グローバル変数の、"counter"の値を変更するので、"global"を忘れずに記述します。

```python:main.py(抜粋)
def on_mouse_clicked(e):
    global counter
    #print("Clicked:", e.x, e.y)

    # 鬼軍団
    for demon in demons:
        if demon.is_inside(e.x, e.y):
            if demon.is_dead(): continue
            demon.die(cvs)
            counter = counter - 1 # 鬼カウンタをマイナス1
            break
```

## 3, カウンターを表示する

"update()"関数では、先ほどの"counter"を画面に描画する処理を実装します。

```python:main.py(抜粋)
def update():
    """ 更新関数 """
    
    cvs.delete("hud")

    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 鬼カウンタを描画
    msg = "残り鬼数: {}".format(counter)
    cvs.create_text(20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="nw")

    # 鬼軍団
    for demon in demons:
        overlap_area(demon) # 画面外判定
        demon.update(cvs)

    root.after(F_INTERVAL, update)
```

![](/images/books/0fc9f54eefe9fd/09_01.gif)

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
        
        file_alive = "images/dmn_alive_{}.png".format(self.type)
        self.photo_alive = tkinter.PhotoImage(file=file_alive)
        
        file_dead = "images/dmn_dead_{}.png".format(self.type)
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

F_RATE = 30
F_INTERVAL = int(1000 / F_RATE)

FONT = ("Arial", 16)

mx, my = 0, 0

bg_photo, bg_image = None, None

TOTAL_DEMONS = 10

demons = []

# 鬼カウンタ
counter = TOTAL_DEMONS

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

    # 鬼カウンタを描画
    msg = "残り鬼数: {}".format(counter)
    cvs.create_text(20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="nw")

    # 鬼軍団
    for demon in demons:
        overlap_area(demon)
        demon.update(cvs)

    root.after(F_INTERVAL, update)

def overlap_area(obj):
    if obj.x < 0: obj.set_x(W)
    if W < obj.x: obj.set_x(0)
    if obj.y < 0: obj.set_y(H)
    if H < obj.y: obj.set_y(0)

def on_mouse_clicked(e):
    global counter
    #print("Clicked:", e.x, e.y)

    # 鬼軍団
    for demon in demons:
        if demon.is_inside(e.x, e.y):
            if demon.is_dead(): continue
            demon.die(cvs)
            counter = counter - 1 # 鬼カウンタをマイナス1
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
次回のタイトルは「残り時間を表示しよう」です。
お楽しみに!!