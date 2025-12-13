---
title: "第10章: 残り時間を表示しよう"
---

# 残り時間を表示しよう

今回は、残り時間を表示し、ゲーム終了判定を実装します。
(最終回です!!)

## 1, 変数を用意する

残り時間を格納する、"timer"変数を用意します。
ここでは、10秒程度を想定した値を計算します。(難しめ!?)

```python:main.py(抜粋)
# タイマー
timer = F_RATE * 10 # 残り時間(10秒)
```

## 2, タイマーを-1する

"update()"関数では、タイマーをゲーム画面右上に表示し、タイマー変数を-1します。

```python:main.py(抜粋)
def update():
    """ 更新関数 """
    global timer
    
    cvs.delete("hud")

    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    msg = "残り鬼数: {}".format(counter)
    cvs.create_text(20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="nw")

    # タイマーを描画
    msg = "残り時間: {:.2f}秒".format(timer / F_RATE)
    cvs.create_text(W-20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="ne")

    # 鬼軍団
    for demon in demons:
        overlap_area(demon)
        demon.update(cvs)

    # タイマー
    timer = timer - 1

    root.after(F_INTERVAL, update)
```

## 3, ゲーム終了判定

最後に、鬼の残り数が0であれば、"GAME CLEAR"を、
タイマーが0であれば、"GAME OVER"を表示する処理を実装して完成です。

```python:main.py(抜粋)
# 画面更新
if 0 < counter and 0 <= timer:
    root.after(F_INTERVAL, update)
else:
    # ゲーム判定
    msg = "GAME CLEAR" if counter <= 0 else "GAME OVER"
    cvs.create_text(W/2, H-40, text=msg,
                    fill="white", font=FONT, tag="hud")
```

![](/images/0fc9f54eefe9fd/10_01.gif)

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

# キャンバスの幅と高さ
W, H = 480, 320

# フレームレート
F_RATE = 30 # 1秒間に実行するフレーム回数
F_INTERVAL = int(1000 / F_RATE) # 1フレームの間隔

# フォント
FONT = ("Arial", 16)

# マウスの座標
mx, my = 0, 0

# 背景画像とイメージ
bg_photo, bg_image = None, None

# 鬼軍団の数
TOTAL_DEMONS = 10

# 鬼軍団
demons = []

# 鬼カウンタ
counter = TOTAL_DEMONS

# タイマー
timer = F_RATE * 10 # 残り時間(10秒)

def init():
    """ 初期化関数 """
    global bg_photo, bg_image

    # 背景
    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)

    # 鬼軍団
    for i in range(TOTAL_DEMONS):
        x = random.random() * W
        y = random.random() * H
        demon = sprite.DemonSprite(cvs, x, y, 20)
        spd = random.randint(1, 4)
        deg = random.randint(0, 360)
        demon.move(spd, deg) # ランダムで移動
        demons.append(demon)
    
def update():
    """ 更新関数 """
    global timer
    
    cvs.delete("hud")

    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 鬼カウンタを描画
    msg = "残り鬼数: {}".format(counter)
    cvs.create_text(20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="nw")

    # タイマーを描画
    msg = "残り時間: {:.2f}秒".format(timer / F_RATE)
    cvs.create_text(W-20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="ne")

    # 鬼軍団
    for demon in demons:
        overlap_area(demon) # 画面外判定
        demon.update(cvs)

    # タイマー
    timer = timer - 1

    # 画面更新
    if 0 < counter and 0 <= timer:
        root.after(F_INTERVAL, update)
    else:
        # ゲーム判定
        msg = "GAME CLEAR" if counter <= 0 else "GAME OVER"
        cvs.create_text(W/2, H-40, text=msg,
                        fill="white", font=FONT, tag="hud")

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

# 終わりに...

ここまで読んでいただき有り難うございました。
今回で、"Pythonで2Dゲームをかじる本_tkinter編"は終了です。

今回作ったゲームはとてもシンプルですが、

- スプライト管理
- マウス入力
- ゲームループ
- 終了判定

といった、ゲーム制作の基本要素がすべて含まれています。

ここまで理解できていれば、
Tkinterを使った簡単なゲームは、もう自力で作れるはずです。

次は、
- クラスを使ってコードを整理する  
- 効果音を鳴らす  
- もう一度遊べる仕組みを作る  

などに挑戦してみるのもおすすめです。
この連載が、そのきっかけになれば幸いです。


