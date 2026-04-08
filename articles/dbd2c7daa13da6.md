---
title: "WinBoxでかんたんウィンドウ"
emoji: "🔰"
type: "tech"
topics:
  - "javascript"
  - "初心者"
  - "初心者向け"
  - "ウィンドウ"
published: true
published_at: "2022-01-16 11:46"
---

# WinBoxとは!?
WinBoxを利用する事で、Windowsライクなウィンドウを簡単に実装する事ができます。

[WinBox](https://nextapps-de.github.io/winbox/)

![](https://storage.googleapis.com/zenn-user-upload/95667d37d8a0-20220116.png)

今回は、このライブラリを使ってウィンドウを実装していきます。
(簡単過ぎて驚きますよ!!)

![](https://storage.googleapis.com/zenn-user-upload/e582d63f955f-20220116.gif)

# プロジェクトを用意する
次の様にプロジェクトを作ります。

MyProject01/
　├ custom.css (スタイルを記述するファイルです)
　├ index.html (プログラムを起動するファイルです)
　├ main.js (メインのプログラムを記述するファイルです)

# HTMLファイルを用意する
では、作っていきましょう。
HTMLファイルを用意して、下記コードを記述します。

```HTML:index.html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8"/>
	<link rel="stylesheet" href="./custom.css"></style>
	<!-- Windowbox -->
	<script src="//cdn.jsdelivr.net/gh/nextapps-de/winbox@0.1.8/dist/winbox.bundle.js"></script>
</head>
<body>
	<!-- WinBoxを起動するボタン -->
	<p>
		<button onclick="showWagahai();">Windowを開く</button>
	</p>

	<!-- WinBox -->
	<div style="display: none">
		<div id="content">
			<h1>吾輩は猫である</h1>
			<h2>夏目漱石</h2>
			<p>
				吾輩は猫である。名前はまだ無い。どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。この書生というのは時々我々を捕えて煮て食うという話である。しかしその当時は何という考もなかったから別段恐しいとも思わなかった。ただ彼の掌に載せられてスーと持ち上げられた時何だかフワフワした感じがあったばかりである。掌の上で少し落ちついて書生の顔を見たのがいわゆる人間というものの見始であろう。この時妙なものだと思った感じが今でも残っている。第一毛をもって装飾されべきはずの顔がつるつるしてまるで薬缶だ。その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。のみならず顔の真中があまりに突起している。そうしてその穴の中から時々ぷうぷうと煙を吹く。どうも咽せぽくて実に弱った。これが人間の飲む煙草というものである事はようやくこの頃知った。
			</p>
		</div>
	</div>

	<script src="./main.js"></script>
</body>
</html>
```

WinBoxのライブラリは、CDNを使って読み込みをしておきます。
(こうしておく事で、プロジェクトがシンプルになりますね)

そして、WinBoxを利用して表示されるウィンドウの内容として、
"div"タグを用意し、id="content"としておきます。
(この部分がウィンドウのコンテンツになります)

# CSSファイルを用意する
次はCSSファイルです。
(こちらは特に説明することはありませんね)

```CSS:custom.css
/* CSS */

body{
	margin: 0px; padding: 30px;
}

#window-content{
	margin: 0px; padding: 30px;
}
```

# JavaScriptファイルを用意する
最後はJavaScriptです。

WinBoxをインスタンス化する際に、必要最低限のオプションを付けて実行してみます。
次のコードを参考にしてみてくださいね。

```JavaScript:main.js
console.log("main.js!!");

// Windowboxを表示する関数(ボタンをクリックして実行します)
function showWagahai(){

	// Windowbox
	new WinBox({
		title: "吾輩は猫である",// ウィンドウのタイトル
		background: "#3333ff",// ウィンドウの色
		border: "0.3em",// ウィンドウの枠線の太さ
		x: "center",// ウィンドウを中央に(x方向)
		y: "center",// ウィンドウを中央に(y方向)
		width: "50%",// ウィンドウの幅
		height: "50%",// ウィンドウの高さ
		mount: document.getElementById("content").cloneNode(true)// 表示されるコンテンツのidを指定
	});
}
```

他にも様々なオプションが用意されているので、公式サイトを参考にしてみると良いでしょう。
(一目瞭然です!!)

[WinBox](https://nextapps-de.github.io/winbox/)

ここまでの記述だけで、多機能なウィンドウを実装する事ができます。(ボタンをクリックしてくださいね)

![](https://storage.googleapis.com/zenn-user-upload/e582d63f955f-20220116.gif)

とても簡単で多機能なWinBoxを紹介させていただきました。
簡単なアプリケーションを作る際にとても重宝しそうな感じですね。
ここまで読んでいただき有難う御座いました。

