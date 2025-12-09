---
title: "第4章: スプライトを作ってみよう"
---

# スプライトを作ってみよう

今回は、"スプライト"についてです。
ゲームに登場するキャラクター等のオブジェクトを、特別に"スプライト"と呼びます。
ここでは、新たにスプライトモジュールを追加し、DemonSpriteクラスを定義します。

必要であれば、[12章:クラスを使ってみよう](https://zenn.dev/sdkfz181tiger/books/c4a251dd2b1b94/viewer/chap12)を確認しておくとスムーズです。

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

"sprite.py"に、DemonSpriteクラスを定義します。(鬼スプライト!!)

DemonSpriteクラスは、"鬼の位置や見た目を管理する設計図"です。
座標(x, y)や半径(r)を記憶し、画面更新のたびに"update()"で描き直します。
この設計図を元にして、鬼スプライトを大量生産するのです!!(興奮)

DemonSpriteクラスのコンストラクタでは、次のメンバ変数を定義しておきます。
現時点では、座標、半径、円を描くオブジェクトだけのシンプルな状態です。

| メンバ変数 | 意味 |
| ---- | ---- |
| self.x | x座標 |
| self.y | y座標 |
| self.r | スプライトの半径 |
| self.oval | 円を描くオブジェクト |

"self.oval"には、円を描くオブジェクトを格納します。
"cvs.create_oval()"メソッドの引数にはそれぞれ、
円の左上座標(x, y)、円の右下座標(x, y)、"fill"にはカラー、"width"には線の太さ(ここでは0)を指定しています。

"update()"メソッドでは、"self.oval"オブジェクトの座標を更新します。

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

## 3, DemonSpriteクラスを使う

spriteモジュールをインポートすることで、DemonSpriteクラスを使えるようになります。
その他、"mathモジュール"、"randomモジュール"もインポートしておきます。

```python:main.py(抜粋)
import math   # 数学的計算をするモジュール
import random # ランダムを生成するモジュール
import sprite # Spriteモジュール
import tkinter
```

そして、新たにグローバル変数として次の変数を追加します。

```python:main.py(抜粋)
# 鬼軍団の数
TOTAL_DEMONS = 10

# 鬼軍団
demons = []
```

"init()"関数(初期化関数)では、生成した鬼スプライトを、"demons"(鬼軍団)リストに追加します。

鬼スプライトの座標は、"random.random()"メソッドを利用してランダム位置とします。
"random.random()"は、"0.0以上〜1.0未満"の小数をランダムで返すメソッドです。
画面幅"W"にこの乱数を掛け算すると、"0.0以上〜W未満"の範囲で値を取得できるので、これをx座標としています。同様に、画面の高さ"H"を掛け算し、y座標としています。

```python:main.py(抜粋)
def init():
    """ 初期化関数 """
    global bg_photo, bg_image

    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)

    # 鬼軍団
    for i in range(TOTAL_DEMONS):
        x = random.random() * W # 0.0以上 ~ W未満の小数
        y = random.random() * H # 0.0以上 ~ H未満の小数
        demon = sprite.DemonSprite(cvs, x, y, 20) # 鬼スプライトを生成
        demons.append(demon) # リストに追加
```

"update()"関数(更新関数)では、"demons"(鬼軍団)リストの鬼スプライトそれぞれで"demon.update()"メソッドを実行します。

```python:main.py(抜粋)
def update():
    """ 更新関数 """
    cvs.delete("hud")

    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 鬼軍団
    for demon in demons:
        demon.update(cvs) # 鬼スプライトを更新

    # 画面更新
    root.after(30, update)
```

この時点で実行すると、ゲーム画面に10個のスプライト(白い円)が描画されます。

![](/images/0fc9f54eefe9fd/04_01.png)

## 4, 完成コード

今回の完成コードは次の通りです。

```python:sprite.py(完成コード)
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

```python:main.py(完成コード)
import math   # 数学的計算をするモジュール
import random # ランダムを生成するモジュール
import sprite # Spriteモジュール
import tkinter

W, H = 480, 320

FONT = ("Arial", 16)

mx, my = 0, 0

bg_photo, bg_image = None, None

# 鬼軍団の数
TOTAL_DEMONS = 10

# 鬼軍団
demons = []

def init():
    """ 初期化関数 """
    global bg_photo, bg_image

    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)

    # 鬼軍団
    for i in range(TOTAL_DEMONS):
        x = random.random() * W # 0.0以上 ~ W未満の小数
        y = random.random() * H # 0.0以上 ~ H未満の小数
        demon = sprite.DemonSprite(cvs, x, y, 20) # 鬼スプライトを生成
        demons.append(demon) # リストに追加
    
def update():
    """ 更新関数 """
    cvs.delete("hud")

    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 鬼軍団
    for demon in demons:
        demon.update(cvs) # 鬼スプライトを更新

    # 画面更新
    root.after(30, update)

def on_mouse_clicked(e):
    global counter
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
次回のタイトルは「スプライトを動かしてみよう」です。
お楽しみに!!