---
title: "第9章: 弾丸を発射しよう"
---

# 弾丸を発射しよう

今回は、プレイヤースプライトから弾丸を発射する処理を実装します。

この章では、
- 新しいスプライト（弾丸）を追加する
- 複数の弾丸をリストで管理する
- 不要になった弾丸を削除する
といった、シューティングゲームの基本的な仕組みを作っていきます。

※完成コードは最後に記述してあります。

## 1, 弾丸スプライトを用意する

前回と同様に、"sprite.py"に、新たに"BulletSprite"クラスを追加します。

ここではシンプルに画像は使わず、
"pyxel.rect()"を利用して、2×2の正方形を描画します。
小さな弾を表現するには、これで十分です。

```python: sprite.py(クラスを追加)
class BulletSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)
        self.x += self.w / 2 - 1 # 中央に調整

    def draw(self):
        """ 描画処理 """
        pyxel.rect(self.x, self.y, 2, 2, 12)
```

## 2, 定数を用意する

"main.py"に、弾丸の速度として、次の定数を追加します。

定数にしておくことで、
後から弾速を調整したくなった場合も簡単に変更できます。

```python: main.py(定数を追加)
BULLET_SPD = 3 # 弾丸の速度
```

## 3, 弾丸を発射する

次に、弾丸を発射する処理を追加します。

このサンプルでは、
プレイヤーが左右に切り返す"スペースキーを押す"タイミングで、
弾丸を発射するようにしています。

弾丸は、真上方向(270度)に移動させます。

```python: main.py(Gameクラスの"control_ship()"メソッドに追加)
def control_ship(self):
    """ アクション """
    if pyxel.btnp(pyxel.KEY_SPACE):
        self.ship.flip_x() # 移動反転
        # 弾丸発射
        bullet = sprite.BulletSprite(self.ship.x, self.ship.y)
        bullet.move(BULLET_SPD, 270)
        self.bullets.append(bullet)
```

## 4, 弾丸の更新と描画

続いて、弾丸の更新処理を追加します。

"Game"クラスの"update()"メソッドでは、
すべての弾丸を更新し、画面外に出た弾丸を削除します。

ここでは、走査中に要素を削除するため、
リストを逆順に処理しています。
この方法を使うことで、インデックスずれによる不具合を防げます。

```python: main.py(Gameクラスのupdateメソッドに追加)
# 弾丸の更新(逆順)
for bullet in self.bullets[::-1]:
    bullet.update()
    # 画面外削除
    if bullet.y < 0:
        self.bullets.remove(bullet)
        continue
```

次に、"draw()"メソッドで弾丸をまとめて描画します。

```python: main.py(Gameクラスのdrawメソッドに追加)
# 弾丸の描画
for bullet in self.bullets:
    bullet.draw()
```

これで、プレイヤーが弾を撃てるようになりました。

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

class BulletSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)
        self.x += self.w / 2 - 1 # 中央に調整

    def draw(self):
        """ 描画処理 """
        pyxel.rect(self.x, self.y, 2, 2, 12)
```

```python: main.py
import pyxel
import math
import random
import sprite

W, H = 160, 120
SHIP_SPD = 1.4

ASTEROID_INTERVAL = 20
ASTEROID_LIMIT = 30

ASTEROID_SPD_MIN = 1.0
ASTEROID_SPD_MAX = 2.0
ASTEROID_DEG_MIN = 30
ASTEROID_DEG_MAX = 150

BULLET_SPD = 3 # 弾丸の速度

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

        # 弾丸
        self.bullets = []

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

        # 弾丸の更新
        for bullet in self.bullets[::-1]:
            bullet.update()
            # 画面外削除
            if bullet.y < 0:
                self.bullets.remove(bullet)
                continue

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

        # 弾丸の描画
        for bullet in self.bullets:
            bullet.draw()

    def control_ship(self):
        """ アクション """
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.ship.flip_x() # 移動反転
            # 弾丸発射
            bullet = sprite.BulletSprite(self.ship.x, self.ship.y)
            bullet.move(BULLET_SPD, 270)
            self.bullets.append(bullet)

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

![](/images/675e49a3e4d34b/09_01.gif)

# 次回は...

ここまで読んでいただきありがとうございました。
次回のタイトルは「衝突判定を実装しよう」です。
お楽しみに!!