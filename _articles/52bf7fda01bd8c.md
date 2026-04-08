---
title: "VS-Codeでかんたんp5.js"
emoji: "🔰"
type: "tech"
topics:
  - "vscode"
  - "初心者"
  - "初心者向け"
  - "p5js"
  - "p5play"
published: true
published_at: "2021-08-14 00:14"
---

# VS-Codeであっさりp5.js
この記事は、VS-Codeを使ってp5.jsをサクッと始める方法についての手順書です。

いきなりですが、p5.jsを始めるのに最も簡単な方法は、[OpenProcessing](https://openprocessing.org/)や、[p5.jsエディタ](https://editor.p5js.org/)等の様な、Webサービスを利用する事だと思います。
「そうなの？じゃあそちらで!!」という方は[p5.jsをかじる本](https://zenn.dev/sdkfz181tiger/books/6693d767c90588)をご参照くださいませ。

# VS-Codeのダウンロードとインストール
VS-Codeのダウンロードとインストールについては、次のリンクに手順をまとめたものが御座いますのでご参照くださいませ。
[VS-Codeで"Hello JavaScript!!"まで最短で!!](https://zenn.dev/sdkfz181tiger/articles/e95252e9e98615)

# HTMLファイルとJavaScriptファイル
プロジェクトを用意し、HTMLファイルとJavaScriptファイルを用意します。
ファイル名は、以下の通りです。

- HTMLファイル: index.html
- JavaScriptファイル: main.js

![](https://storage.googleapis.com/zenn-user-upload/05c73e77c1eb5ba579994584.png)

# HTMLを記述する
HTMLファイルに、下記の3つのライブラリを読み込むタグを記述します。

- p5.js: メインのライブラリ
- p5.sound: サウンドを再生するライブラリ
- p5.play: スプライトを使う事が出来るライブラリ

これらは、CDN(Content Delivery Network)を使ってネットワークから直接ロードしています。
こうする事で、ライブラリ自体をフォルダに格納する必要が無くなります。(便利ですね!!)

HTMLファイル
```HTML:index.html
<html>
<head>
	<meta charset="UTF-8">
	<style type="text/css">body{margin:0px; padding:0px;}</style>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.4/p5.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.4/addons/p5.sound.min.js"></script>
	<script src="https://cdn.jsdelivr.net/gh/molleindustria/p5.play/lib/p5.play.js"></script>
	<script src="./main.js"></script>
</head>
<body>
</body>
</html>
```

# JavaScriptを記述する
JavaScriptファイルには、お馴染みのsetup関数、draw関数を記述します。

JavaScriptファイル
```JavaScript:main.js
function setup(){
	createCanvas(windowWidth, windowHeight);
	frameRate(8);
}

function draw(){
	background(33);
	fill(255);
	circle(width/2, height/2, 100);
}
```

これだけで、p5.jsの実行環境が整います。
プロジェクトの実行方法については、[VS-Codeで"Hello JavaScript!!"まで最短で!!](https://zenn.dev/sdkfz181tiger/articles/e95252e9e98615)をご参照ください。

![](https://storage.googleapis.com/zenn-user-upload/6ec1983a746ce72ca3b273da.png)

以上です。
ここまで読んでいただき有難うございました。

# おまけ

Youtubeもやっておりますので何卒よろしくお願い致します。

https://www.youtube.com/watch?v=bHtS5tgRmFY&list=PLnuMEhzF78PkNrJpv5E0aUzgxbVU2Ll6T&index=1