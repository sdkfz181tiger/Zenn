---
title: "第14章(付録2): 実行してみよう(VS-Code編)"
---

# 実行してみよう(VS-Code編)

ここでは、VS-Codeを使った開発環境の構築手順を紹介します。

(あらかじめ、[第13章(付録1): 実行してみよう(IDLE編)](https://zenn.dev/sdkfz181tiger/books/c4a251dd2b1b94/viewer/chap13)でPythonをインストールした上で読み進めてください)

## 1, VS-Codeのダウンロード&インストール
[公式サイト](https://code.visualstudio.com/)から、"Download for xxx"をクリックし、
インストーラーをダウンロード&インストールします。

![](/images/c4a251dd2b1b94/03_vscode_01.png)

## 2, VS-Codeを立ち上げよう

インストール後、"VS-Code"を立ち上げます。

### Macの場合

Finderから、次の手順で"VS-Code"を立ち上げます。

Applications -> Visual Studio Code.app

![](/images/c4a251dd2b1b94/03_vscode_02.png)

### Winの場合

スタートメニューから、次の手順で"VS-Code"を立ち上げます。

スタートメニュー -> 検索窓で"Visual" -> Visual Studio Code

![スクリーンショット待ち...](/images/c4a251dd2b1b94/02_idle_win_01.png)

## 3, エクステンションをインストール

"VS-Code"左側のメニュー、"エクステンション"ボタンをクリックし、
検索窓で"python"を検索&インストールします。

![](/images/c4a251dd2b1b94/03_vscode_04.png)

## 4, フォルダを開く

前回、[第13章(付録1): 実行してみよう(IDLE編)](https://zenn.dev/sdkfz181tiger/books/c4a251dd2b1b94/viewer/chap13)で作ったフォルダを、次の手順で開きます。

File -> Open Folder

![](/images/c4a251dd2b1b94/03_vscode_05.png)

フォルダを初めて開くと、次の様なダイアログが表示されます。
チェックボックスにチェックを入れた上で、"Yes, I trust the authors"(このフォルダの作者を信用します)をクリックします。

![](/images/c4a251dd2b1b94/03_vscode_06.png)

## 5, 実行する

"VS-Code"左側のファイル名、"main.py"を選択すると、コードが表示されます。
コードを次のように書き換え、"File -> Save"で保存し、右上にある"Run"ボタンで実行します。

```python:main.py
print("Hello, VS-Code!!")
```

実行結果が、"TERMINAL"に表示されれば成功です。

![](/images/c4a251dd2b1b94/03_vscode_07.png)

# 終わりに...

VS-Codeでの実行環境構築については以上になります。
ここまで読んでいただき有り難うございました。