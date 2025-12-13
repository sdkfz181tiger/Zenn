---
title: "第3章: マウスイベントを使ってみよう"
---

# マウスイベントを使ってみよう

今回は、"マウスイベント"についてです。
マウスの動きやクリックを検知し、その座標を取得します。

## マウスイベントの設定方法

マウスイベントは、Tkオブジェクトに対して次の様に指定します。
第一引数に対し、"<Button>"でクリックを検知、"<Motion>"でマウスの移動を検知します。
第二引数には、イベント発生タイミングで実行したい関数を指定します。

```python:main.py(抜粋)
root.bind("<Button>", on_mouse_clicked) # マウス(Click)
root.bind("<Motion>", on_mouse_moved) # マウス(Motion)
```

### 1, Buttonイベント

Buttonイベントを受け取る、"on_mouse_clicked()"関数では、
"e.x"でx座標を、"e.y"でy座標を取得しています。

```python:main.py(抜粋)
def on_mouse_clicked(e):
    print("Clicked:", e.x, e.y)
```

クリックをする都度、その座標がShellに表示されていきます。

![](/images/0fc9f54eefe9fd/03_01.png)

### 2, Motionイベント

Motionイベントを受け取る、"on_mouse_moved()"関数では、
その座標をグローバル変数"mx", "my"にコピーしています。
(globalを忘れずに...)

```python:main.py(抜粋)
def on_mouse_moved(e):
    global mx, my
    mx, my = e.x, e.y # グローバル変数にコピー
```

"update()"関数では、"mx"と、"my"に格納された座標をキャンバスに描画しています。
"cvs.create_text()"関数の引数は、x座標、y座標、
"text"には表示する文字列、"font"にはフォント名とサイズを指定します。
"tag"には、テキスト描画オブジェクトに付ける目標として、"hud"という文字列を指定します。

ここで、この"tag"について説明します。
"update()"関数の最初にある、"cvs.delete("hud")"に着目してください。
これは、"tag"が"hud"である描画オブジェクトを画面から消去する命令です。
つまり、一旦"hud"タグのオブジェクトを削除し、あらためてマウス位置に再描画する処理になっています。

```python:main.py(抜粋)
def update():
    """ 更新関数 """
    cvs.delete("hud") # "hud"タグの描画オブジェクトを消去

    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 画面更新
    root.after(30, update)
```

この時点で実行すると、ゲーム画面上のマウス位置に座標が描画されます。

![](/images/0fc9f54eefe9fd/03_02.gif)

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python:main.py(完成コード)
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

def init():
    """ 初期化関数 """
    global bg_photo, bg_image

    # 背景
    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)
    
def update():
    """ 更新関数 """
    cvs.delete("hud") # "hud"タグの描画オブジェクトを消去

    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 画面更新
    root.after(F_INTERVAL, update)

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
:::

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「スプライトを作ってみよう」です。
お楽しみに!!