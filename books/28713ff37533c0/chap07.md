---
title: "第7章: 小判をゲットしよう"
---

# 小判をゲットしよう

今回は、小判を大量に配置し、衝突判定で削除します。

## 1, 小判画像を用意する

"images"フォルダに、新たに"coin"フォルダを作り、以下の画像を格納します。
(忍者といえば小判!!)

| 画像 | ファイル名 |
| ---- | ---- |
| ![](/images/28713ff37533c0/coin/coin_01.png) | coin_01.png |

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py
　└ images/
　 　├ bg_temple.png
　　 ├ ninja/
　　 └ coin/ <- 小判画像を格納するフォルダ
　　　　└ coin_01.png
```

## 2, 小判スプライトを定義する

"sprite.py"に、新たに"Coin"クラスを定義します。
このクラスは、"Player"クラスと同様に、"BaseSprite"クラスを継承しておきます。

```python:sprite.py(抜粋)
class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
```

## 3, ランダムモジュールをインポートする

"main.py"に、"random"モジュールをインポートしておきます。
後ほどこのモジュールを使って小判をランダム配置します。

```python:main.py(抜粋)
import random
```

## 4, 小判スプライトを作る

"GameView"のコンストラクタで、先ほど用意した"Coin"クラスからスプライトを作ります。
これまでと同様に、複数のスプライトをまとめて管理、描画するために、"arcade.SpriteList"を使います。

```python:python:main.py(抜粋)
# 小判スプライト
self.coins = arcade.SpriteList()
for i in range(10):
    x = random.random() * self.w # x座標ランダム
    y = random.random() * self.h # y座標ランダム
    coin = sprite.Coin("images/coin/coin_01.png",
                       x=x, y=y)
    self.coins.append(coin)
```

ここでは、小判を10個(10回ループ)用意しています。
配置する座標として、"random.random()"メソッドを利用します。

"random.random()"は、"0.0以上〜1.0未満"の小数を返すため、
画面サイズと掛け算することで、画面内のランダムな位置を作ることができます。

## 5, 小判スプライトを更新する

"GameView"の"on_update()"メソッドで、小判リストを一括で更新します。
現状で小判は動きませんが、このタイミングで座標を更新しつつスプライトを移動させる事も可能です。

```python:main.py(抜粋)
self.coins.update(delta_time) # 小判リストを更新
```

## 6, 小判スプライトを描画する

"GameView"の"on_draw()"メソッドで、小判リストを一括で描画します。
(要領がわかってきましたね!?)

```python:main.py(抜粋)
self.coins.draw() # 小判リストを描画
```

## 7, プレイヤーと小判リストの衝突判定

最後に、"GameView"の"on_update()"メソッドで、
プレイヤーと小判リストとの衝突判定を実装します。

```python:main.py(抜粋)
# プレイヤー x コインリストの衝突判定
hit_coins = arcade.check_for_collision_with_list(self.player,
                                                 self.coins)
# 衝突したコインをコインリストから削除
for coin in hit_coins:
    hit_coins.remove_from_sprite_lists()
```

"check_for_collision_with_list()"メソッドは、
第一引数のスプライトと、"SpriteList"とを衝突判定した結果を返すメソッドです。

衝突判定後、そのリスト"hit_coins"に対し、
"remove_from_sprite_lists()"メソッドで小判スプライトを削除します。

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

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
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
            x = random.random() * self.w # x座標ランダム
            y = random.random() * self.h # y座標ランダム
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
        self.player.stop() # 停止

    def on_update(self, delta_time):
        self.players.update(delta_time)
        self.coins.update(delta_time) # 小判リストを更新

        # プレイヤー x コインリストの衝突判定
        hit_coins = arcade.check_for_collision_with_list(self.player,
                                                         self.coins)
        # 衝突したコインをコインリストから削除
        for coin in hit_coins:
            coin.remove_from_sprite_lists()

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw()
        self.coins.draw() # 小判リストを描画

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

![](/images/28713ff37533c0/07_01.gif)

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「アニメーションさせよう」です。
お楽しみに!!
(よろしければ👍頂けると大変励みになります!!)