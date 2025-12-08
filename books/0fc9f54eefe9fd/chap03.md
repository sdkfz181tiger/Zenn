---
title: "第3章: マウスイベントを使ってみよう"
---

# マウスイベントを使ってみよう

今回は、"マウスイベント"についてです。
マウスの動きやクリックを検知し、その座標を取得します。

## マウスイベントの設定方法

マウスイベントは、Tkオブジェクトに対して次の様に指定します。
第一引数に対し、"<Button>"でクリックを検知、"<Motion>"でマウスの移動を検知します。
第二引数には、イベント発生タイミングで実行したいメソッドを指定します。

```python:main.py(抜粋)
root.bind("<Button>", on_mouse_clicked) # マウス(Click)
root.bind("<Motion>", on_mouse_moved) # マウス(Motion)
```

### 1, Buttonイベント

Buttonイベントを受け取る、"on_mouse_clicked()"メソッドでは、
"e.x"でx座標を、"e.y"でy座標を取得しています。

```python:main.py(抜粋)
def on_mouse_clicked(e):
    print("Clicked:", e.x, e.y)
```

クリックをする都度、その座標がShellに表示されていきます。

![](/images/0fc9f54eefe9fd/03_01.png)

### 2, Motionイベント

Motionイベントを受け取る、"on_mouse_moved()"メソッドでは、
その座標をグローバル変数"mx", "my"にコピーしています。
(globalを忘れずに...)

```python:main.py(抜粋)
def on_mouse_moved(e):
    global mx, my
    mx, my = e.x, e.y # グローバル変数にコピー
```

"update()"メソッドでは、"mx"と、"my"に格納された座標をキャンバスに描画しています。
"cvs.create_text()"メソッドの引数は、x座標、y座標、
"text"には表示する文字列、"font"にはフォント名とサイズを指定します。

```python:main.py(抜粋)
def update():
    """ 更新関数 """
    cvs.delete("hud")

    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 画面更新
    root.after(30, update)
```

この時点で実行すると、ゲーム画面上のマウス位置に座標が描画されます。

![](/images/0fc9f54eefe9fd/03_02.gif)

### 3, 完成コード

今回の完成コードです。

```python:main.py(完成コード)
import tkinter

# キャンバスの幅と高さ
W, H = 480, 320

# フォント
FONT = ("Arial", 16)

# マウスの座標
mx, my = 0, 0

# 背景画像とイメージ
bg_photo, bg_image = None, None

def init():
    """ 初期化関数 """
    global bg_photo, bg_image

    # 背景
    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)
    
def update():
    """ 更新関数 """
    cvs.delete("hud")

    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 画面更新
    root.after(30, update)

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
次回のタイトルは「xxxしてみよう」です。
お楽しみに!!