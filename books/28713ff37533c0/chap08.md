---
title: "第8章: アニメーションさせよう"
---

# アニメーションさせよう

複数の画像を使って、アニメーションを実装します。

## 1, 忍者の画像を追加する

"images"フォルダの、"ninja"フォルダに以下の画像を追加します。

| 画像 | ファイル名 | 画像 | ファイル名 | 画像 | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/28713ff37533c0/ninja/front_01.png) | front_01.png | ![](/images/28713ff37533c0/ninja/front_02.png) | front_02.png | ![](/images/28713ff37533c0/ninja/front_03.png) | front_03.png |
| ![](/images/28713ff37533c0/ninja/front_04.png) | front_04.png | ![](/images/28713ff37533c0/ninja/front_05.png) | front_05.png |

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py
　└ images/
　 　├ bg_temple.png
　　 └ ninja/ <- 忍者画像を格納するフォルダ
　　　　├ front_01.png
　　　　├ front_02.png
　　　　├ front_03.png
　　　　├ front_04.png
　　　　└ front_05.png
```

## 2, 小判の画像を追加する

先ほどと同様に、"images"フォルダの、"coin"フォルダに以下の画像を追加します。

| 画像 | ファイル名 | 画像 | ファイル名 | 画像 | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/28713ff37533c0/coin/coin_01.png) | coin_01.png | ![](/images/28713ff37533c0/coin/coin_02.png) | coin_02.png | ![](/images/28713ff37533c0/coin/coin_03.png) | coin_03.png |
| ![](/images/28713ff37533c0/coin/coin_04.png) | coin_04.png | ![](/images/28713ff37533c0/coin/coin_05.png) | coin_05.png |

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py
　└ images/
　 　├ bg_temple.png
　　 ├ ninja/
　　 └ coin/ <- 小判画像を格納するフォルダ
　　　　├ coin_01.png
　　　　├ coin_02.png
　　　　├ coin_03.png
　　　　├ coin_04.png
　　　　└ coin_05.png
```

## 3, 忍者の画像を読み込む

次に、"sprite.py"の、"Player"クラスのコンストラクタ部分で、
忍者の画像を5枚分、"anim"リストへ追加します。

```python:sprite.py(Playerに追加)
def __init__(self, filename, x, y):
    super().__init__(filename, x, y)

    # 忍者の画像を5枚読み込む
    self.anim.append(arcade.load_texture("images/ninja/front_01.png"))
    self.anim.append(arcade.load_texture("images/ninja/front_02.png"))
    self.anim.append(arcade.load_texture("images/ninja/front_03.png"))
    self.anim.append(arcade.load_texture("images/ninja/front_04.png"))
    self.anim.append(arcade.load_texture("images/ninja/front_05.png"))
```

## 4, 小判の画像を読み込む

同様に、"sprite.py"の、"Coin"クラスのコンストラクタ部分で、
小判の画像を5枚分、"anim"リストへ追加します。

```python:sprite.py(Coinに追加)
def __init__(self, filename, x, y):
    super().__init__(filename, x, y)

    # 小判の画像を5枚読み込む
    self.anim.append(arcade.load_texture("images/coin/coin_01.png"))
    self.anim.append(arcade.load_texture("images/coin/coin_02.png"))
    self.anim.append(arcade.load_texture("images/coin/coin_03.png"))
    self.anim.append(arcade.load_texture("images/coin/coin_04.png"))
    self.anim.append(arcade.load_texture("images/coin/coin_05.png"))
```

## 5, 基底クラスに変数を追加する

"sprite.py"の基底クラスである"BaseSprite"に、新たに4つの変数を追加します。
これらの変数は、この後に実装する"update_animation()"メソッドで利用します。

```python:sprite.py(BaseSpriteに追加)
def __init__(self, filename, x, y):
    super().__init__(filename)
    # Position
    self.center_x = x
    self.center_y = y
    # Velocity
    self.vx = 0
    self.vy = 0
    # Animation
    self.anim_counter = 0 # カウンタ
    self.anim_interval = 4 # 4フレームおきにカウント
    self.anim_index = 0 # フレーム番号
    self.anim = [] # 画像を格納するリスト
```

## 6, アニメーション専用のメソッドを追加する

同じ"BaseSprite"に、新たに"update_animation()"メソッドを追加します。

```python:sprite.py(BaseSpriteに追加)
def update_animation(self):
    """ Animation """
    if not self.anim: return
    self.anim_counter += 1 # カウンタに+1
    if(self.anim_counter < self.anim_interval): return # 4フレームおきにカウント
    self.anim_counter = 0 # カウンタをリセット
    self.anim_index += 1 # 画像番号を次へ
    if len(self.anim) <= self.anim_index: self.anim_index = 0 # 最後であれば0に
    self.texture = self.anim[self.anim_index] # 画像をセット
```

この部分では、"anim"に格納された画像を、4フレームおきに順番に切り替える処理を行なっています。
この値を小さくすれば、画像の切り替えが早くなり、大きくすると切り替えが遅くなります。
(是非試してみてくださいね)

## 7, 更新メソッドで実行する

最後に、"update_animation()"メソッドを、"update()"メソッドから実行します。

```python:sprite.py(BaseSpriteに追加)
def update(self, delta_time):
    """ Update """
    self.center_x += self.vx * delta_time
    self.center_y += self.vy * delta_time
    # Animation
    self.update_animation()
```

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
        # Animation
        self.anim_counter = 0 # カウンタ
        self.anim_interval = 4 # 4フレームおきにカウント
        self.anim_index = 0 # フレーム番号
        self.anim = [] # 画像を格納するリスト

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
        self.anim_counter += 1 # カウンタに+1
        if(self.anim_counter < self.anim_interval): return # 4フレームおきにカウント
        self.anim_counter = 0 # カウンタをリセット
        self.anim_index += 1 # 画像番号を次へ
        if len(self.anim) <= self.anim_index: self.anim_index = 0 # 最後であれば0に
        self.texture = self.anim[self.anim_index] # 画像をセット

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        # 忍者の画像を5枚読み込む
        self.anim.append(arcade.load_texture("images/ninja/front_01.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_02.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_03.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_04.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_05.png"))

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        # 小判の画像を5枚読み込む
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

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw()
        self.coins.draw()

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

![](/images/28713ff37533c0/08_01.gif)

# 次回は...

ここまで読んでいただき、ありがとうございました。
次回のタイトルは「スコアを表示しよう」です。
お楽しみに!!
(よろしければ👍頂けると大変励みになります!!)