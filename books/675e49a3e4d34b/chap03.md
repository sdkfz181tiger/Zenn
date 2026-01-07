---
title: "第3章: リソースファイルを用意しよう"
---

# リソースファイルを用意しよう

今回は、"Pyxel Editor"を使って、ゲームで利用する素材を用意します。
※完成コードは最後に記述してあります。

## 1, Pyxel Editorを起動する

"Pyxel Editor"は、画像やサウンドなどのデータをまとめて管理するツールです。
これらのデータは、"pyxres"形式のファイルにまとめて管理します。

エディタは次のコマンドで起動することができます。
("$"マークはコマンドに含めません)

```command: Pyxel Editorを起動する
$ pyxel edit ファイル名.pyxres
```

![](/images/675e49a3e4d34b/03_01.png)

## 2, ドット絵を描いてみよう

"Pyxel Editor"の詳しい使い方については、以下のサイトの解説がとても参考になります。

- [Pyxel Editor使用方法まとめ](https://note.com/koide_mizu1433/n/n289cf5c5c785)
- [Pyxelでゲームを作る - エディターを使う -](https://qiita.com/hiro_underclass/items/2cf51f4edfbda7864929)
- [Pyxel エディタでいろいろ作ってみよう](https://www.tento-net.com/learning-materials/python/app/pyxel/pyxel-05/)

今回は、次のような素材を用意しました。
- 宇宙船x2
- 隕石x6
- ブースターx2

[リソースファイルをダウンロード](https://github.com/sdkfz181tiger/Zenn/blob/main/images/675e49a3e4d34b/shooter.pyxres) (右上の"ダウンロード"ボタンを押してダウンロードしてください)

![](/images/675e49a3e4d34b/03_02.png)

## 3, pyxresファイルを配置する

作成された、".pyxres"ファイルを、作業用フォルダに配置します。
フォルダ構成は次のようになります。

```text:フォルダ構成
作業用フォルダ/
　├ main.py
　└ shooter.pyxres <- pyxresファイルを配置する
```

## 4, pyxresファイルを読み込む

次に、配置した、".pyxres"ファイルを読み込む処理を実装します。
"Game"クラスのコンストラクタで、次のようにしてファイルを読み込みます。

```python: main.py(抜粋)
def __init__(self):
    """ コンストラクタ """

    # Pyxelの起動
    pyxel.init(W, H, title="Hello, Pyxel!!")
    pyxel.load("shooter.pyxres") # pyxresファイルを読み込む
    pyxel.run(self.update, self.draw)
```

## 5, 画像を表示する

読み込んだ"pyxres"ファイルから、描いた画像を切り出します。
"Game"クラスの"draw()"メソッドで、宇宙船1の部分だけ切り出して表示します。

"pyxel.blt()"メソッドは、
"画像の一部を切り出して、画面に貼り付ける"命令です。
引数の意味は以下のとおりです。

- ゲーム画面の描画位置(x座標)
- ゲーム画面の描画位置(y座標)
- イメージバンクの番号
- Pyxel Editorに描いた左上のx座標
- Pyxel Editorに描いた左上のy座標
- Pyxel Editorに描いた画像の幅
- Pyxel Editorに描いた画像の高さ
- 透明扱いにする色の指定

```python: main.py(抜粋)
def draw(self):
    """ 描画処理 """
    pyxel.cls(0)

    # 宇宙船1のテスト
    pyxel.blt(20, 20, 0, 0, 0, 8, 8, 0) # 宇宙船1
    pyxel.blt(20, 28, 0, 0, 8, 8, 8, 0) # ブースター1
```

宇宙船1が、座標(20, 20)の位置に、
ブースター1が、座標(20, 28)の位置に表示されます。

![](/images/675e49a3e4d34b/03_03.png)

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

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("shooter.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # 宇宙船1のテスト
        pyxel.blt(20, 20, 0, 0, 0, 8, 8, 0) # 宇宙船1
        pyxel.blt(20, 28, 0, 0, 8, 8, 8, 0) # ブースター1
        
        # 宇宙船2のテスト
        pyxel.blt(30, 30, 0, 8, 0, 8, 8, 0) # 宇宙船2
        pyxel.blt(30, 38, 0, 8, 8, 8, 8, 0) # ブースター2

        # 隕石のテスト
        pyxel.blt(40, 40, 0, 16, 0, 8, 8, 0) # 隕石1
        pyxel.blt(50, 50, 0, 24, 0, 8, 8, 0) # 隕石2
        pyxel.blt(60, 60, 0, 32, 0, 8, 8, 0) # 隕石3
        pyxel.blt(70, 70, 0, 40, 0, 8, 8, 0) # 隕石4
        pyxel.blt(80, 80, 0, 48, 0, 8, 8, 0) # 隕石5
        pyxel.blt(90, 90, 0, 56, 0, 8, 8, 0) # 隕石5

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()
```
:::

実行結果は次のようになります。

![](/images/675e49a3e4d34b/03_04.png)

# 次回は...

ここまで読んでいただきありがとうございました。
次回のタイトルは「テキストを表示しよう」です。
お楽しみに!!