---
title: "第10章: サウンドを再生しよう"
---

# サウンドを再生しよう

今回は、サウンドを再生します。

## 1, 音源ファイルを用意する

新たに、"sounds"フォルダを作り、以下の音源ファイルを格納します。

| 音源ファイル | ファイル名 |
| ---- | ---- |
| [se_coin.oggをダウンロード](https://github.com/sdkfz181tiger/Zenn/blob/main/images/28713ff37533c0/se_coin.ogg) | se_coin.ogg |

音源ファイルは、[SEADENDEN 8bit Free BGM](https://seadenden-8bit.com/)からお借りしました。
(筆者激推し!!)

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py
　├ images/
　└ sounds/ <- 音源ファイルを格納するフォルダ
　 　└ se_coin.ogg
```

## 2, サウンドオブジェクトを作る

サウンドオブジェクトは、次のようにして作ります。

```python:python:main.py(抜粋)
# サウンドオブジェクト
self.se_coin = arcade.Sound("sounds/se_coin.ogg")
```

## 3, サウンドを再生する

サウンドの再生は、次のようにして再生します。

```python:python:main.py(抜粋)
# サウンドを再生
arcade.play_sound(self.se_coin)
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
        self.anim = []

    def update(self, delta_time):
        """ Update """
        self.center_x += self.vx * delta_time
        self.center_y += self.vy * delta_time
        # Animation
        self.update_animation()

    def move(self, spd, deg):
        """ Move Sprite """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

    def stop(self):
        """ Stop Sprite """
        self.vx = 0
        self.vy = 0

    def update_animation(self):
        """ Animation """
        if not self.anim: return
        self.anim_counter += 1
        if(self.anim_counter < self.anim_interval): return
        self.anim_counter = 0
        self.anim_index += 1
        if len(self.anim) <= self.anim_index: self.anim_index = 0
        self.texture = self.anim[self.anim_index]

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        self.anim.append(arcade.load_texture("images/ninja/front_01.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_02.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_03.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_04.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_05.png"))

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        self.anim.append(arcade.load_texture("images/coin/coin_01.png"))
        self.anim.append(arcade.load_texture("images/coin/coin_02.png"))
        self.anim.append(arcade.load_texture("images/coin/coin_03.png"))
        self.anim.append(arcade.load_texture("images/coin/coin_04.png"))
        self.anim.append(arcade.load_texture("images/coin/coin_05.png"))
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
        if key == arcade.key.W: self.player.move(90, 90)
        if key == arcade.key.A: self.player.move(90, 180)
        if key == arcade.key.S: self.player.move(90, 270)
        if key == arcade.key.D: self.player.move(90, 0)

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

実行結果は次のようになります。(音が...鳴ってる筈...!?)

![](/images/28713ff37533c0/10_01.gif)

# 終わりに...

ここまで読んでいただき、ありがとうございました。
今回で、"Pythonで2Dゲームをかじる本_Arcade編"は終了です。
お疲れ様でした!!

今回作ったゲームはとてもシンプルですが、

- スプライト管理
- キーボード入力
- サウンド再生

といった、ゲーム制作の基本要素がすべて含まれています。

ここまで理解できていれば、
Arcadeを使った簡単なゲームは、もう自力で作れるはずです。

ここまでの技術をベースにして、シンプルなゲームを作ってみる事をオススメ致します。
この連載が、そのきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว
(よろしければ👍頂けると大変励みになります!!)