---
title: "第11章(番外編): アニメーションを切り替えよう"
---

# アニメーションを切り替えよう

今回は、サンプルコードの紹介です。
プレイヤーの動作に応じてアニメーションを切り替えます。

## 忍者の画像を追加する

"images"フォルダの、"ninja"フォルダに以下の画像を追加します。

### 1, 後ろ姿

| 画像 | ファイル名 | 画像 | ファイル名 | 画像 | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/28713ff37533c0/ninja/back_01.png) | back_01.png | ![](/images/28713ff37533c0/ninja/back_02.png) | back_02.png | ![](/images/28713ff37533c0/ninja/back_03.png) | back_03.png |
| ![](/images/28713ff37533c0/ninja/back_04.png) | back_04.png | ![](/images/28713ff37533c0/ninja/back_05.png) | back_05.png |

### 2, 左に走る

| 画像 | ファイル名 | 画像 | ファイル名 | 画像 | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/28713ff37533c0/ninja/left_01.png) | left_01.png | ![](/images/28713ff37533c0/ninja/left_02.png) | left_02.png | ![](/images/28713ff37533c0/ninja/left_03.png) | left_03.png |
| ![](/images/28713ff37533c0/ninja/left_04.png) | left_04.png | ![](/images/28713ff37533c0/ninja/left_05.png) | left_05.png |

### 3, 右に走る

| 画像 | ファイル名 | 画像 | ファイル名 | 画像 | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/28713ff37533c0/ninja/right_01.png) | right_01.png | ![](/images/28713ff37533c0/ninja/right_02.png) | right_02.png | ![](/images/28713ff37533c0/ninja/right_03.png) | right_03.png |
| ![](/images/28713ff37533c0/ninja/right_04.png) | right_04.png | ![](/images/28713ff37533c0/ninja/right_05.png) | right_05.png |

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py
　└ images/
　 　├ bg_temple.png
　 　├ coins/
　　 └ ninja/ <- 忍者画像を格納するフォルダ
　　　　├ front_01.png
　　　　├ front_02.png
　　　　├ front_03.png
　　　　├ front_04.png
　　　　├ front_05.png
　　　　├ back_01.png
　　　　├ back_02.png
　　　　├ back_03.png
　　　　├ back_04.png
　　　　├ back_05.png
　　　　├ left_01.png
　　　　├ left_02.png
　　　　├ left_03.png
　　　　├ left_04.png
　　　　├ left_05.png
　　　　├ right_01.png
　　　　├ right_02.png
　　　　├ right_03.png
　　　　├ right_04.png
　　　　└ right_05.png
```

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

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
        # Animation
        self.anim_counter = 0
        self.anim_interval = 4
        self.anim_index = 0
        self.anim_key = "" # 選択中のアニメ
        self.anim_pause = True # 停止中かどうか
        self.anims = {} # アニメーションリスト(ディクショナリ)

    def update(self, delta_time):
        """ Update """
        self.center_x += self.vx * delta_time
        self.center_y += self.vy * delta_time
        # Animation
        self.update_animation() # アニメーション更新

    def move(self, spd, deg, tag=""):
        """ Move Sprite """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)
        if tag: self.change_animation(tag) # アニメーション変更

    def stop(self):
        """ Stop Sprite """
        self.vx = 0
        self.vy = 0
        self.stop_animation() # アニメーション停止

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
        self.anims[key] = anim # アニメーションリストに追加

    def change_animation(self, key):
        """ Change Animation """
        if not key in self.anims: return
        self.anim_counter = 0
        self.anim_index = 0
        self.anim_key = key
        self.texture = self.anims[key][0]
        self.start_animation() # アニメーション開始

    def start_animation(self):
        """ Start Animation """
        self.anim_pause = False # アニメーション開始

    def stop_animation(self):
        """ Stop Animation """
        self.anim_pause = True # アニメーション停止

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        # アニメーションを登録
        self.load_animation("front", "images/ninja/front_{:02d}.png", 5)
        self.load_animation("left", "images/ninja/left_{:02d}.png", 5)
        self.load_animation("right", "images/ninja/right_{:02d}.png", 5)
        self.load_animation("back", "images/ninja/back_{:02d}.png", 5)
        self.change_animation("front")

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        # アニメーションを登録
        self.load_animation("coin", "images/coin/coin_{:02d}.png", 5)
        self.change_animation("coin")
```

```python:main.py(完成コード)
import arcade
import sprite
import random

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

        # 小判スプライト
        self.coins = arcade.SpriteList()
        for i in range(10):
            x = random.random() * self.w
            y = random.random() * self.h
            coin = sprite.Coin("images/coin/coin_01.png",
                               x=x, y=y)
            self.coins.append(coin)

        # スコア
        self.score = 0
        self.score_text = arcade.Text(
            "SCORE: {}".format(self.score), 
            self.w/2, self.h-20,
            arcade.color.BLACK, 16,
            anchor_x="center", anchor_y="top")

        # サウンドオブジェクト
        self.se_coin = arcade.Sound("sounds/se_coin.ogg")

    def on_key_press(self, key, key_modifiers):
        # Move(WASD)
        if key == arcade.key.W: self.player.move(90, 90, "back") # 上へ
        if key == arcade.key.A: self.player.move(90, 180, "left") # 左へ
        if key == arcade.key.S: self.player.move(90, 270, "front") # 下へ
        if key == arcade.key.D: self.player.move(90, 0, "right") # 右へ

    def on_key_release(self, key, key_modifiers):
        self.player.stop()

    def on_update(self, delta_time):
        self.players.update(delta_time)
        self.coins.update(delta_time)

        # プレイヤー x コインリスト
        hit_coins = arcade.check_for_collision_with_list(self.player,
                                                         self.coins)
        for coin in hit_coins:
            coin.remove_from_sprite_lists()
            # スコア
            self.score += 1
            self.score_text.text = "SCORE: {}".format(self.score)
            # サウンドを再生
            arcade.play_sound(self.se_coin)

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw()
        self.coins.draw()
        self.score_text.draw()

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

![](/images/28713ff37533c0/11_01.gif)

# 終わりに...

# 終わりに...

ここまで読んでいただき、ありがとうございました。
この連載が、そのきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว
(よろしければ👍頂けると大変励みになります!!)