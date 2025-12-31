---
title: "第7章: キャラクターをコントロールしよう"
---

# キャラクターをコントロールしよう

今回は、スペースキーの押されたタイミングを判定し、
プレイヤーの移動方向を左右反転する処理を実装します。

## 1, 左右反転するメソッドを追加

"Game"クラスのコンストラクタで、
右方向(0度)か、左方向(180)のどちらかに移動をさせます。

```python: main.py(Gameクラスのコンストラクタ内)
# 左右いずれかをランダムで選ぶ
deg = 0 if random.random()<0.5 else 180
self.ship.move(SHIP_SPD, deg)
```

次に、移動方向(左右切り替え)を行う"flip_x()"メソッドを追加します。
この処理では、"vx"に対して"-1"を掛け算します。

x方向の移動速度である、"vx"の符号を反転することで、
左右の移動方向が切り替わる訳です。

```python: sprite.py(BaseSpriteクラスに追加)
def flip_x(self):
    """ x方向反転 """
    self.vx *= -1
```

## 2, キーボードを押した時の処理

"Game"クラスに、新たに"control_ship()"メソッドを追加します。
ここでは、"pyxel.btnp()"を利用し、
キーボードが押された時の判定を行います。
引数に、"pyxel.KEY_SPACE"を記述し、"スペースキー"を判定しています。

```python: main.py(Gameクラスに追加)
def control_ship(self):
    """ アクション """
    if pyxel.btnp(pyxel.KEY_SPACE):
        self.ship.flip_x() # 移動反転
```

## 3, ゲーム画面のオーバーラップ処理

キャラクターの座標と、ゲーム画面の境界を比較し、画面外判定を行う、
"overlap_spr()"メソッドを追加します。

画面外を判定した時、反対側に移動(左<->右、上<->下)させます。
引数に、"spr"とすることで、
"プレイヤー"や"隕石"に対して、オーバーラップ処理を適用できるようにしています。

```python: main.py(Gameクラスに追加)
def overlap_spr(self, spr):
    """ 画面外に出たら反対側へ """
    if spr.x < -spr.w: 
        spr.x = W
        return
    if W < spr.x:
        spr.x = -spr.w
        return
    if spr.y < -spr.h:
        spr.y = H
        return
    if H < spr.y:
        spr.y = -spr.h
        return
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
        self.vx = 0
        self.vy = 0

    def update(self):
        """ 更新処理 """
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        """ 描画処理(派生クラスで実装) """
        pass

    def move(self, spd, deg):
        """ 移動 """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度

    def flip_x(self):
        """ x方向反転 """
        self.vx *= -1

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

        # 左右いずれかをランダムで選ぶ
        deg = 0 if random.random()<0.5 else 180
        self.ship.move(SHIP_SPD, deg)

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("shooter.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # プレイヤーを更新
        self.ship.update()
        # プレイヤーをコントロール
        self.control_ship()
        # プレイヤーの画面外判定
        self.overlap_spr(self.ship)

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

        # プレイヤーを描画
        self.ship.draw()

    def control_ship(self):
        """ アクション """
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.ship.flip_x() # 移動反転

    def overlap_spr(self, spr):
        """ 画面外に出たら反対側へ """
        if spr.x < -spr.w: 
            spr.x = W
            return
        if W < spr.x:
            spr.x = -spr.w
            return
        if spr.y < -spr.h:
            spr.y = H
            return
        if H < spr.y:
            spr.y = -spr.h
            return

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/675e49a3e4d34b/07_01.gif)

# 次回は...

ここまで読んでいただきありがとうございました。
次回のタイトルは「隕石を発生させよう」です。
お楽しみに!!