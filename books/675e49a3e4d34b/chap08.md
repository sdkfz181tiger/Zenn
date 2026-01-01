---
title: "第8章: 隕石を発生させよう"
---

# 隕石を発生させよう

今回は、一定間隔で隕石を発生させる処理を実装します。
※完成コードは最後に記述してあります。

## 1, 隕石スプライトを用意する

"sprite.py"に、新たに"AsteroidSprite"クラスを追加します。
コンストラクタでは、ランダム値を利用し隕石画像を選択します。

```python: sprite.py(クラスを追加)
class AsteroidSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)
        self.index = random.randint(2, 7) # 隕石画像

    def draw(self):
        """ 描画処理 """
        pyxel.blt(self.x, self.y, 0, self.w*self.index, 0, 
                self.w, self.h, 0) # Ship
```

## 2, 定数と変数を用意する

"main.py"に、次の定数を追加します。

定数にしてまとめておくことで、
ゲームの難易度を一括で管理することができるようになります。

```python: main.py(定数を追加)
ASTEROID_INTERVAL = 20 # 隕石の発生間隔
ASTEROID_LIMIT = 30 # 隕石の最大数

ASTEROID_SPD_MIN = 1.0 # 隕石の最低速度
ASTEROID_SPD_MAX = 2.0 # 隕石の最高速度
ASTEROID_DEG_MIN = 30 # 隕石の最低角度
ASTEROID_DEG_MAX = 150 # 隕石の最高角度
```

"Game"クラスのコンストラクタに、次の変数とリストを追加します。
この後、これらを利用し、一定間隔で隕石が発生する仕組みを実装します。

```python: sprite.py(Gameクラスのコンストラクタに追加)
# 隕石
self.asteroid_time = 0
self.asteroids = []
```

## 3, 隕石の発生処理

"Game"クラスに、"check_interval()"メソッドを追加します。

隕石は、先ほど用意した"ASTEROID_INTERVAL"の間隔で発生します。
同時に、"ASTEROID_LIMIT"で、発生する最大数に制限をかけています。

発生する隕石の座標として、ゲーム画面上端からランダムで選択します。
速度は、"ASTEROID_SPD_MIN ~ ASTEROID_SPD_MAX"で、
角度は、"ASTEROID_DEG_MIN ~ ASTEROID_DEG_MAX"からランダムで決定します。

```python: main.py(Gameクラスに追加)
def check_interval(self):
    # 隕石の出現間隔
    self.asteroid_time += 1
    if self.asteroid_time < ASTEROID_INTERVAL: return
    self.asteroid_time = 0
    # 隕石の最大数を超えない範囲で
    if ASTEROID_LIMIT < len(self.asteroids): return
    # 隕石の追加
    x = random.random() * W
    y = 0
    spd = random.uniform(ASTEROID_SPD_MIN, ASTEROID_SPD_MAX)
    deg = random.uniform(ASTEROID_DEG_MIN, ASTEROID_DEG_MAX)
    asteroid = sprite.AsteroidSprite(x, y)
    asteroid.move(spd, deg)
    self.asteroids.append(asteroid)
```

## 4, 隕石の更新と描画

"Game"クラスの"update()"メソッドで、
隕石の発生処理と、更新を行います。

```python: main.py(Gameクラスのupdateメソッドに追加)
self.check_interval() # 隕石の追加

# 隕石の更新
for asteroid in self.asteroids:
    asteroid.update()
    self.overlap_spr(asteroid)
```

次に、"draw()"メソッドで隕石の描画をまとめて行います。

```python: main.py(Gameクラスのdrawメソッドに追加)
# 隕石の描画
for asteroid in self.asteroids:
    asteroid.draw()
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

class AsteroidSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)
        self.index = random.randint(2, 7) # 隕石画像

    def draw(self):
        """ 描画処理 """
        pyxel.blt(self.x, self.y, 0, self.w*self.index, 0, 
                self.w, self.h, 0) # Ship
```

```python: main.py
import pyxel
import math
import random
import sprite

W, H = 160, 120
SHIP_SPD = 1.4

ASTEROID_INTERVAL = 20 # 隕石の発生間隔
ASTEROID_LIMIT = 30 # 隕石の最大数

ASTEROID_SPD_MIN = 1.0 # 隕石の最低速度
ASTEROID_SPD_MAX = 2.0 # 隕石の最高速度
ASTEROID_DEG_MIN = 30 # 隕石の最低角度
ASTEROID_DEG_MAX = 150 # 隕石の最高角度

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # プレイヤーを初期化
        self.ship = sprite.ShipSprite(W/2, H - 40)
        deg = 0 if random.random()<0.5 else 180
        self.ship.move(SHIP_SPD, deg)

        # 隕石
        self.asteroid_time = 0
        self.asteroids = []

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("shooter.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # プレイヤーを更新
        self.ship.update()
        self.control_ship()
        self.overlap_spr(self.ship)

        self.check_interval() # 隕石の追加

        # 隕石の更新
        for asteroid in self.asteroids:
            asteroid.update()
            self.overlap_spr(asteroid)

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

        # プレイヤーを描画
        self.ship.draw()

        # 隕石の描画
        for asteroid in self.asteroids:
            asteroid.draw()

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

    def check_interval(self):
        # 隕石の出現間隔
        self.asteroid_time += 1
        if self.asteroid_time < ASTEROID_INTERVAL: return
        self.asteroid_time = 0
        # 隕石の最大数を超えない範囲で
        if ASTEROID_LIMIT < len(self.asteroids): return
        # 隕石の追加
        x = random.random() * W
        y = 0
        spd = random.uniform(ASTEROID_SPD_MIN, ASTEROID_SPD_MAX)
        deg = random.uniform(ASTEROID_DEG_MIN, ASTEROID_DEG_MAX)
        asteroid = sprite.AsteroidSprite(x, y)
        asteroid.move(spd, deg)
        self.asteroids.append(asteroid)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/675e49a3e4d34b/08_01.gif)

# 次回は...

ここまで読んでいただきありがとうございました。
次回のタイトルは「弾丸を発射しよう」です。
お楽しみに!!