---
title: "第4章: プレイヤーを用意しよう"
---

# プレイヤーを用意しよう

今回は、背景の上に"操作するプレイヤー"を表示します。

## 1, スプライトモジュールを用意する

コードが増えてくると、1つのファイルにすべてを書くのは大変になります。
そこで、スプライトに関する処理を別ファイルに分けます。

プレイヤー用のスプライトを定義する、専用のモジュールを用意します。
ファイル名は"sprite.py"として以下の様に用意してください。

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py <- スプライトモジュール
　└ images/
　 　└ bg_temple.png
```

スプライトモジュールには、
次のように、"arcade.Sprite"を継承した2つのクラスを定義します。

```python:sprite.py
import arcade

class BaseSprite(arcade.Sprite):

    def __init__(self, filename, x, y):
        super().__init__(filename)
        # Position
        self.center_x = x
        self.center_y = y

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
```

"BaseSprite"は、すべてのスプライトで共通の処理をまとめるための基底クラスです。
今回は"位置の初期化"だけを担当します。

"Player"は、今回の主役であるプレイヤーの設計図です。
"BaseSprite"を継承しておきます。

## 2, プレイヤー画像を用意する

"images"フォルダに、新たに"ninja"フォルダを作り、以下の画像を格納します。
(今回の主役は忍者!!)

| 画像 | ファイル名 |
| ---- | ---- |
| ![](/images/28713ff37533c0/ninja/front_01.png) | front_01.png |

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ sprite.py
　└ images/
　 　├ bg_temple.png
　　 └ ninja/ <- 忍者画像を格納するフォルダ
　　　　└ front_01.png
```

## 3, プレイヤースプライトを作る

"GameView"のコンストラクタで、先ほど用意した"Player"クラスからスプライトを作ります。
前回と同様に、複数のスプライトをまとめて管理、描画するために、"arcade.SpriteList"を使います。

"sprite.Player()"の引数にはそれぞれ、"画像のパス", "x座標", "y座標"を指定します。

```python:main.py(抜粋)
# プレイヤーリストを用意する
self.players = arcade.SpriteList()

# プレイヤースプライトを作る
self.player = sprite.Player("images/ninja/front_01.png",
                            x=self.w/2, y=self.h/2)

self.players.append(self.player) # プレイヤーリストに追加する
```

## 4, プレイヤースプライトを更新する

"GameView"の"on_update()"メソッドで、プレイヤーリストを一括で更新します。
現状でプレイヤーは動きませんが、このタイミングで座標を更新しつつスプライトを移動させます。

```python:main.py(抜粋)
self.players.update(delta_time) # プレイヤーリストを更新
```

## 5, プレイヤースプライトを描画する

"GameView"の"on_draw()"メソッドで、プレイヤーリストを一括で描画します。
(前回の背景スプライトと同じですね)

```python:main.py(抜粋)
self.players.draw() # プレイヤーリストを描画
```

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。
コードをそのままコピーしても動作します。

:::details 完成コード
```python:sprite.py(完成コード)
import arcade

class BaseSprite(arcade.Sprite):

    def __init__(self, filename, x, y):
        super().__init__(filename)
        # Position
        self.center_x = x
        self.center_y = y

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
```

```python:main.py(完成コード)
import arcade
import sprite

class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width # ゲーム画面の幅
        self.h = self.window.height # ゲーム画面の高さ

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景スプライト
        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = self.w / 2
        bkg.center_y = self.h / 2
        self.backgrounds.append(bkg)

        # プレイヤーリストを用意する
        self.players = arcade.SpriteList()

        # プレイヤースプライトを作る
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=self.w/2, y=self.h/2)

        self.players.append(self.player) # プレイヤーリストに追加する

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        self.players.update(delta_time) # プレイヤーリストを更新

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw() # プレイヤーリストを描画

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    game = GameView(window)
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/28713ff37533c0/04_01.png)

# 次回は...

ここまで読んでいただき、ありがとうございました。
次回のタイトルは「プレイヤーを動かしてみよう」です。
お楽しみに👍