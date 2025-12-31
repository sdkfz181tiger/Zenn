---
title: "第5章: キャラクターをクラスで管理してみよう"
---

# キャラクターをクラスで管理してみよう

ゲームに登場するキャラクターを、総称して"スプライト"と呼びます。
今回は、クラスを利用して、スプライトクラスを用意します。

"クラスって難しそう..."と感じるかもしれませんが、
ここでは、"仕組みをざっくり理解すること"を目的にします。

まずは、"キャラクターを1つの部品として扱えるようになる"ことを目指しましょう。

クラスについては、[12章:クラスを使ってみよう](https://zenn.dev/sdkfz181tiger/books/c4a251dd2b1b94/viewer/chap12)を確認しておくとスムーズです。

## 1, スプライトモジュールを用意する

新たに、"sprtite.py"というファイルを用意し、作業用フォルダに配置します。
フォルダ構成は次のようになります。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py <- spriteモジュール
　└ shooter.pyxres
```

## 2, スプライトの共通クラスを用意する

用意した、"sprtite.py"ファイルに、"BaseSprite"クラスを記述します。
このクラスが、全てのスプライトの共通クラスになります。

```python:sprite.py(抜粋)
import pyxel
import math
import random

class BaseSprite:

    def __init__(self, x, y, w=8, h=8):
        """ コンストラクタ """
        self.x = x # x座標
        self.y = y # y座標
        self.w = w # 画像の幅
        self.h = h # 画像の高さ

    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理(派生クラスで実装) """
        pass
```

## 3, プレイヤークラスを用意する

"sprtite.py"ファイルに続けて、"ShipSprite"クラスを用意します。
このクラスは"BaseSprite"クラスを継承させておきます。
プレイヤーは、このクラスから生成します。

```python:sprite.py(抜粋)
# 省略

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

## 4, プレイヤークラスを利用する

"main.py"クラスで、先ほど用意したプレイヤークラスを使います。
具体的には次の3ステップで利用します。

### 4-1, プレイヤーを初期化

"Game"クラスのコンストラクタで、プレイヤーオブジェクトを生成します。

```python:main.py(抜粋)
# プレイヤーを初期化(画面中央下に配置)
self.ship = sprite.ShipSprite(W/2, H - 40)
```

### 4-2, プレイヤーを更新

"Game"クラスの"update()"メソッドで、プレイヤーオブジェクトを更新します。
(今は動かずに停止している状態です)

```python:main.py(抜粋)
# プレイヤーを更新
self.ship.update()
```

### 4-3, プレイヤーを描画

"Game"クラスの"draw()"メソッドで、プレイヤーオブジェクトを描画します。

```python:main.py(抜粋)
# プレイヤーを描画
self.ship.draw()
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
        self.x = x # x座標
        self.y = y # y座標
        self.w = w # 画像の幅
        self.h = h # 画像の高さ
        self.vx = 0 # 移動速度(x方向)
        self.vy = 0 # 移動速度(y方向)

    def update(self):
        """ 更新処理 """
        self.x += self.vx # x方向に移動
        self.y += self.vy # y方向に移動

    def draw(self):
        """ 描画処理(派生クラスで実装) """
        pass

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
import sprite # spriteモジュールをインポート

W, H = 160, 120

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # プレイヤーを初期化
        self.ship = sprite.ShipSprite(W/2, H - 40)

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

![](/images/675e49a3e4d34b/05_01.png)

# 次回は...

ここまで読んでいただきありがとうございました。
次回のタイトルは「スプライトを動かそう」です。
お楽しみに!!