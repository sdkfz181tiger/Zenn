---
title: "第18章(番外編): スーパーランドゲーム(サンプル)"
---

# スーパーランドゲーム(サンプル)

今回は、どこかで見た様なアクションゲームに挑戦します。
(ここでは、サンプルコードのみの紹介です)

## 1, 素材を用意する

"Pyxel Editor"で、背景の素材を描きます。

![](/images/books/675e49a3e4d34b/18_01.png)

[完成したリソースファイルをダウンロード](https://github.com/sdkfz181tiger/Zenn/blob/main/images/books/675e49a3e4d34b/res_superland/my_resource.pyxres) (右上の"ダウンロード"ボタンを押してダウンロードしてください)

![](/images/books/675e49a3e4d34b/03_05.png)

# サンプルコード

今回のサンプルコードは、次の通りです。

:::details 完成コード(sprite.py)
```python: sprite.py
import pyxel
import math
import random

TILE_NONE     = 0
TILE_OBSTACLE = 1
TILE_ITEM     = 2

TILE_TYPES = {
    (0, 7): TILE_OBSTACLE, # Grounds
    (1, 7): TILE_OBSTACLE,
    (2, 7): TILE_OBSTACLE,
    (3, 7): TILE_OBSTACLE,
    (4, 7): TILE_OBSTACLE,
    (0, 8): TILE_OBSTACLE,
    (1, 8): TILE_OBSTACLE,
    (2, 8): TILE_OBSTACLE,
    (3, 8): TILE_OBSTACLE,
    (4, 8): TILE_OBSTACLE,
    (4, 2): TILE_OBSTACLE, # Blocks
    (5, 2): TILE_OBSTACLE,
    (2, 2): TILE_OBSTACLE, # Tunnels
    (3, 2): TILE_OBSTACLE,
    (2, 3): TILE_OBSTACLE,
    (3, 3): TILE_OBSTACLE,
    (2, 4): TILE_OBSTACLE,
    (3, 4): TILE_OBSTACLE,
    (0, 2): TILE_ITEM,     # Coin
    (1, 2): TILE_ITEM      # Onigiri
}

class BaseSprite:

    def __init__(self, x, y, u, v, w=8, h=8):
        """ Constructor """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0
        self.hw = w / 2
        self.hh = h / 2

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pass

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def move(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

    def stop(self):
        self.vx = 0
        self.vy = 0

    def intersects(self, other):
        if other.x + other.w < self.x: return False
        if self.x + self.w < other.x: return False
        if other.y + other.h < self.y: return False
        if self.y + self.h < other.y: return False
        return True

    def get_left(self):
        return (self.x, self.y + self.hh)

    def get_right(self):
        return (self.x + self.w, self.y + self.hh)

    def get_top(self):
        return (self.x + self.hw, self.y)

    def get_bottom(self):
        return (self.x + self.hw, self.y + self.h)

    def is_tile_type(self, x, y, type):
        tilemap = pyxel.tilemaps[0]
        u, v = x // 8, y // 8
        tile = tilemap.pget(u, v)
        if not(tile in TILE_TYPES):
            return TILE_NONE, u, v
        return TILE_TYPES[tile] == type, u, v

    def collide_obstacles(self):
        t_obs = TILE_OBSTACLE
        x, y = self.get_bottom()# x Bottom
        flg, u, v = self.is_tile_type(x, y, t_obs)
        if flg:
            self.y = (v-1) * 8
            self.vy = 0
            self.land() # Land
        x, y = self.get_top() # x Top
        flg, u, v = self.is_tile_type(x, y, t_obs)
        if flg:
            self.y = (v+1) * 8
            self.vy = 0
            return
        # x Left
        if self.vx < 0:
            x, y = self.get_left() # Left
            flg, u, v = self.is_tile_type(x, y, t_obs)
            if flg:
                self.x = (u+1) * 8
                self.vx = 0
                return
        # x Right
        if 0 < self.vx:
            x, y = self.get_right() # Right
            flg, u, v = self.is_tile_type(x, y, t_obs)
            if flg:
                self.x = (u-1) * 8
                self.vx = 0
                return

    def collide_items(self):
        tilemap = pyxel.tilemaps[0]
        t_item = TILE_ITEM
        x, y = self.get_bottom()# x Bottom
        flg, u, v = self.is_tile_type(x, y, t_item)
        if flg:
            tilemap.pset(u, v, (0, 0))
            return
        x, y = self.get_top() # x Top
        flg, u, v = self.is_tile_type(x, y, t_item)
        if flg:
            tilemap.pset(u, v, (0, 0))
            return
        x, y = self.get_left() # Left
        flg, u, v = self.is_tile_type(x, y, t_item)
        if flg:
            tilemap.pset(u, v, (0, 0))
            return
        x, y = self.get_right() # Right
        flg, u, v = self.is_tile_type(x, y, t_item)
        if flg:
            tilemap.pset(u, v, (0, 0))
            return
                
class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ Constructor """
        super().__init__(x, y, u, v)
        self.gravity = 0.4 # Gravity
        self.jump_x  = 0.8
        self.jump_y  = -2.4
        self.off_u   = 0
        self.off_v   = 0

    def update(self):
        super().update()
        self.vy += self.gravity # Gravity

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 
            self.u + self.off_u, 
            self.v + self.off_v, 
            self.w, self.h, 0)

    def jump(self):
        self.off_v = 8
        self.vy = self.jump_y

    def runL(self):
        self.off_u = 8
        self.vx = -self.jump_x

    def runR(self):
        self.off_u = 0
        self.vx = self.jump_x

    def stopLR(self):
        self.off_v = 0
        self.vx = 0

    def land(self):
        self.off_v = 0
```
:::

:::details 完成コード(main.py)
```python: main.py
import pyxel
import math
import random
import sprite

W, H = 160, 120

START_X = W / 4
START_Y = H / 2 - 16

MODE_TITLE     = "title"
MODE_PLAY      = "play"
MODE_GAME_OVER = "game_over"

CAMERA_PAD_X   = 60
CAMERA_LIMIT_L = W - 640
CAMERA_LIMIT_R = 0

# Game
class Game:
    def __init__(self):
        """ Constructor """

        # Pyxel
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        # Tilemap(Copy 0 -> 1)
        pyxel.tilemaps[1].blt(0, 0, 0, 0, 0, 640, 128)

        # Score
        self.score = 0

        # Game Mode
        self.game_mode = MODE_TITLE

        # Player
        self.player = sprite.PlayerSprite(START_X, START_Y, 16, 0)

        # Reset
        self.reset()

        # Run
        pyxel.run(self.update, self.draw)

    def update(self):

        # Score
        self.score = int(self.player.x - START_X)

        # Controll
        self.controll()

        # Game Mode
        if self.game_mode != MODE_PLAY: return

        # Player
        self.player.update()

        # x Obstacles, Items
        self.player.collide_obstacles()
        self.player.collide_items()

        # Game Over
        if H < self.player.y: 
            self.game_mode = MODE_GAME_OVER

    def draw(self):
        pyxel.cls(1)

        # Camera(on)
        self.camera_on()

        # Tilemap
        pyxel.bltm(0, 0, 0, 0, 0, 640, 128, 0)

        # Player
        self.player.draw()

        # Camera(off)
        self.camera_off()

        # Message
        if self.game_mode == MODE_TITLE:
            msg = "WASD TO PLAY"
            pyxel.text(W/2-len(msg)*2, 16, msg, 7)
        elif self.game_mode == MODE_GAME_OVER:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, 16, msg, 7)

        # Score
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 1)

    def reset(self):

        # Tilemap(1 -> 0)
        pyxel.tilemaps[0].blt(0, 0, 1, 0, 0, 640, 128) # Copy

        # Camera
        self.camera_x = 0

        # Reset
        self.player.reset(START_X, START_Y)

    def controll(self):

        # Game Mode
        if self.game_mode != MODE_PLAY:
            if not(pyxel.btnp(pyxel.KEY_W) or 
                pyxel.btnp(pyxel.KEY_A) or 
                pyxel.btnp(pyxel.KEY_S) or 
                pyxel.btnp(pyxel.KEY_D)):
                return

            # Title -> Play
            if self.game_mode == MODE_TITLE:
                self.game_mode = MODE_PLAY

            # Game Over -> Title
            if self.game_mode == MODE_GAME_OVER:
                self.game_mode = MODE_TITLE
                self.reset() # Reset
        else:
            # Player
            if pyxel.btnp(pyxel.KEY_W):
                self.player.jump()
            if pyxel.btnp(pyxel.KEY_A):
                self.player.runL()
            if pyxel.btnp(pyxel.KEY_D):
                self.player.runR()
            if pyxel.btnr(pyxel.KEY_A):
                self.player.stopLR()
            if pyxel.btnr(pyxel.KEY_D):
                self.player.stopLR()

    def camera_on(self):
        line_r = W - self.camera_x - CAMERA_PAD_X
        if line_r < self.player.x:
            self.camera_x += line_r - self.player.x
            if self.camera_x < CAMERA_LIMIT_L:
                self.camera_x = CAMERA_LIMIT_L
        line_l = 0 - self.camera_x + CAMERA_PAD_X
        if self.player.x < line_l:
            self.camera_x += line_l - self.player.x
            if CAMERA_LIMIT_R < self.camera_x:
                self.camera_x = CAMERA_LIMIT_R
        pyxel.camera(-self.camera_x, 0)

    def camera_off(self):
        pyxel.camera()

def main():
    """ Main """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/books/675e49a3e4d34b/18_02.gif)

# 終わりに...

ここまで読んでいただきありがとうございました。
この連載が、ゲーム開発のきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว
(よろしければ👍頂けると大変励みになります!!)