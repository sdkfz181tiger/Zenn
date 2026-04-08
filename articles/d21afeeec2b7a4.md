---
title: "Animate.cssでかんたんアニメーション"
emoji: "🔰"
type: "tech"
topics:
  - "javascript"
  - "初心者"
  - "初心者向け"
  - "初学者"
  - "アニメーション"
published: true
published_at: "2022-12-14 18:12"
---

# Animate.cssとは!?
Animate.cssを利用することで、いとも簡単にAnimationを実装する事ができます。

[Animate.css](https://animate.style/)

![](https://storage.googleapis.com/zenn-user-upload/9674c067ad97-20221214.png)

今回はこのライブラリを使ってアニメーションを試してみます。

![](https://storage.googleapis.com/zenn-user-upload/0e86886441d0-20221214.gif)

# プロジェクトを用意する
次の様にプロジェクトを作ります。

MyProject01/
　├ index.html (プログラムを起動するファイルです)
　├ custom.css (CSSを記述するファイルです)
　├ main.js (メインのプログラムを記述するファイルです)

# HTMLファイルを用意する
では、作っていきましょう。
用意したHTMLファイルには次のコードを記述します。

```HTML:index.html
<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="shortcut icon" href="./images/favicon.ico">
	<title>Animate.css</title>
	<!-- CSS -->
	<link rel="stylesheet" href="./custom.css">
	<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
</head>
<body>
	<div id="my_controller">
		<button id="btnA">BtnA</button>
		<button id="btnB">BtnB</button>
		<button id="btnC">BtnC</button>
		<button id="btnD">BtnD</button>
		<button id="btnE">BtnE</button>
	</div>
	<div id="my_container">
		<div id="my_target">Animate.js</div>
	</div>
	<!-- JavaScript -->
	<script src="//code.jquery.com/jquery-3.6.1.min.js"></script>
	<script src="./main.js"></script>
</body>
</html>
```

# CSSファイルを用意する
次はCSSファイルです。

```CSS:custom.css
/* CSS */

html, body{
	width: 100%; height: 100%;
	margin: 0px; padding: 0px;
}

#my_controller{
	position: absolute;
	margin: 10px; padding: 0px;
}

#my_container{
	width: 100%; height: 100%;
	display: flex; flex-flow: wrap;
	justify-content: space-around;
	align-items: center;
}

#my_container div{
	margin: 0px; padding: 10px 30px;
	border-radius: 20px;
	background-color: royalblue; color: white;
	font-size: 2rem;
}
```

# JavaScriptファイルを用意する
いよいよメインの処理です。
JavaScriptファイルには次のコードを記述します。(今回の完成コードです)

```JavaScript:main.js
console.log("main.js!!");

// ボタンイベント
$("#btnA").click(()=>{
	doAnimation("#my_target", "animate__bounce");// Bounce
});

$("#btnB").click(()=>{
	doAnimation("#my_target", "animate__flash");// Flash
});

$("#btnC").click(()=>{
	doAnimation("#my_target", "animate__pulse");// Pulse
});

$("#btnD").click(()=>{
	doAnimation("#my_target", "animate__rubberBand");// RubberBand
});

$("#btnE").click(()=>{
	doAnimation("#my_target", "animate__shakeX");// ShakeX
});

// アニメーション
function doAnimation(id, type){
	const elem = $(id);
	elem.addClass("animate__animated");
	elem.addClass(type);
	elem.on("animationend", ()=>{
		elem.off("animationend");
		elem.removeAttr("class");
	});
}
```

# コードの解説
上記のコードについて、次の順番で解説を進めます。

1. Animate.cssの仕組みについて
2. jQueryを使ってクラスを追加/削除する

## 1, Animate.cssの仕組みについて
Animate.cssを利用する上で必要なファイルは次のファイルです。
CDNを利用し、HTMLファイルに次の様に記述しましょう。

```HTML:index.html(抜粋)
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
```

次に、アニメーション対象のエレメント(タグ)に対して、
2つのクラス"animate__animated"と"animate__bounce"を指定します。
2つめのクラス"animate__bounce"がアニメーションの種類になります。

```HTML:index.html(抜粋)
<div class="animate__animated animate__bounce">Animate.css</div>
```

公式ページの右側にあるアニメーションのメニューから、
様々なアニメーション用のクラスとその動き確認することができます。
使いたいアニメーションのクラス名"animate__xxx"をコピーして使ってみましょう。

![](https://storage.googleapis.com/zenn-user-upload/a4292292522c-20221214.png)

## 1, jQueryを使ってクラスを追加/削除する
jQueryを使って先程のクラスを動的に追加/削除します。
(このあたりはお好みでどうぞ)

```JavaScript:custom.js(抜粋)
// ボタンイベント
$("#btnA").click(()=>{
	doAnimation("#my_target", "animate__bounce");// Bounce
});

// アニメーション
function doAnimation(id, type){
	const elem = $(id);
	elem.addClass("animate__animated");
	elem.addClass(type);
	elem.on("animationend", ()=>{
		elem.off("animationend");
		elem.removeAttr("class");
	});
}
```

簡単にアニメーションを実装することができました。(やりました!!)

![](https://storage.googleapis.com/zenn-user-upload/0e86886441d0-20221214.gif)

# 最後に

CSSを使ったアニメーションの実装は何かと面倒なので、
こういうライブラリがあるととても助かります。
他にも様々な機能が紹介されておりますので、公式サイトを是非ご活用くださいませ。
ここまで読んでいただき有難うございました。