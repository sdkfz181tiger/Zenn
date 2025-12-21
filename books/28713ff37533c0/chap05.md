---
title: "第5章: プレイヤーを動かしてみよう"
---

# プレイヤーを動かしてみよう

今回は、プレイヤーを動かします。

## 1, プレイヤースプライトを改良する

最初に、"math"モジュールをインポートします。
このモジュールは、数学的計算を手軽に扱える定番モジュールの一つです。

```python:python:sprite.py(抜粋)
import math # 数学的計算をするモジュール
```

## 2, 移動速度を格納する変数を追加する

ここからは、スプライトの基底クラス"BaseSprite"に機能を追加していきます。

コンストラクタでは、
x方向の速度を格納する変数"vx"と、
y方向の速度を格納する変数"vy"を追加します。

```python:sprite.py(BaseSpriteに追加)
def __init__(self, filename, x, y):
    super().__init__(filename)
    # Position
    self.center_x = x
    self.center_y = y
    # Velocity
    self.vx = 0 # x方向の速度
    self.vy = 0 # y方向の速度
```

## 3, 更新メソッドで座標に速度を加算する

"update()"メソッドを追加し、速度を座標に適用する処理を実装します。

```python:sprite.py(BaseSpriteに追加)
def update(self, delta_time):
    """ Update """
    self.center_x += self.vx * delta_time # x座標を更新
    self.center_y += self.vy * delta_time # y座標を更新
```

ここでは、x,y座標に対して"vx"と"vy"に"delta_time"を掛けた値を加算しています。
"delta_time"は、前フレームからの経過時間です。
つまり、約1秒後に"vx"、"vy"分だけの距離を移動する事になります。
(毎フレーム実行し続けることで、座標が少しづつ変化するという訳ですね)

## 4, 移動を開始するメソッドを用意する

"move()"メソッドを追加し、移動速度と角度を指定する処理を実装します。
このメソッドは、引数に"速度"、"角度"を指定して実行します。
なお、角度は"右方向を0°"として、反時計回りに増えていきます。

```python:sprite.py(BaseSpriteに追加)
def move(self, spd, deg):
    """ Move Sprite """
    rad = deg * math.pi / 180 # 度数法から弧度法へ変換
    self.vx = spd * math.cos(rad) # x方向の速度
    self.vy = spd * math.sin(rad) # y方向の速度
```

"math"モジュールの"math.pi"は"円周率"のことです。
これを使って度数法(0° ~ 360°)を、弧度法(0 ~ 2π)へ変換しています。

次に、spd(速度)に対し、"cos"を掛け算し、"x"方向の速度として"vx"に代入します。
同様にして、"sin"を掛け算し、"y"方向の速度として"vy"に代入しています。
("cos"や、"sin"が出てくるのはここだけなので、深追いしなくても大丈夫ですよ)

## 5, 停止するメソッドを用意する

"stop()"メソッドを追加し、停止する処理を実装します。
このメソッドでは、単純に"vx"と、"vy"に0を代入しているだけです。

```python:sprite.py(BaseSpriteに追加)
def stop(self):
    """ Stop Sprite """
    self.vx = 0 # x方向の速度を0に
    self.vy = 0 # y方向の速度を0に
```

## 6, テストしてみる

最後に、"main.py"で動作確認をしてみます。
"player.move()"の引数に、速度"90"、角度"30"を指定し実行します。

```python:main.py(抜粋)
# プレイヤースプライト
self.players = arcade.SpriteList()
self.player = sprite.Player("images/ninja/front_01.png",
                            x=self.w/2, y=self.h/2)
self.players.append(self.player)

self.player.move(90, 30) # プレイヤーを移動させてみる
```

この場合、"1秒あたり90ピクセルの速さで、右上方向30°に移動"します。
他の値で是非試してみてください。

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python:sprite.py(完成コード)
import arcade
import math # 数学的計算をするモジュール

class BaseSprite(arcade.Sprite):

    def __init__(self, filename, x, y):
        super().__init__(filename)
        # Position
        self.center_x = x
        self.center_y = y
        # Velocity
        self.vx = 0 # x方向の速度
        self.vy = 0 # y方向の速度

    def update(self, delta_time):
        """ Update """
        self.center_x += self.vx * delta_time # x座標を更新
        self.center_y += self.vy * delta_time # y座標を更新

    def move(self, spd, deg):
        """ Move Sprite """
        rad = deg * math.pi / 180 # 度数法から弧度法へ変換
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度

    def stop(self):
        """ Stop Sprite """
        self.vx = 0 # x方向の速度を0に
        self.vy = 0 # y方向の速度を0に

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
```

```python:main.py(完成コード)
import arcade
import sprite

class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景スプライト
        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = self.w / 2
        bkg.center_y = self.h / 2
        self.backgrounds.append(bkg)

        # プレイヤースプライト
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=self.w/2, y=self.h/2)
        self.players.append(self.player)

        self.player.move(90, 30) # プレイヤーを移動させてみる

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        self.players.update()

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw()

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    game = GameView(window)
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/28713ff37533c0/05_01.gif)

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「プレイヤーをコントロールしよう」です。
お楽しみに!!
(よろしければ👍頂けると大変励みになります!!)