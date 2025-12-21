---
title: "第13章(番外編): カメラを使おう"
---

# カメラを使おう

今回は、カメラを使ってプレイヤーを追尾させます。
カメラを使う事で、ゲーム画面を広く使うことができるようになります。

## 1, 2つのカメラを作る

カメラオブジェクトは、ゲーム中の表示範囲を決めるオブジェクトです。

"main.py"の"GameView"のコンストラクタでは、
プレイヤー等を追尾させる"self.camera"オブジェクトと、
GUI等を固定表示させるための"self.camera_gui"オブジェクトの2つのカメラを用意します。

```python:main.py(抜粋)
# Camera
self.camera = arcade.Camera2D() # プレイヤー用カメラ
self.camera_gui = arcade.Camera2D() # 固定したカメラ
```

## 2, カメラをプレイヤーに追尾させる

次に、"on_update()"メソッドで、カメラオブジェクトにプレイヤーの座標を追尾する処理を実装します。
最後の"0.1"の部分を調整する事で、カメラの移動速度を調整することができます。

```python:main.py(抜粋)
# プレイヤー用カメラの座標をプレイヤーに追わせる
self.camera.position = arcade.math.lerp_2d(
	self.camera.position, self.player.position, 0.1)
```

## 3, カメラを有効にする

最後に、"on_draw()"メソッドで、2つのカメラいずれかの利用を決めます。
"self.camera.use()"の後に描画をすれば、カメラに追随し、
"self.camera_gui.use()"の後に描画を行えば、定位置に描画されます。

```python:main.py(抜粋)
def on_draw(self):
    self.clear() # Clear

    self.camera.use() # プレイヤー用カメラを使う
    self.players.draw()
    self.coins.draw()

    self.camera_gui.use() # 固定したカメラを使う
    self.msg_info.draw()
```

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。
コードをそのままコピーしても動作します。

:::details 完成コード
```python:sprite.py(完成コード)
import arcade
import random
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
        # Animation
        self.anim_counter = 0
        self.anim_interval = 4
        self.anim_index = 0
        self.anim_key = ""
        self.anim_pause = True
        self.anims = {}

    def update(self, delta_time):
        """ Update """
        self.center_x += self.vx * delta_time
        self.center_y += self.vy * delta_time
        # Animation
        self.update_animation()

    def move(self, spd, deg, tag=""):
        """ Move Sprite """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)
        if tag: self.change_animation(tag)

    def stop(self):
        """ Stop Sprite """
        self.vx = 0
        self.vy = 0
        self.stop_animation()

    def update_animation(self):
        """ Update Animation """
        if not self.anim_key in self.anims: return
        if self.anim_pause: return
        self.anim_counter += 1
        if(self.anim_counter < self.anim_interval): return
        self.anim_counter = 0
        self.anim_index += 1
        anim = self.anims[self.anim_key]
        if len(anim) <= self.anim_index: self.anim_index = 0
        self.texture = anim[self.anim_index]

    def load_animation(self, key, filename, num):
        """ Load Animation """
        anim = []
        for i in range(num):
            path = filename.format(i+1)
            anim.append(arcade.load_texture(path))
        self.anims[key] = anim

    def change_animation(self, key):
        """ Change Animation """
        if not key in self.anims: return
        self.anim_counter = 0
        self.anim_index = 0
        self.anim_key = key
        self.texture = self.anims[key][0]
        self.start_animation()

    def start_animation(self):
        """ Start Animation """
        self.anim_pause = False

    def stop_animation(self):
        """ Stop Animation """
        self.anim_pause = True

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        # Animation
        self.load_animation("front", "images/ninja/front_{:02d}.png", 5)
        self.load_animation("left", "images/ninja/left_{:02d}.png", 5)
        self.load_animation("right", "images/ninja/right_{:02d}.png", 5)
        self.load_animation("back", "images/ninja/back_{:02d}.png", 5)
        self.change_animation("front")

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        # Animation
        self.load_animation("coin", "images/coin/coin_{:02d}.png", 5)
        self.change_animation("coin")
```

```python:main.py(完成コード)
import arcade
import random
import sprite

PLAYER_SPEED = 90

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height

        self.background_color = arcade.color.PAYNE_GREY

        # Camera
        self.camera = arcade.Camera2D() # プレイヤー用カメラ
        self.camera_gui = arcade.Camera2D() # 固定したカメラ

        # Player
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png", 
                             self.w/2, self.h/2)
        self.players.append(self.player)

        # Coin
        self.coins = arcade.SpriteList()
        for i in range(10):
            x = random.random() * self.w
            y = random.random() * self.h
            coin = sprite.Coin("images/coin/coin_01.png", x, y)
            self.coins.append(coin)

         # Info
        self.msg_info = arcade.Text(
            "GAME", 
            self.w/2, self.h-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Move(WASD)
        if key == arcade.key.W: self.player.move(PLAYER_SPEED, 90, "back")
        if key == arcade.key.A: self.player.move(PLAYER_SPEED, 180, "left")
        if key == arcade.key.S: self.player.move(PLAYER_SPEED, 270, "front")
        if key == arcade.key.D: self.player.move(PLAYER_SPEED, 0, "right")

    def on_key_release(self, key, key_modifiers):
        self.player.stop() # Stop

    def on_update(self, delta_time):

        self.players.update(delta_time)
        self.coins.update(delta_time)

        # プレイヤー用カメラの座標をプレイヤーに追わせる
        self.camera.position = arcade.math.lerp_2d(
            self.camera.position, self.player.position, 0.1)

    def on_draw(self):
        self.clear() # Clear

        self.camera.use() # プレイヤー用カメラを使う
        self.players.draw()
        self.coins.draw()

        self.camera_gui.use() # 固定したカメラを使う
        self.msg_info.draw()

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    window.show_view(GameView(window)) # GameView
    arcade.run()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/28713ff37533c0/13_01.gif)

# 終わりに...

ここまで読んでいただき、ありがとうございました。
この連載が、ゲーム開発のきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว
(よろしければ👍頂けると大変励みになります!!)