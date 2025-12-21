---
title: "第11章(番外編): 画面を切り替えよう"
---

# 画面を切り替えよう

今回は、番外編として、画面の切り替えを行う例を紹介します。
"タイトル画面" → "ゲーム画面" → "結果画面" といった、
ゲームでよくある画面遷移を実装します。

## 1, ファイルを整理する

開発を続けていくに連れて、ソースコードを書くファイルも増えていくため、
管理が大変になっていきます。

そこで、ソースコードを格納する専用の"src"フォルダを作り、
画面単位で3つのモジュールに分割します。

| ファイル名 | 役割 | 格納場所 |
| ---- | ---- | ---- |
| title.py | タイトル画面 | src/title.py |
| game.py | ゲーム画面 | src/game.py |
| result.py | 結果画面 | src/result.py |

フォルダ構成は次のとおりです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　├ images/
　└ src/ <- ソースコードを格納するフォルダ
　 　├ title.py
　 　├ game.py
　 　└ result.py
```

## 2, 画面を切り替える

画面を切り替えるコードは、これまでの事例と同じです。

以下と同様の処理を、画面切り替えの必要なタイミングで実装します。
"arcade.View"を生成し、"window.show_view()"メソッドに渡すだけで切り替えられます。

```python:python:main.py(完成コード)
view = title.TitleView(window) # TitleView
window.show_view(view)
```

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。
SPACEキーを押す事で、"タイトル画面" -> "ゲーム画面" -> "結果画面"に切り替わっていきます。
コードをそのままコピーしても動作します。

:::details 完成コード
```python:main.py(完成コード)
import arcade
import random
import src.title as title

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    view = title.TitleView(window) # TitleView
    window.show_view(view)
    arcade.run()

if __name__ == "__main__":
    main()
```

```python:title.py(完成コード)
import arcade
import random
import src.game as game

# Title
class TitleView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.background_color = arcade.color.PRUNE

        # Info
        self.msg_info = arcade.Text(
            "TITLE: SPACE TO NEXT", 
            window.width/2, window.height-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Space to Game
        if key == arcade.key.SPACE:
            view = game.GameView(self.window) # GameView
            self.window.show_view(view)

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()
```

```python:game.py(完成コード)
import arcade
import random
import src.result as result

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.background_color = arcade.color.DARK_SPRING_GREEN

        # Info
        self.msg_info = arcade.Text(
            "GAME: SPACE TO NEXT", 
            window.width/2, window.height-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Space to Result
        if key == arcade.key.SPACE: 
            view = result.ResultView(self.window) # ResultView
            self.window.show_view(view)

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()
```

```python:result.py(完成コード)
import arcade
import random
import src.title as title

# Result
class ResultView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.background_color = arcade.color.CERULEAN

        # Info
        self.msg_info = arcade.Text(
            "RESULT: SPACE TO NEXT", 
            window.width/2, window.height-20,
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Space to Title
        if key == arcade.key.SPACE:
            view = title.TitleView(self.window) # TitleView
            self.window.show_view(view)

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()
```
:::

実行結果は次のようになります。

![](/images/28713ff37533c0/11_01.gif)

# 終わりに...

ここまで読んでいただき、ありがとうございました。
この連載が、ゲーム開発のきっかけになれば幸いです。ޱ(ఠ皿ఠ)ว
(よろしければ👍頂けると大変励みになります!!)