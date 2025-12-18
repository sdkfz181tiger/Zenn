---
title: "第4章: プレイヤーを用意しよう"
---

# プレイヤーを用意しよう

今回は、プレイヤーを用意します。

## 1, スプライトモジュールを用意する

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
import math
import random

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

## 2, プレイヤー画像を用意する

"images"フォルダに、新たに"ninja"フォルダを作り、以下の画像を格納します。
(今回の主役は忍者!!)

| 画像 | ファイル名 | 画像 | ファイル名 | 画像 | ファイル名 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| ![](/images/28713ff37533c0/ninja/front_01.png) | front_01.png | ![](/images/28713ff37533c0/ninja/front_02.png) | front_02.png | ![](/images/28713ff37533c0/ninja/front_03.png) | front_03.png |
| ![](/images/28713ff37533c0/ninja/front_04.png) | front_04.png | ![](/images/28713ff37533c0/ninja/front_05.png) | front_05.png |

フォルダ構成は次の通りです。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　└ images/
　 　├ bg_temple.png <- 背景画像
　　 └ ninja/
　　　　├ front_01.png
　　　　├ front_02.png
　　　　├ front_03.png
　　　　├ front_04.png
　　　　└ front_05.png
```

# 完成コード

ここまでの機能を実装した完成コードは、次の通りです。

:::details 完成コード
```python:main.py(完成コード)

```
:::

実行結果は次のようになります。

![](/images/28713ff37533c0/03_01.png)

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「xxxしよう」です。
お楽しみに!!