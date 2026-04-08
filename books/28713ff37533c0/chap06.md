---
title: "第6章: プレイヤーをコントロールしよう"
---

# プレイヤーをコントロールしよう

今回は、プレイヤーをキーボードで動かします。

## 1, キーボードが押されたら移動

GameViewクラスにある、"on_key_press()"メソッドは、
キーボードのボタンが押されるタイミングで、実行されます。
引数の"key"には、押されたボタンの種類が格納されています。

```python:python:main.py(抜粋)
def on_key_press(self, key, key_modifiers):
    # Move(WASD)
    if key == arcade.key.W: self.player.move(90, 90) # 上へ
    if key == arcade.key.A: self.player.move(90, 180) # 左へ
    if key == arcade.key.S: self.player.move(90, 270) # 下へ
    if key == arcade.key.D: self.player.move(90, 0) # 右へ
```

ここでは、Wキーで上方向(90°)、Aキーで左方向(180°)、Sキーで下方向(270°)、Dキーで右方向(0°)へ移動する判定を実装します。
速度は全て"90"に指定しています(1秒間に90ピクセル移動するイメージです)。
(仕組みがわかったら、斜め移動が出来るように調整してみましょう)

## 2, キーボードを離したら停止

"on_key_released()"メソッドは、
キーボードを離したタイミングで実行されます。

```python:python:main.py(抜粋)
def on_key_release(self, key, key_modifiers):
    self.player.stop() # 停止
```

ここでは、BaseSpriteに実装した"stop()"メソッドを実行しています。

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。
コードをそのままコピーしても動作します。

:::details 完成コード
```python:sprite.py(完成コード)
import arcade
import math

class BaseSprite(arcade.Sprite):

    def __init__(self, filename, x, y):
        super().__init__(filename)
        # Position
        self.center_x = x
        self.center_y = y
        # Velocity
        self.vx = 0
        self.vy = 0

    def update(self, delta_time):
        """ Update """
        self.center_x += self.vx * delta_time
        self.center_y += self.vy * delta_time

    def move(self, spd, deg):
        """ Move Sprite """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

    def stop(self):
        """ Stop Sprite """
        self.vx = 0
        self.vy = 0

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

    def on_key_press(self, key, key_modifiers):
        # Move(WASD)
        if key == arcade.key.W: self.player.move(90, 90) # 上へ
        if key == arcade.key.A: self.player.move(90, 180) # 左へ
        if key == arcade.key.S: self.player.move(90, 270) # 下へ
        if key == arcade.key.D: self.player.move(90, 0) # 右へ

    def on_key_release(self, key, key_modifiers):
        self.player.stop() # 停止

    def on_update(self, delta_time):
        self.players.update(delta_time)

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

![](/images/books/28713ff37533c0/06_01.gif)

# 次回は...

ここまで読んでいただき、ありがとうございました。
次回のタイトルは「小判をゲットしよう」です。
お楽しみに👍