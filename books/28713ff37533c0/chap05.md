---
title: "第5章: プレイヤーを動かしてみよう"
---

# プレイヤーを動かしてみよう

今回は、プレイヤーを動かしてみます。

## 1, プレイヤースプライトを改良する

最初に、"math"モジュールをインポートします。
このモジュールは、数学的計算を手軽に扱える定番モジュールの一つです。

```python:python:sprite.py(抜粋)
import math # 数学的計算をするモジュール
```

## 2, 移動速度を格納する変数を追加する

ここからは、スプライトの基底クラス"BaseSprite"に機能を追加していきます。

コンストラクタでは、
x方向の速度を格納する変数"vx"と、
y方向の速度を格納する変数"vy"を追加します。

```python:sprite.py(BaseSprite内)
def __init__(self, filename, x, y):
    super().__init__(filename)
    # Position
    self.center_x = x
    self.center_y = y
    # Velocity
    self.vx = 0 # x方向の速度
    self.vy = 0 # y方向の速度
```

## 3, 更新メソッドで座標に速度を加算する

"update()"メソッドを追加し、速度を座標に適用する処理を実装します。

```python:sprite.py(BaseSprite内)
def update(self, delta_time):
    """ Update """
    super().update(delta_time)
    self.center_x += self.vx * delta_time # x座標を更新
    self.center_y += self.vy * delta_time # y座標を更新
```

ここでは、"vx"と"vy"に"delta_time"を掛けた値を加算しています。
"delta_time"は、前フレームからの経過時間です。
つまり、約1秒後に"vx"、"vy"分だけの距離を移動する事になります。
毎フレーム実行し続けることで、座標が少しづつ変化するという訳ですね。

## 4, 移動を開始するメソッドを用意する

"move()"メソッドを追加し、移動速度と角度を指定する処理を実装します。
このメソッドは、引数に"速度"、"角度"を指定し実行します。

```python:sprite.py(抜粋)
def move(self, spd, deg):
    """ Move Sprite """
    rad = deg * math.pi / 180 # 度数法から弧度法へ変換
    self.vx = spd * math.cos(rad) # x方向の速度
    self.vy = spd * math.sin(rad) # y方向の速度
```

"math"モジュールの"math.py"は"円周率"のことです。
これを使って度数法(0° ~ 180°)を、弧度法(0.0 ~ 3.14)へ変換しています。

次に、spd(速度)に対し、"cos"を掛け算し"x"方向の速度として"vx"に代入します。
同様にして、"sin"を掛け算し"y"方向の速度として"vy"に代入しています。
("cos"や、"sin"が出てくるのはここだけなので、深追いしなくても大丈夫ですよ)

## 5, 停止するメソッドを用意する

"stop()"メソッドを追加し、止める処理を実装します。
このメソッドは、単純に"vx"と、"vy"に0を代入するだけです。

```python:sprite.py(抜粋)
def stop(self):
    """ Stop Sprite """
    self.vx = 0 # x方向の速度を0に
    self.vy = 0 # y方向の速度を0に
```

## 6, テストしてみる




# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python:sprite.py(完成コード)

```

```python:main.py(完成コード)

```
:::

実行結果は次のようになります。

![](/images/28713ff37533c0/04_01.png)

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「xxxしよう」です。
お楽しみに!!