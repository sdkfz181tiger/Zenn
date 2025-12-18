---
title: "第3章: 背景画像を表示しよう"
---

# 背景画像を表示しよう

今回は、背景画像を表示します。

## 1, 背景画像を用意する

作業用フォルダに、"images"フォルダを作ります。
画像素材はこのフォルダにまとめていきます。

背景画像として、以下の画像をお使いください。(今回の舞台は和風!!)

![](/images/28713ff37533c0/bg_temple.png)

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　└ images/
　 　└ bg_temple.png <- 背景画像
```

## 2, SpriteListとSprite

ゲーム画面に登場するキャラクターや背景などは、全て"arcade.Sprite"クラスで作ります。
複数のスプライトをまとめて管理、描画するために、"arcade.SpriteList"を使います。

```python:main.py(抜粋)
# 背景リストを用意する
self.backgrounds = arcade.SpriteList()
```

次に、"arcade.Sprite"クラスでスプライトを作ります。
引数には、画像へのパス(先ほどの背景画像)を指定します。
生成されたスプライトに対してx, y座標を指定します。

```python:main.py(抜粋)
# 背景スプライトを作る
bkg = arcade.Sprite("images/bg_temple.png")
bkg.center_x = W/2
bkg.center_y = H/2
```

最後に、先ほどのリストに背景スプライトを追加します。

```python:main.py(抜粋)
self.backgrounds.append(bkg)# 背景リストに追加する
```

## 3, SpriteListを描画する

GameViewの、"on_draw()"メソッドで、リストに追加されたスプライトを一括で描画します。
(Arcadeの分かりやすいポイントの一つです)

```python:main.py(抜粋)
self.backgrounds.draw() # 背景リストを描画
```

この時点で、背景画像がゲーム画面に描画されます。

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python:main.py(完成コード)
import arcade

W, H = 480, 320 # ゲーム画面の幅と高さ
TITLE = "Hello, Arcade!!" # タイトル

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景リストを用意する
        self.backgrounds = arcade.SpriteList()

        # 背景スプライトを作る
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = W/2
        bkg.center_y = H/2

        self.backgrounds.append(bkg)# 背景リストに追加する

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw() # 背景リストを描画

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

![](/images/28713ff37533c0/03_01.png)

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「プレイヤーを用意しよう」です。
お楽しみに!!