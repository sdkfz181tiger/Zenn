---
title: "第15章(番外編): 物理エンジンを使おう_ひよこ&ケーキ"
---

# 物理エンジンを使おう_ひよこ&ケーキ

前回に引き続き、物理エンジンを使ったサンプルを紹介します。
ジャンプでケーキタワーを作るシンプルなサンプルです。

## 1, 画像素材

ひよこの画像は次のものをお使いください。

### 1-1, ひよこ着地

|  | ファイル名 |  | ファイル名 |  | ファイル名 |  | ファイル名 |  | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/books/28713ff37533c0/hiyoko/land_01.png) | land_01.png | ![](/images/books/28713ff37533c0/hiyoko/land_02.png) | land_02.png | ![](/images/books/28713ff37533c0/hiyoko/land_03.png) | land_03.png | ![](/images/books/28713ff37533c0/hiyoko/land_04.png) | land_04.png | ![](/images/books/28713ff37533c0/hiyoko/land_05.png) | land_05.png |

### 1-2, ひよこジャンプ

|  | ファイル名 |  | ファイル名 |  | ファイル名 |  | ファイル名 |  | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/books/28713ff37533c0/hiyoko/jump_01.png) | jump_01.png | ![](/images/books/28713ff37533c0/hiyoko/jump_02.png) | jump_02.png | ![](/images/books/28713ff37533c0/hiyoko/jump_03.png) | jump_03.png | ![](/images/books/28713ff37533c0/hiyoko/jump_04.png) | jump_04.png | ![](/images/books/28713ff37533c0/hiyoko/jump_05.png) | jump_05.png |

### 1-3, 背景の星

|  | ファイル名 |  | ファイル名 |  | ファイル名 |  | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/books/28713ff37533c0/hiyoko/star_01.png) | star_01.png | ![](/images/books/28713ff37533c0/hiyoko/star_02.png) | star_02.png | ![](/images/books/28713ff37533c0/hiyoko/star_03.png) | star_03.png | ![](/images/books/28713ff37533c0/hiyoko/star_04.png) | star_04.png |

### 1-4, ケーキ

|  | ファイル名 |  | ファイル名 |  | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/books/28713ff37533c0/hiyoko/cake_01.png) | cake_01.png | ![](/images/books/28713ff37533c0/hiyoko/cake_02.png) | cake_02.png | ![](/images/books/28713ff37533c0/hiyoko/cake_03.png) | cake_03.png |

### 1-5, テーブル

|  | ファイル名 |
| ---- | ---- |
| ![](/images/books/28713ff37533c0/hiyoko/table_01.png) | table_01.png |

### 1-6, カーペット

|  | ファイル名 |
| ---- | ---- |
| ![](/images/books/28713ff37533c0/hiyoko/carpet_01.png) | carpet_01.png |

## 2, 音源素材

レトロゲーム風のフリーサウンドはここがオススメです!!
お好みのBGMや、SEはこちらからダウンロードして使いましょう。
(利用規約を確認して利用してください)

[しーでんでん8bitフリーサウンド](https://seadenden-8bit.com/)

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。
コードをそのままコピーしても動作します。

:::details 完成コード
```python:sprite.py(完成コード)
# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import math

class Background(arcade.Sprite):

    def __init__(self, filename, x, y):
        super().__init__(filename)
        # Position
        self.center_x = x
        self.center_y = y


class BaseSprite(arcade.Sprite):

    def __init__(self, physics, filename, x, y):
        super().__init__(filename)
        # Physics
        self.physics = physics
        # Position
        self.center_x = x
        self.center_y = y
        # Animation
        self.anim_interval_cnt = 0
        self.anim_interval_limit = 6
        self.anim_textures = {}
        self.anim_key = "" # Key of Animation

    def change_animation(self, key):
        if not key in self.anim_textures: return
        self.anim_key = key
        self.cur_texture = 0
        self.texture = self.anim_textures[self.anim_key][0]

    def update_animation(self, delta_time: float=1/60):
        # Textures
        textures = self.anim_textures[self.anim_key]

        # Interval
        self.anim_interval_cnt += 1
        if self.anim_interval_cnt < self.anim_interval_limit: return
        self.anim_interval_cnt = 0
        # Frames
        self.cur_texture += 1
        if self.cur_texture >= len(textures):
            self.cur_texture = 0
        self.texture = textures[self.cur_texture]

    def stop(self):
        self.physics.set_velocity(self, (0, 0))

    def check_body_type(self, body_type):
        return self.physics.get_physics_object(self).body.body_type == body_type


class Player(BaseSprite):

    def __init__(self, physics, filename, x, y):
        super().__init__(physics, filename, x, y)
        # Physics
        self.physics.add_sprite(self, 
            friction=1.0, collision_type="player")

        self.anim_textures["land"] = [
            arcade.load_texture("images/cake_x2/land_01.png"),
            arcade.load_texture("images/cake_x2/land_02.png"),
            arcade.load_texture("images/cake_x2/land_03.png"),
            arcade.load_texture("images/cake_x2/land_04.png"),
            arcade.load_texture("images/cake_x2/land_05.png"),
        ]

        self.anim_textures["jump"] = [
            arcade.load_texture("images/cake_x2/jump_01.png"),
            arcade.load_texture("images/cake_x2/jump_02.png"),
            arcade.load_texture("images/cake_x2/jump_03.png"),
            arcade.load_texture("images/cake_x2/jump_04.png"),
            arcade.load_texture("images/cake_x2/jump_05.png"),
        ]

        self.change_animation("land")


class Block(BaseSprite):

    def __init__(self, physics, filename, x, y):
        super().__init__(physics, filename, x, y)
        # Physics
        self.physics.add_sprite(self,
            friction=1.0, collision_type="block",
            body_type=arcade.PymunkPhysicsEngine.STATIC)


class Cake(BaseSprite):

    def __init__(self, physics, filename, x, y):
        super().__init__(physics, filename, x, y)
        # Physics
        self.physics.add_sprite(self,
            friction=1.0, collision_type="cake",
            body_type=arcade.PymunkPhysicsEngine.KINEMATIC)

    def move(self, spd_x, spd_y):
        self.physics.set_velocity(self,(spd_x, spd_y))

    def change_dynamic(self):
        if self.check_body_type(arcade.PymunkPhysicsEngine.DYNAMIC): return False
        self.physics.remove_sprite(self)
        self.physics.add_sprite(self,
            friction=1.0, collision_type="cake",
            body_type=arcade.PymunkPhysicsEngine.DYNAMIC)
        return True
```

```python:utility.py(完成コード)
# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade

# Sound
class UtilSounds:

    def __init__(self):
        self.sounds = {}
        self.players = {}

    def load_sound(self, key, file_name):
        self.sounds[key] = arcade.Sound(file_name)

    def play(self, key, loop=False, volume=0.3):
        if not key in self.sounds: return
        self.players[key] = arcade.play_sound(self.sounds[key], 
            loop=loop, volume=volume)

    def stop(self, key):
        if not key in self.players: return
        self.sounds[key].stop(self.players[key])

    def stop_all(self):
        for key in self.players.keys():
            self.sounds[key].stop(self.players[key])
```

```python:main.py(完成コード)
# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import arcade.gui
import random
import sprite
import utility

PLAYER_JUMP_X = 10
PLAYER_JUMP_Y = 400

CAKE_SPEED_X_MIN = 64
CAKE_SPEED_X_MAX = 96
CAKE_PAD_Y       = 48
CAKE_INTERVAL    = 2.0
CAKE_FILES = [
    "images/cake_x2/cake_01.png",
    "images/cake_x2/cake_02.png",
    "images/cake_x2/cake_02.png",
    "images/cake_x2/cake_03.png",
    "images/cake_x2/cake_03.png",
    "images/cake_x2/cake_03.png"]

STAR_FILES = [
    "images/cake_x2/star_01.png",
    "images/cake_x2/star_02.png",
    "images/cake_x2/star_03.png",
    "images/cake_x2/star_04.png"]

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height
        self.background_color = arcade.color.POMP_AND_POWER

        # UtilSounds
        self.sounds = utility.UtilSounds()
        self.sounds.load_sound("ready", "sounds/bgm_ready.ogg")
        self.sounds.load_sound("game",  "sounds/bgm_game.ogg")
        self.sounds.load_sound("coin",  "sounds/se_coin.ogg")
        self.sounds.load_sound("jump",  "sounds/se_jump.ogg")
        self.sounds.load_sound("land",  "sounds/se_land.ogg")

        # Camera
        self.camera = arcade.Camera2D()
        self.camera_gui = arcade.Camera2D()

        # UI
        self.ui_manager = arcade.gui.UIManager()
        btn_retry = arcade.gui.UIFlatButton(
            text="RETRY", width=128, height=32)
        btn_retry.on_click = self.on_click_retry_button

        # Grid
        rows = 10
        cols = 10
        h_spacing = self.w / cols
        v_spacing = self.h / rows
        self.grid = arcade.gui.UIGridLayout(
            column_count=rows, row_count=cols, 
            horizontal_spacing=h_spacing, 
            vertical_spacing=v_spacing
        )
        self.grid.add(btn_retry, column=7, row=9)
        self.anchor = self.ui_manager.add(arcade.gui.UIAnchorLayout())
        self.anchor.add(
            anchor_x="center_x", anchor_y="center_y", child=self.grid,
        )

        self.setup()

    def setup(self):

        self.ready_flg = True
        self.cake_y = self.h / 2 + CAKE_PAD_Y / 2
        self.cake_interval = CAKE_INTERVAL

        self.sounds.stop_all()
        self.sounds.play("ready", volume=0.2)

        # PhysicsEngine
        self.physics = arcade.PymunkPhysicsEngine(
            damping=0.8, gravity=(0, -900))

        # SpriteList
        self.backgrounds = arcade.SpriteList()
        self.players = arcade.SpriteList()
        self.blocks = arcade.SpriteList()
        self.cakes = arcade.SpriteList()

        # Carpet
        carpet = sprite.Background(
            "images/cake_x2/carpet_01.png", self.w/2, 50)
        self.backgrounds.append(carpet)

        # Stars
        for i in range(16):
            x = self.camera.position.x - self.w/2 + random.randrange(int(self.w))
            y = self.camera.position.y + random.randrange(int(self.h*2))
            file = random.choice(STAR_FILES)
            star = sprite.Background(file, x, y)
            self.backgrounds.append(star)

        # Player
        self.player = sprite.Player(self.physics, 
            "images/cake_x2/land_01.png", self.w/2, self.h/2 + 34)
        self.players.append(self.player)

        # Table
        table = sprite.Block(self.physics,
                "images/cake_x2/table_01.png", self.w/2, self.h/2 - 64)
        self.blocks.append(table)

        # Info
        self.msg_info = arcade.Text(
            "PRESS KEY TO START!!", self.w/2, self.h-20, 
            arcade.color.WHITE, 16,
            anchor_x="center", anchor_y="top")

        # Camera
        self.camera.position = self.player.position

    def on_hide_view(self):
        self.ui_manager.disable()

    def on_show_view(self):
        self.ui_manager.enable()

    def on_key_press(self, key, key_modifiers):

        # Ready...
        if self.ready_flg == True:
            self.ready_flg = False
            self.sounds.stop("ready")
            self.sounds.play("game", loop=True, volume=0.2)
            return

        # Move(WASD)
        if key == arcade.key.A:
            self.physics.set_velocity(self.player, (-PLAYER_JUMP_X, PLAYER_JUMP_Y))
            self.player.change_animation("jump")
            self.sounds.play("jump")
        if key == arcade.key.S:
            self.physics.set_velocity(self.player, (PLAYER_JUMP_X, PLAYER_JUMP_Y))
            self.player.change_animation("jump")
            self.sounds.play("jump")
        
    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        if self.ready_flg == True: return

        # Cakes
        self.msg_info.text = "CAKES: {}".format(len(self.cakes))

        self.physics.step(delta_time) # PhysicsEngine

        # Animation
        self.players.update_animation(delta_time)

        # Player x Cakes
        hit_cakes = arcade.check_for_collision_with_list(
            self.player, self.cakes)
        for cake in hit_cakes:
            if cake.change_dynamic():
                self.cake_interval = CAKE_INTERVAL
                self.player.change_animation("land")
                self.sounds.play("land")

        # Spawn
        if 0.0 < self.cake_interval:
            self.cake_interval -= delta_time
            if self.cake_interval < 0.0:
                self.spawn_cake() # Spawn

        # Camera
        camera_x = self.camera.position[0]
        camera_y = arcade.math.lerp(
            self.camera.position[1],
            self.player.position[1], 0.1)
        self.camera.position = (camera_x, camera_y)

    def on_draw(self):
        self.clear() # Clear

        self.camera.use()
        arcade.draw_line(
            self.camera.position.x - self.w/2, self.cake_y, 
            self.camera.position.x + self.w/2, self.cake_y, 
            (255, 255, 255, 100), 1)

        self.backgrounds.draw()
        self.players.draw()
        self.blocks.draw()
        self.cakes.draw()

        # Debug
        #self.players.draw_hit_boxes()
        #self.blocks.draw_hit_boxes()
        #self.cakes.draw_hit_boxes()

        self.camera_gui.use()
        self.msg_info.draw()
        self.ui_manager.draw()

    def spawn_cake(self):
        path = random.choice(CAKE_FILES)
        x = 0
        y = self.cake_y + 1
        spd_x = random.randrange(CAKE_SPEED_X_MIN, CAKE_SPEED_X_MAX)
        if random.random() < 0.5:
            x = self.w
            spd_x *= -1
        cake = sprite.Cake(self.physics,
            path, x, y)
        cake.move(spd_x, 0)
        self.cakes.append(cake)
        self.cake_y += CAKE_PAD_Y

    def on_click_retry_button(self, event):
        print("RETRY")
        self.setup()
        

def main():
    """ メイン処理 """
    window = arcade.Window(320, 480, "Hello, Arcade!!")
    window.show_view(GameView(window)) # GameView
    arcade.run()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/books/28713ff37533c0/15_01.gif)

# 終わりに...

ここまで読んでいただき、ありがとうございました。
この連載が、ゲーム開発のきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว👍