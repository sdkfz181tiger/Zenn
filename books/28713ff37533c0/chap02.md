---
title: "第2章: ゲーム画面を作ってみよう"
---

# ゲーム画面を作ってみよう

今回は、ゲーム画面を作ります。

## 1, 作業用フォルダを用意する

作業用フォルダを用意し、"main.py"ファイルを作ります。
ファイルの作り方に関しては、[プログラムをファイルに保存する](https://zenn.dev/sdkfz181tiger/books/c4a251dd2b1b94/viewer/chap99#4%2C-%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AB%E4%BF%9D%E5%AD%98%E3%81%99%E3%82%8B)を参考にしてください。

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　└ main.py <- プログラムを記述するファイル
```

以降、"main.py"ファイルにコードを記述していきます。

## 2, GameViewを用意する

"GameView"クラスは、ゲームのライフサイクルを実現するクラスです。
それぞれのメソッドには次の処理を実装していきます。

| メソッド名 | 役割 | 具体的な処理 |
| ---- | ---- | ---- |
| \_\_init\_\_ | 初期化 | スコアやキャラクターの初期化等 |
| on_key_press | キーボードを押した時 | プレイヤーの移動 |
| on_key_release | キーボードを離した時 | プレイヤーの停止 |
| on_update | 更新処理 | キャラクター等の座標移動 |
| on_draw | 描画処理 | キャラクター等の描画 |

```python:main.py(抜粋)
import arcade
import math
import random

W, H = 480, 320 # ゲーム画面の幅と高さ
TITLE = "Hello, Arcade!!" # タイトル

class GameView(arcade.View):

    def __init__(self):
        """ 初期化 """
        super().__init__()
        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

    def on_key_press(self, key, key_modifiers):
        """ キーを押した時 """
        pass

    def on_key_release(self, key, key_modifiers):
        """ キーを離した時 """
        pass

    def on_update(self, delta_time):
        """ 更新処理 """
        pass

    def on_draw(self):
        """ 描画処理 """
        self.clear() # Clear
```

コンストラクタである、"\_\_init\_\_"では、
ゲーム画面の背景色を指定しています。

```python:main.py(抜粋)
# 背景色
self.background_color = arcade.color.PAYNE_GREY
```

RGBカラーでも指定は可能ですが、[arcade.color](https://api.arcade.academy/en/stable/api_docs/arcade.color.html)から好きな色を直接指定することができます。

"on_update()"で更新処理(1秒間に沢山実行)を行います。
引数の"delta_time"は、フレームとフレームの感覚(秒数)が格納されています。

"on_draw()"メソッドで、画面の描画を行います。
この時点では、画面全体をクリア(背景色で塗りつぶす)しています。

```python:main.py(抜粋)
self.clear() # Clear
```

## 3, ゲーム画面を用意する

"main()"関数でゲーム画面を用意します。

具体的なコードは次のとおりです。

```python:main.py(抜粋)
def main():
    """ メイン処理 """

    # Window
    window = arcade.Window(W, H, TITLE)

    # GameView
    game = GameView()

    # Show
    window.show_view(game)

    # Run
    arcade.run()
```

最初に、"arcade.Window()"メソッドを実行しゲームウィンドウを作ります。
引数にはそれぞれ、画面の幅、高さを指定します。

次に、"window.show_view()"メソッドで、先ほどの"GameView"インスタンスを指定し、
"arcade.run()"でゲームが実行されます。

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python:main.py(完成コード)
import arcade
import math
import random

W, H = 480, 320 # ゲーム画面の幅と高さ
TITLE = "Hello, Arcade!!" # タイトル

class GameView(arcade.View):

    def __init__(self):
        """ 初期化 """
        super().__init__()
        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

    def on_key_press(self, key, key_modifiers):
        """ キーを押した時 """
        pass

    def on_key_release(self, key, key_modifiers):
        """ キーを離した時 """
        pass

    def on_update(self, delta_time):
        """ 更新処理 """
        pass

    def on_draw(self):
        """ 描画処理 """
        self.clear() # Clear

def main():
    """ メイン処理 """

    # Window
    window = arcade.Window(W, H, TITLE)

    # GameView
    game = GameView()

    # Show
    window.show_view(game)

    # Run
    arcade.run()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/28713ff37533c0/02_01.png)

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「背景を表示しよう」です。
お楽しみに!!
