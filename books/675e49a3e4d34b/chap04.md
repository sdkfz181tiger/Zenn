---
title: "第4章: テキストを表示しよう"
---

# テキストを表示しよう

今回は、ゲーム画面にスコアを表示します。

## 1, テキストを表示する

テキスト表示は、Pyxelの中でも特にシンプルな機能のひとつです。
"座標、文字列、色"を指定するだけで、すぐに画面に表示できます。

"pyxel.text()"メソッドの引数に次の値を指定します。

- x座標
- y座標
- 表示する文字列
- 文字の色

```python: main.py
pyxel.text(10, 10, "HELLO, TEXT!!", 12)
```

# 完成コード

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
        pyxel.load("shooter.pyxres")
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

![](/images/675e49a3e4d34b/04_01.gif)

# 次回は...

ここまで読んでいただきありがとうございました。
次回のタイトルは「Spriteクラスを用意しよう」です。
お楽しみに!!