---
title: "第4章: テキストやグラフィックスを表示しよう"
---

# テキストやグラフィックスを表示しよう

今回は、ゲーム画面にスコアやグラフィックスを表示します。
※完成コードは最後に記述してあります。

## 1-1, テキストを表示する

テキスト表示は、Pyxelの中でも特にシンプルな機能のひとつです。
"pyxel.text()"メソッドの引数に次の値を指定します。

- x座標
- y座標
- 表示する文字列
- 文字の色

```python: main.py(抜粋)
pyxel.text(10, 10, "HELLO, TEXT!!", 12)
```

## 1-2, スコアをフォーマット表示する

スコアを表示する際、フォーマットを使うと便利です。
":04"となっている意味は、数値を4桁でゼロ埋め表示する指定です。

```python: main.py(抜粋)
# スコアを描画
pyxel.text(10, 10, 
    "SCORE:{:04}".format(self.score), 12)
```

## 1-3, 完成コード(テキスト)

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python: main.py
import pyxel
import math
import random

W, H = 160, 120

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """
        # スコアのテスト
        self.score += 1

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/books/675e49a3e4d34b/04_01.gif)

## 2-1, 様々なグラフィックスを表示する

Pyxelには、線や四角、円等のグラフィックスを描画するメソッドが用意してあります。

[Pyxel APIリファレンス](https://kitao.github.io/pyxel/web/api-reference/)では、Pyxelに用意された様々な機能を確認する事ができます。

```python: main.py(抜粋)
# 線を描画
# x1, y1, x2, y2, color
pyxel.line(0, 0, 50, 50, 1)

# 四角を描画
# x, y, w, h, color
pyxel.rect(90, 10, 10, 20, 2)
pyxel.rectb(120, 30, 30, 20, 3) # 線のみ

# 円を描画
# x, y, r, color
pyxel.circ(60, 80, 10, 4)
pyxel.circb(90, 50, 10, 5) # 線のみ

# 楕円を描画
# x, y, w, h, color
pyxel.elli(10, 60, 30, 10, 6)
pyxel.ellib(20, 80, 10, 30, 7) # 線のみ

# 三角形を描画
# x1, y1, x2, y2, x3, y3, color
pyxel.tri(90, 70, 70, 100, 110, 90, 8)
pyxel.trib(120, 70, 100, 100, 140, 90, 9) # 線のみ
```

## 2-2, 完成コード(グラフィックス)

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python: main.py
import pyxel
import math
import random

W, H = 160, 120

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!", fps=16)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # テキストを描画
        pyxel.text(10, 10, 
            "HELLO, GRAPHICS!!", 12)
        
        # 線を描画
        # x1, y1, x2, y2, color
        pyxel.line(0, 0, 50, 50, 1)

        # 四角を描画
        # x, y, w, h, color
        pyxel.rect(90, 10, 10, 20, 2)
        pyxel.rectb(120, 30, 30, 20, 3) # 線のみ

        # 円を描画
        # x, y, r, color
        pyxel.circ(60, 80, 10, 4)
        pyxel.circb(90, 50, 10, 5) # 線のみ

        # 楕円を描画
        # x, y, w, h, color
        pyxel.elli(10, 60, 30, 10, 6)
        pyxel.ellib(20, 80, 10, 30, 7) # 線のみ

        # 三角形を描画
        # x1, y1, x2, y2, x3, y3, color
        pyxel.tri(90, 70, 70, 100, 110, 90, 8)
        pyxel.trib(120, 70, 100, 100, 140, 90, 9) # 線のみ


def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/books/675e49a3e4d34b/04_02.png)

# 次回は...

ここまで読んでいただきありがとうございました。
次回のタイトルは「キャラクターをクラスで作ろう」です。
お楽しみに!!