---
title: "第6章: キャラクターを動かしてみよう"
---

# キャラクターを動かしてみよう

前回作ったスプライトを、いよいよ動かします。
この章では、スプライトに"速度"を持たせることで、
移動の仕組みを作っていきます。

## 1, スプライトクラスを改良する

共通クラスである、"BaseSprite"のコンストラクタに、
新たに"vx, vy"の2つのメンバ変数を追加します。

これらの変数は、"update()"のタイミングで座標"x, y"にそれぞれ加算します。
こうすることで、キャラクターの座標が少しづつ変化します。
その結果、ゲーム画面上でキャラクターが移動して見えるようになる訳です。

追加した、"move()"メソッドは、その名の通り移動を開始するメソッドです。
引数に速度と角度を与えることで、
"math.cos()"で水平方向(x方向)に変換し"vx"へ、
"math.sin()"で垂直方向(y方向)に変換し"vy"にそれぞれ代入します。
(このあたりは深く考えなくても大丈夫です!!)

```python: sprite.py(抜粋)
class BaseSprite:

    def __init__(self, x, y, w=8, h=8):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = 0 # 移動速度(x方向)
        self.vy = 0 # 移動速度(y方向)

    def update(self):
        """ 更新処理 """
        self.x += self.vx # x方向に移動
        self.y += self.vy # y方向に移動

    def draw(self):
        """ 描画処理(派生クラスで実装) """
        pass

    def move(self, spd, deg):
        """ 移動 """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度
```

## 2, スプライトの動きをテストする

"Game"クラスのコンストラクタで、動きをテストしてみましょう。

```python: main.py(抜粋)
SHIP_SPD = 1.4 # プレイヤーの速度

# 中略

# 移動をテスト(左上へ)
self.ship.move(SHIP_SPD, 220)
```

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python: sprite.py
import pyxel
import math
import random

class BaseSprite:

    def __init__(self, x, y, w=8, h=8):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = 0 # 移動速度(x方向)
        self.vy = 0 # 移動速度(y方向)

    def update(self):
        """ 更新処理 """
        self.x += self.vx # x方向に移動
        self.y += self.vy # y方向に移動

    def draw(self):
        """ 描画処理(派生クラスで実装) """
        pass

    def move(self, spd, deg):
        """ 移動 """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度

class ShipSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)

    def draw(self):
        """ 描画処理 """
        pyxel.blt(self.x, self.y, 0, 
            0, 0, 
            self.w, self.h, 0) # Ship
```

```python: main.py
import pyxel
import math
import random
import sprite

W, H = 160, 120
SHIP_SPD = 1.4 # プレイヤーの速度

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # プレイヤーを初期化
        self.ship = sprite.ShipSprite(W/2, H - 40)

        # 移動をテスト(左上へ)
        self.ship.move(SHIP_SPD, 220)

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("shooter.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # プレイヤーを更新
        self.ship.update()

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

        # プレイヤーを描画
        self.ship.draw()

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/675e49a3e4d34b/06_01.gif)

# 次回は...

ここまで読んでいただきありがとうございました。
次回のタイトルは「xxxを用意しよう」です。
お楽しみに!!