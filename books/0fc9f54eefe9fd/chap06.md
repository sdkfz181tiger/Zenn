---
title: "第6章: スプライトを閉じ込めよう"
---

# スプライトを閉じ込めよう

今回は、スプライトの座標を元に、ゲーム画面から出られないように改良します。

## 1, DemonSpriteクラスを改良する

DemonSpriteクラスに、x座標、y座標を変更する"set_x()"、"set_y()"メソッドを追加します。
画面の外に出たら、このメソッドを使って座標を変更します。

```python:sprite.py(抜粋)
def set_x(self, x):
    self.x = x # x座標を変更

def set_y(self, y):
    self.y = y # y座標を変更
```

## 2, 画面外判定を実装する

新たに、"main.py"には、画面外判定を行う"overlap_area()"関数を追加します。
引数には、スプライト(obj)を受け取り、4つの判定を実装しています。
上から順番に、
x座標が0(画面の左端)より小さい場合は、"W"(画面の右端)に、
"W"(画面の右端)よりx座標が大きい場合は、0(画面の左端)に変更します。
続く2行は、y座標に対し同様のことを行なっています。

```python:main.py(抜粋)
def overlap_area(obj):
    if obj.x < 0: obj.set_x(W) # x座標が画面の左端より小さい時は右端へ
    if W < obj.x: obj.set_x(0) # x座標が画面の右端より大きい時は左端へ
    if obj.y < 0: obj.set_y(H)
    if H < obj.y: obj.set_y(0)
```

上記の"overlap_area()"関数は、"update()"関数(更新関数)で利用します。

```python:main.py(抜粋)
# 鬼軍団
for demon in demons:
    overlap_area(demon) # 画面外判定
    demon.update(cvs)
```

上記の処理を実装すると、スプライトをゲーム画面に閉じ込めることが可能になります。

![](/images/0fc9f54eefe9fd/06_01.gif)

## 3, 完成コード

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
        self.dead = False
        # 円
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill="white", width=0)

    def update(self, cvs):

        # 座標の更新
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)

    def set_x(self, x):
        self.x = x # x座標を変更

    def set_y(self, y):
        self.y = y # y座標を変更

    def move(self, spd, deg):
        radian = deg * math.pi / 180
        self.vx = spd * math.cos(radian)
        self.vy = spd * math.sin(radian)

    def stop(self):
        self.move(0, 0)
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
        overlap_area(demon) # 画面外判定
        demon.update(cvs)

    root.after(30, update)

def overlap_area(obj):
    if obj.x < 0: obj.set_x(W) # x座標が画面の左端より小さい時は右端へ
    if W < obj.x: obj.set_x(0) # x座標が画面の右端より大きい時は左端へ
    if obj.y < 0: obj.set_y(H)
    if H < obj.y: obj.set_y(0)

def on_mouse_clicked(e):
    print("Clicked:", e.x, e.y)

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
次回のタイトルは「スプライトをクリックで止めよう」です。
お楽しみに!!