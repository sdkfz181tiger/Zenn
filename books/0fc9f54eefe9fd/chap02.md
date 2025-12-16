---
title: "第2章: ゲーム画面を作ってみよう"
---

# ゲーム画面を作ってみよう

今回は、"Tkinter"の"Canvas"を使ってゲーム画面を作ります。

## 1, 作業用フォルダを用意する

作業用フォルダを用意し、"main.py"ファイルを作ります。
ファイルの作り方に関しては、[プログラムをファイルに保存する](https://zenn.dev/sdkfz181tiger/books/c4a251dd2b1b94/viewer/chap99#4%2C-%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AB%E4%BF%9D%E5%AD%98%E3%81%99%E3%82%8B)を参考にしてください。

次に、"images"フォルダを作ります。
画像素材はこのフォルダにまとめていきます。

背景画像として、以下の画像をお使いください。(どこかで見た様な地獄の雰囲気!!)

![](/images/0fc9f54eefe9fd/bg_jigoku.png)

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py <- プログラムを記述するファイル
　└ images/
　 　└ bg_jigoku.png <- 背景画像
```

以降、"main.py"ファイルにコードを記述していきます。

## 2, Tkinterオブジェクトを作る

先ずは、"Tkinter"ライブラリをインポートし、"tkinter.Tk()"関数でオブジェクトを作ります。

次の例では、生成されたオブジェクト"root"に対し、タイトルの指定、画面リサイズの無効化を行っています。

```python: main.py
import tkinter

root = tkinter.Tk() # tkinterオブジェクトを作る
root.title("Hello, Tkinter!!") # ゲーム画面のタイトル
root.resizable(False, False) # 画面リサイズを無効化する
```

## 3, キャンバスを作る

あらかじめ、ゲーム画面の幅として"W"、高さとして"H"変数を用意しておきます。
(こうしておくと後々便利です!!)

次に、"tkinter.Canvas()"関数を使ってキャンバスを作ります。
引数には、キャンバスの幅(width)、高さ(height)、背景色(bg)を指定します。

この時点で実行すると、幅480px x 高さ320pxのゲーム画面が表示されます。

```python: main.py
import tkinter

# キャンバスの幅と高さ
W, H = 480, 320

root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black") # キャンバスを作る
cvs.pack() # キャンバスを配置する
root.mainloop() # tkinterを起動する
```

今後は、このキャンバスに対して背景画像やキャラクターの画像を描画していきます。

![](/images/0fc9f54eefe9fd/02_01.png)

## 4, 初期化関数を用意する

ゲーム開始時に実行する"初期化関数"と、画面を更新し続ける"更新関数"を用意します。
初期化部分と、更新部分を明確に分離することでコード全体がスッキリします。

用意した"init()"関数にある"pass"は、"何もしない"という意味です。
(今は中身がありませんが、今後はここにコードを追加していきます)

```python: main.py
import tkinter

W, H = 480, 320

def init():
    """ 初期化関数 """
    pass

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init() # 初期化関数を実行
update() # 更新関数を実行
root.mainloop()
```

## 5, 更新関数を用意する

次に、フレームレートとして、"F_RATE"を決めます。
フレームレートとは、"1秒間に画面更新する回数"のことです。
フレームレートは60程度が望ましいですが、今回は練習なので30としています。

"F_INTERVAL"は、1フレームにおける更新間隔です。(単位はミリ秒)
画面を更新する都度、キャラクターの座標を変更しつづける事で、キャラクターが動いている様に見えるのですね。

"update()"関数には、"root.after(F_INTERVAL, update)"と記述します。
これは、"F_INTERVALミリ秒後に、update()関数を再実行"するという命令です。
これ以降は、キャラクターの位置の更新等を行います。

```python: main.py
import tkinter

W, H = 480, 320

# フレームレート
F_RATE = 30 # 1秒間に実行するフレーム回数
F_INTERVAL = int(1000 / F_RATE) # 1フレームの間隔

def init():
    """ 初期化関数 """
    pass

def update():
    """ 更新関数 """
    # 画面更新
    root.after(F_INTERVAL, update)

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init() # 初期化関数を実行
update() # 更新関数を実行
root.mainloop()
```

## 6, 背景画像を配置する

先ほど用意した、"初期化関数"で背景画像の読み込みと配置を行います。
利用する画像は、imagesフォルダに配置した"bg_jigoku.png"です。

"init()"関数の最初にある"global"は、関数外の変数(グローバル変数)を利用するという意味です。
"global"の記述が無い場合、"ローカル変数"として扱われ、画像が開放されてしまうので注意が必要です。
(画像が表示されません)

"tkinter.PhotoImage()"関数では、画像ファイルの読み込みを行っています。
引数の"file"には、画像ファイルまでのパスを指定します。

"cvs.create_image()"関数は、読み込んだ画像をキャンバスに配置する命令です。
第一引数はx座標(左右中央にするためにW/2)、第二引数はy座標(上下中央にするためにH/2)、"image"には読み込んだ画像オブジェクトを指定します。

```python:main.py(抜粋)
# 背景画像とイメージ(グローバル変数)
bg_photo, bg_image = None, None

def init():
    """ 初期化関数 """
    global bg_photo, bg_image # グローバル変数を指定

    # 背景
    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)
```

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。(地獄にようこそ!!)

:::details 完成コード
```python: main.py
import tkinter

# キャンバスの幅と高さ
W, H = 480, 320

# フレームレート
F_RATE = 30 # 1秒間に実行するフレーム回数
F_INTERVAL = int(1000 / F_RATE) # 1フレームの間隔

# 背景画像とイメージ(グローバル変数)
bg_photo, bg_image = None, None

def init():
    """ 初期化関数 """
    global bg_photo, bg_image # グローバル変数を指定

    # 背景
    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)

def update():
    """ 更新関数 """
    # 画面更新
    root.after(F_INTERVAL, update)

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
```
:::

![](/images/0fc9f54eefe9fd/02_02.png)

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「マウスイベントを使ってみよう」です。
お楽しみに!!