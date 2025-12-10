---
title: "第7章: スプライトをクリックで止めよう"
---

# スプライトをクリックで止めよう

今回は、スプライトに対するクリック判定と、状態管理を実装します。

## 1, DemonSpriteクラスを改良する

DemonSpriteクラスのコンストラクタに、新たにメンバ変数、"dead"を追加します。
これは、スプライトの生死を管理するフラグとして利用します。
初期値は"False"(生きている)とし、鬼スプライトをクリックしたタイミングで"True"(死んでいる)にします。

```python:sprite.py(抜粋)
def __init__(self, cvs, x, y, r):
    self.x = x
    self.y = y
    self.r = r
    self.vx = 0
    self.vy = 0
    self.dead = False # 死亡フラグ
    # 円
    self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                fill="white", width=0)
```

次に、スプライトを死亡状態に変更する"die()"メソッドを追加します。
ここでは、"dead"フラグをTrueに変更して停止、そして円を"赤"に変更します。

```python:sprite.py(抜粋)
def die(self, cvs):
    self.dead = True # 死亡フラグをTrueに
    self.stop() # 停止する
    # 円の色を更新
    cvs.itemconfig(self.oval, fill="red")
```

次に、スプライトの死亡状態を返す、"is_dead()"メソッドを追加します。
返り値が"False"であれば、生きている状態、"True"であれば、死んでいる状態とします。

```python:sprite.py(抜粋)
def is_dead(self):
    return self.dead # 死亡フラグを返す
```

最後に、クリックした座標を受け取り、スプライトの座標との距離を計算する、"is_hit()"メソッドを追加します。
計算された距離"dist"が、半径"r"より小さい時は"True"を、大きい時は"False"を返します。
(円と、クリックされた座標が"重なっているか"を確認しているだけです)

```python:sprite.py(抜粋)
def is_hit(self, x, y):
    dist_x = (self.x - x) ** 2 # スプライトの水平方向の距離
    dist_y = (self.y - y) ** 2 # スプライトの垂直方向の距離
    dist = (dist_x + dist_y) ** 0.5 # スプライトとの距離
    return dist < self.r # スプライトとの距離が半径以内ならヒット(True)
```

## 2, main.pyを改良する

"main.py"に実装した、"on_mouse_clicked()"関数では、クリックした座標を取得することができます。
このタイミングで、スプライトそれぞれと距離を計算してクリック判定を行います。

ここで、死亡フラグが"True"になっているスプライトに対して判定を行う必要が無いので、
"is_dead()"を使って死亡フラグを確認します。
死亡フラグが"True"の時は、"continue"でキャンセルし、次のスプライトを調べていきます。

```python:main.py(抜粋)
def on_mouse_clicked(e):
    print("Clicked:", e.x, e.y)

    # 鬼軍団
    for demon in demons:
        if demon.is_dead(): continue # 既に死んでいたら次のスプライトへ
        if demon.is_hit(e.x, e.y): # クリック座標がヒットしていたら
            demon.die(cvs) # 死亡フラグをOnにする
            break # 繰り返し処理を終了
```

ここまでの処理を実装すると、スプライトをクリックで止めることができるようになります。

![](/images/0fc9f54eefe9fd/06_01.gif)

## x, 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

```python:sprite.py(完成コード)

```

```python:main.py(完成コード)

```

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「xxx」です。
お楽しみに!!