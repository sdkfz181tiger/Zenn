---
title: "第13章(番外編): 流れる星を演出しよう"
---

# 流れる星を演出しよう

今回は、流れる星の背景を用意して、ゲーム画面を賑やかに演出します。
ここでは、サンプルコードのみの紹介です。

※完成コードは最後に記述してあります。

## 1, 星を描画するクラス

"sprite.py"に、星を描画する"Star"クラスと、
背景全体の星を更新&描画する、"Background"クラスを用意します。

```python: sprite.py(抜粋)
class Star():

    def __init__(self, x, y, w, h):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = random.randint(0, 15)
        self.spd = random.randint(1, 3)

    def update(self):
        """ 更新処理 """
        self.y += self.spd
        if self.h < self.y: self.y = 0

    def draw(self):
        """ 描画処理 """
        pyxel.pset(self.x, self.y, self.c)

class Background():

    def __init__(self, w, h):
        """ コンストラクタ """
        self.w = w # ゲーム画面の幅
        self.h = h # ゲーム場面の高さ
        self.stars = [] # 星を管理するリスト
        for i in range(30):
            x = random.randint(0, w)
            y = random.randint(0, h)
            star = Star(x, y, self.w, self.h)
            self.stars.append(star)

    def update(self):
        """ 更新処理 """
        for star in self.stars:
            star.update()

    def draw(self):
        """ 描画処理 """
        for star in self.stars:
            star.draw()
```

## 2, 背景クラスを利用する

最初に、"main.py"の、"Game"クラスのコンストラクタで、
"Background"クラスを作ります。

```python: main.py(Gameクラスのコンストラクタ内)
# 背景
self.background = sprite.Background(W, H)
```

次に、"update()"で、更新処理を実行します。

```python: main.py(Gameクラスのコンストラクタ内)
# 背景
self.background.update()
```

最後に、"draw()"で、描画処理を実行します。

```python: main.py(Gameクラスのコンストラクタ内)
# 背景
self.background.draw()
```

上記のように、必要な処理をクラスにまとめておくことで、
コードをシンプルにすることができるようになります。

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

    def intersects(self, other):
        """ 矩形同士の当たり判定(AABB) """
        if other.x + other.w < self.x: return False
        if self.x + self.w < other.x: return False
        if other.y + other.h < self.y: return False
        if self.y + self.h < other.y: return False
        return True

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

class Star():

    def __init__(self, x, y, w, h):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = random.randint(0, 15)
        self.spd = random.randint(1, 3)

    def update(self):
        """ 更新処理 """
        self.y += self.spd
        if self.h < self.y: self.y = 0

    def draw(self):
        """ 描画処理 """
        pyxel.pset(self.x, self.y, self.c)

class Background():

    def __init__(self, w, h):
        """ コンストラクタ """
        self.w = w # ゲーム画面の幅
        self.h = h # ゲーム場面の高さ
        self.stars = [] # 星を管理するリスト
        for i in range(30):
            x = random.randint(0, w)
            y = random.randint(0, h)
            star = Star(x, y, self.w, self.h)
            self.stars.append(star)

    def update(self):
        """ 更新処理 """
        for star in self.stars:
            star.update()

    def draw(self):
        """ 描画処理 """
        for star in self.stars:
            star.draw()
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

BULLET_SPD = 3

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # ゲームオーバーフラグ
        self.game_over_flg = False

        # スコアを初期化
        self.score = 0

        # 背景
        self.background = sprite.Background(W, H)

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

        # サウンド(ショット)
        pyxel.sound(0).set("c4g3", 
            tones="p", volumes="76",
            effects="f", speed=20)

        # サウンド(ヒット)
        pyxel.sound(1).set("e4d4c4", 
            tones="p", volumes="76",
            effects="n", speed=20)

        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # ゲームオーバー
        if self.game_over_flg:
            return

        # 背景
        self.background.update()

        # プレイヤーを更新
        self.ship.update()
        self.control_ship()
        self.overlap_spr(self.ship)

        self.check_interval() # 隕石の追加

        # 隕石の更新
        for asteroid in self.asteroids:
            asteroid.update()
            self.overlap_spr(asteroid)
            # 衝突判定(隕石 x プレイヤー)
            if asteroid.intersects(self.ship):
                self.game_over_flg = True # ゲームオーバー

        # 弾丸の更新(逆順)
        for bullet in self.bullets[::-1]:
            bullet.update()
            # 画面外削除
            if bullet.y < 0:
                self.bullets.remove(bullet)
                continue
            # 衝突判定(弾丸 x 隕石)
            for asteroid in self.asteroids[::-1]:
                if asteroid.intersects(bullet):
                    self.score += 1 # スコア
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)

                    # サウンド(channel, sound)
                    pyxel.play(1, 1)
                    return

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # 背景
        self.background.draw()

        # ゲームオーバー
        if self.game_over_flg:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 13)

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

            # サウンド(channel, sound)
            pyxel.play(0, 0)

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

![](/images/675e49a3e4d34b/13_01.png)

# 終わりに...

ここまで読んでいただきありがとうございました。
この連載が、ゲーム開発のきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว
(よろしければ👍頂けると大変励みになります!!)