---
title: "付録: 実行してみよう(インストール編)"
---

# Pythonの開発環境を構築する

ここでは、Pythonの開発環境の構築手順を紹介します。

## 1, Pythonのダウンロード&インストール
[公式サイト](https://www.python.org/downloads/)から"Python"インストーラーをダウンロードし、インストールします。

![](/images/c4a251dd2b1b94/02_install_01.png)

## 2, IDLEを立ち上げよう

Pythonをインストールすると、同時に専用のエディタ"IDLE"もインストールされます。
次の手順で、"IDLE"を立ち上げてみます。

### Macの場合

Finderから、次の手順で"IDLE"を立ち上げます。

Applications -> Python 3.xx -> IDLE.app

![](/images/c4a251dd2b1b94/02_idle_mac_01.png)

### Winの場合

スタートメニューから、次の手順で"IDLE"を立ち上げます。

スタートメニュー -> すべてのアプリ -> Python 3.xx -> IDLE(Python 3.xx 64-bit)

TODO: スクリーンショット

## 3, 文字を表示してみよう

Pythonで挨拶をしてみます。
(ここからは、Macの画面で説明しますが、Winの場合も基本的に同じ操作です)
IDLEのシェルウィンドウに、次のコードを打ち込み、"Enter"キーを押してみましょう。

```python:IDLE
print("Hello, Python!!")
```

"Hello, Python!!"と表示されれば成功です。

![](/images/c4a251dd2b1b94/02_idle_01.png)

## 4, プログラムをファイルに保存する

プログラムをファイルに保存し、いつでも使える様にします。

### 4-1, 新規ファイル

上部メニューの"File"から、次の手順で新規ファイルを用意します。

File -> New File

![](/images/c4a251dd2b1b94/02_idle_02.png)

### 4-2, コードを入力する

"/*/* untitled /*/*"というウィンドウが開きます。
この画面に次のコードを入力します。

```python:IDLE
print("Hello, IDLE!!")
```

![](/images/c4a251dd2b1b94/02_idle_03.png)

### 4-3, ファイルを保存する

次の手順でファイルを保存します。
ファイル名は"main.py"とします。(ファイルの保存場所は自由です)

File -> Save

![](/images/c4a251dd2b1b94/02_idle_04.png)

### 4-4, プログラムを実行する

上部メニューの"Run"から、次の手順でプログラムを実行します。

Run -> Run Module

![](/images/c4a251dd2b1b94/02_idle_05.png)

シェルウィンドウに、"Hello, IDLE!!"の文字が表示されれば成功です。

![](/images/c4a251dd2b1b94/02_idle_06.png)

以上の手順を繰り返し、コーディングを進めていきます。

## 5, ファイルを開く

ファイルに保存したプログラムを再び開くときは、次の手順でファイルを開きます。

File -> Open

![](/images/c4a251dd2b1b94/02_idle_07.png)

先ほど保存した"main.py"ファイルを指定すると、コードが表示されます。

![](/images/c4a251dd2b1b94/02_idle_08.png)

# 次回は...

ここまで読んでいただき有り難うございました。
次回のタイトルは「計算してみよう」です。
お楽しみに!!