---
title: "第14章(番外編): 物理エンジンを使おう"
---

# 物理エンジンを使おう

今回は、物理エンジンについて紹介します。
物理法則に則った動きをスプライトに与えることができます。

## 1, 物理エンジンを作る

大元となる、"arcade.PymunkPhysicsEngine()"メソッドで、物理エンジンを作ります。
引数にある、"gravity"は、物理世界における"重力"です。

```python:main.py(抜粋)
# 物理エンジンを作る
self.physics = arcade.PymunkPhysicsEngine(damping=0.8, gravity=(0, -900))
```

## 2, プレイヤーを追加する

"add_sprite()"メソッドを使って、スプライトを追加します。

```python:main.py(抜粋)
# プレイヤーを追加
self.physics.add_sprite(self.player, 
	friction=1.0, collision_type="player")
```

## 3, 小判とブロックを追加する

先ほどと同じ要領で、小判とブロックを追加します。
"body_type"には、以下の通り、DYNAMIC/STATICのいずれかを指定します。

| 設定値 | 意味 |
| ---- | ---- |
| arcade.PymunkPhysicsEngine.DYNAMIC | 物理の影響を受ける物体(動くもの) |
| arcade.PymunkPhysicsEngine.STATIC | 物理の影響を受ない物体(止まっているもの) |

小判の場合は、"DYNAMIC"とし、ブロックは"STATIC"とします。

```python:main.py(抜粋)
# 小判を追加
for coin in self.coins:
    self.physics.add_sprite(coin,
        friction=1.0, collision_type="coin",
        body_type=arcade.PymunkPhysicsEngine.DYNAMIC)
# ブロックを追加
for block in self.blocks:
    self.physics.add_sprite(block,
        friction=1.0, collision_type="block",
        body_type=arcade.PymunkPhysicsEngine.STATIC)
```

ブロックの画像は次のものをお使いください。(忍者と言えば瓦です!!)

| 画像 | ファイル名 |
| ---- | ---- |
| ![](/images/28713ff37533c0/block/block_01.png) | block_01.png |

## 4, プレイヤーに速度を与える

"on_key_press()"メソッドでは、プレイヤーに対して瞬間的な速度を与える処理を実装します。

"self.physics.set_velocity()"の第一引数にはプレイヤースプライトを、
第二引数には速度(ベクトル)を指定します。

```python:main.py(抜粋)
PLAYER_JUMP_X = 60
PLAYER_JUMP_Y = 300

# 中略

def on_key_press(self, key, key_modifiers):
    # Move(WASD)
    if key == arcade.key.W: 
        self.physics.set_velocity(self.player, (0, PLAYER_JUMP_Y))
    if key == arcade.key.A:
        self.physics.set_velocity(self.player, (-PLAYER_JUMP_X, PLAYER_JUMP_Y))
    if key == arcade.key.S:
        pass
    if key == arcade.key.D:
        self.physics.set_velocity(self.player, (PLAYER_JUMP_X, PLAYER_JUMP_Y))
```

## 5, 物理エンジンを実行する

最後に、"on_update()"メソッド内で物理エンジンをステップ実行して完成です。

```python:main.py(抜粋)
self.physics.step(delta_time) # 物理エンジンを進める
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

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

class Block(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
```

```python:main.py(完成コード)
import arcade
import random
import sprite

PLAYER_JUMP_X = 60
PLAYER_JUMP_Y = 300

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

        # プレイヤー
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png", 
                             self.w/2, self.h/2)
        self.players.append(self.player)

        # 小判
        self.coins = arcade.SpriteList()
        for i in range(10):
            x = random.random() * self.w
            y = self.h
            coin = sprite.Coin("images/coin/coin_01.png", x, y)
            self.coins.append(coin)

        # ブロック
        block_pad_x = 48
        block_total = 8
        block_x = self.w / 2 - block_pad_x * (block_total-1) / 2
        block_y = 30
        self.blocks = arcade.SpriteList()
        for i in range(block_total):
            x = block_x + block_pad_x * i
            y = block_y
            block = sprite.Block("images/block/block_01.png", x, y)
            self.blocks.append(block)

        # Info
        self.msg_info = arcade.Text(
            "GAME", 
            self.w/2, self.h-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

        # 物理エンジンを作る
        self.physics = arcade.PymunkPhysicsEngine(damping=0.8, gravity=(0, -900))
        # プレイヤーを追加
        self.physics.add_sprite(self.player, 
            friction=1.0, collision_type="player")
        # 小判を追加
        for coin in self.coins:
            self.physics.add_sprite(coin,
                friction=1.0, collision_type="wall",
                body_type=arcade.PymunkPhysicsEngine.DYNAMIC)
        # ブロックを追加
        for block in self.blocks:
            self.physics.add_sprite(block,
                friction=1.0, collision_type="wall",
                body_type=arcade.PymunkPhysicsEngine.STATIC)

    def on_key_press(self, key, key_modifiers):
        # Move(WASD)
        if key == arcade.key.W: 
            self.physics.set_velocity(self.player, (0, PLAYER_JUMP_Y))
        if key == arcade.key.A:
            self.physics.set_velocity(self.player, (-PLAYER_JUMP_X, PLAYER_JUMP_Y))
        if key == arcade.key.S:
            pass
        if key == arcade.key.D:
            self.physics.set_velocity(self.player, (PLAYER_JUMP_X, PLAYER_JUMP_Y))
        
    def on_key_release(self, key, key_modifiers):
        self.player.stop() # Stop

    def on_update(self, delta_time):

        self.physics.step(delta_time) # 物理エンジンを進める

        # Camera
        self.camera.position = arcade.math.lerp_2d(
            self.camera.position, self.player.position, 0.1)

    def on_draw(self):
        self.clear() # Clear

        self.camera.use()
        self.players.draw()
        self.coins.draw()
        self.blocks.draw()

        self.camera_gui.use()
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

![](/images/28713ff37533c0/14_01.gif)

# 終わりに...

ここまで読んでいただき、ありがとうございました。
この連載が、ゲーム開発のきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว👍