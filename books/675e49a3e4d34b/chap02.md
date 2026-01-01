---
title: "第2章: ゲーム画面を作ってみよう"
---

# ゲーム画面を作ってみよう

今回は、"Pyxel"を使ってゲーム画面を作ります。
※完成コードは最後に記述してあります。

## 1, 作業用フォルダを用意する

作業用フォルダを用意し、"main.py"ファイルを作ります。
ファイルの作り方に関しては、[プログラムをファイルに保存する](https://zenn.dev/sdkfz181tiger/books/c4a251dd2b1b94/viewer/chap99#4%2C-%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AB%E4%BF%9D%E5%AD%98%E3%81%99%E3%82%8B)を参考にしてください。

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　└ main.py <- プログラムを記述するファイル 
```

以降、"main.py"ファイルに具体的なコードを記述していきます。

## 2, Pyxelの基本パターン

"main.py"では、Pyxelエンジンや、必要なモジュールをインポートします。
以降、"Game"クラスの中に、ゲームの処理を実装していきます。

```python: main.py(抜粋)
import pyxel # Pyxelゲームエンジン
import math # 数学用モジュール
import random # 乱数用モジュール

W, H = 160, 120 # ゲーム画面の幅、高さ

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """
        pass

    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理 """
        pass

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```

## 3, Pyxelを起動する

"Game"クラスのコンストラクタで、ゲーム画面の初期化を行います。

具体的には、"pyxel.init()"メソッドで、次の値を指定します。
- ゲーム画面の幅
- ゲーム画面の高さ
- ゲーム画面のタイトル

次に続く、"pyxel.run()"の引数では、次の2つのメソッドを指定します。
- 更新処理のメソッド
- 描画処理のメソッド

```python: main.py(抜粋)
def __init__(self):
    """ コンストラクタ """
    # Pyxelの起動
    pyxel.init(W, H, title="Hello, Pyxel!!")
    pyxel.run(self.update, self.draw)
```

以降、キャラクターの移動や衝突判定を、"self.update()"メソッドで、
キャラクターなどの描画処理を、"self.draw()"メソッドに記述します。

## 4, 背景色

"self.draw()"メソッドの最初の行で、画面を単色に塗りつぶします。

"pyxel.cls()"の引数に、"0 ~ 15"までの数値を指定すると、
その色で画面全体をクリア(塗りつぶし)します。

```python: main.py(抜粋)
def draw(self):
    """ 描画処理 """
    pyxel.cls(0)
```

色の番号については次の画像を参考にしてください。
![](/images/675e49a3e4d34b/02_01.png)

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python: main.py
import pyxel # Pyxelゲームエンジン
import math # 数学用モジュール
import random # 乱数用モジュール

W, H = 160, 120 # ゲーム画面の幅、高さ

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/675e49a3e4d34b/02_02.png)

# 次回は...

ここまで読んでいただきありがとうございました。
次回のタイトルは「リソースファイルを用意しよう」です。
お楽しみに!!