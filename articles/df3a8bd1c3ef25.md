---
title: "KalidoKitでかんたんLive2Dアバター体験"
emoji: "🔰"
type: "tech"
topics:
  - "javascript"
  - "初心者"
  - "初心者向け"
  - "アバター"
  - "kalidokit"
published: true
published_at: "2022-01-15 12:52"
---

# KalidoKitとは!?
KalidoKitとは、お手軽にアバター体験が出来る大人気ライブラリです。
WebブラウザとWebカメラさえあれば簡単に実行できてしまいます。(お手軽ですね!!)

今回は、サンプルコードを実行するまでの手順をなるべく簡単にしてご紹介いたします。
(細かいことは抜きにして体験する事が大事っ!!)

[KalidoFace](https://kalidoface.com/)

![](https://storage.googleapis.com/zenn-user-upload/5539605e7612-20220115.png)

# GitHubからプロジェクトをダウンロード
GitHubからKalidoKitのソースコード一式をダウンロードします。

[KalidoKit](https://github.com/yeemachine/kalidokit)

![](https://storage.googleapis.com/zenn-user-upload/449970525ab3-20220115.png)

ダウンロードしたプロジェクトフォルダの中にあるLive2D用のモデリングデータをお借りします。
"/docs/models/hiyori"にある"hiyori"フォルダをコピーしておきます。

# プロジェクトを用意する
次の様にプロジェクトを作ります。(先程ダウンロードした"hiyori"フォルダを忘れずに!!)

MyProject01/
　├ custom.css (スタイルシートです)
　├ hiyori (Live2D用のモデリングデータです)
　├ index.html (プログラムを起動するファイルです)
　├ main.js (メインのプログラムを記述するファイルです)

# HTMLファイルを用意する
では、作っていきましょう。
HTMLファイルを用意して、下記コードを記述します。

```HTML:index.html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="custom.css"/>
		<!-- Live2D -->
		<script src="//cubism.live2d.com/sdk-web/cubismcore/live2dcubismcore.min.js"></script>
		<script src="//cdn.jsdelivr.net/gh/dylanNew/live2d/webgl/Live2D/lib/live2d.min.js"></script>
		<!-- PixiJS -->
		<script src="//cdnjs.cloudflare.com/ajax/libs/pixi.js/5.1.3/pixi.min.js"></script>
		<script src="//cdn.jsdelivr.net/npm/pixi-live2d-display/dist/index.min.js"></script>
		<!-- Mediapipe -->
		<script src="//cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh.js"></script>
		<script src="//cdn.jsdelivr.net/npm/@mediapipe/drawing_utils/drawing_utils.js"></script>
		<script src="//cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js"></script>
		<!-- Kalidokit -->
		<script src="//cdn.jsdelivr.net/npm/kalidokit@1.1/dist/kalidokit.umd.js"></script>
	</head>
	<body>
		<!-- Preview -->
		<div id="preview">
			<video id="my-video"></video>
			<canvas id="my-guides"></canvas>
		</div>
		<!-- Live2D -->
		<canvas id="my-live2d"></canvas>
		<script type="module" src="main.js"></script>
	</body>
</html>
```

KalidoKitは、本体ライブラリの他に次の3つのライブラリを利用して実現されています。
(凄いですね!!)

[Cubism SDK](https://docs.live2d.com/cubism-sdk-tutorials/use-sdk-in-js/?locale=ja#)

![](https://storage.googleapis.com/zenn-user-upload/43d7b8832ea2-20220115.png)

[PixiJS](https://pixijs.com/)

![](https://storage.googleapis.com/zenn-user-upload/5722aee488ee-20220115.png)

[MediaPipe](https://google.github.io/mediapipe/)

![](https://storage.googleapis.com/zenn-user-upload/007ad30a0a50-20220115.png)

これらのライブラリ一式は、CDNを使って読み込みをしておきます。

そして、htmlタグにある、id="my-video"の部分にはWebカメラを、
id="my-guides"の部分にはカメラの上に重ねるフェイスメッシュを、
最後に、id="my-live2d"の部分にはLive2Dモデルを表示します。

# CSSファイルを用意する
次はCSSファイルを用意します。(こちらの説明は要りませんね)

```CSS:custom.css

body {
	margin: 0;
}

canvas {
	display: block;
}

video {
	max-width: 320px;
	height: auto;
	transform: scale(-1, 1);
}

#preview {
	display: flex; flex-direction: column;
	position: absolute;
	top: 16px; left: 16px;
	overflow: hidden;
	border-radius: 16px;
}

#preview canvas {
	transform: scale(-1, 1);
}

#my-guides {
	position: absolute;
	top: 0; left: 0;
	width: 100%; height: auto;
	z-index: 1;
}
```

# JavaScriptファイルを用意する
いよいよメインの処理です。
(丸ごとコピーでも動きますよ!!)

主な処理の流れとしては次の様になります。

1. Live2Dモデルへのパスを指定する("hiyori"フォルダへのパスです)
2. PixiJSを準備する
3. Live2Dモデルをロードする
4. Live2Dモデルをドラッグ可能にする
5. Live2Dモデルを拡大/縮小可能に(マウスホイール)
6. Live2Dモデルを配置する
7. フェイスメッシュの読み込みと設定をする
8. Webカメラを開始する
9. フェイスメッシュの描画
10. Live2Dモデルとランドマークを連動させる

```JavaScript:main.js
// PixiJS
const {
	Application,
	live2d: { Live2DModel }
} = PIXI;

// Kalidokit
const {
	Face,
	Vector: { lerp },
	Utils: { clamp }
} = Kalidokit;

// 1, Live2Dモデルへのパスを指定する
const modelUrl = "./hiyori/hiyori_pro_t10.model3.json";
const videoElement = document.getElementById("my-video");
const guideCanvas = document.getElementById("my-guides");

let currentModel, facemesh;

// メインの処理開始
(async function main() {

	// 2, PixiJSを準備する
	const app = new PIXI.Application({
		view: document.getElementById("my-live2d"),
		autoStart: true,
		backgroundAlpha: 0,
		backgroundColor: 0xffffff,
		resizeTo: window
	});

	// 3, Live2Dモデルをロードする
	currentModel = await Live2DModel.from(modelUrl, { autoInteract: false });
	currentModel.scale.set(0.4);
	currentModel.interactive = true;
	currentModel.anchor.set(0.5, 0.5);
	currentModel.position.set(window.innerWidth * 0.5, window.innerHeight * 0.8);

	// 4, Live2Dモデルをドラッグ可能にする
	currentModel.on("pointerdown", e => {
		currentModel.offsetX = e.data.global.x - currentModel.position.x;
		currentModel.offsetY = e.data.global.y - currentModel.position.y;
		currentModel.dragging = true;
	});
	currentModel.on("pointerup", e => {
		currentModel.dragging = false;
	});
	currentModel.on("pointermove", e => {
		if (currentModel.dragging) {
			currentModel.position.set(
				e.data.global.x - currentModel.offsetX,
				e.data.global.y - currentModel.offsetY
			);
		}
	});

	// 5, Live2Dモデルを拡大/縮小可能に(マウスホイール)
	document.querySelector("#my-live2d").addEventListener("wheel", e => {
		e.preventDefault();
		currentModel.scale.set(
			clamp(currentModel.scale.x + event.deltaY * -0.001, -0.5, 10)
		);
	});

	// 6, Live2Dモデルを配置する
	app.stage.addChild(currentModel);

	// 7, フェイスメッシュの読み込みと設定をする
	facemesh = new FaceMesh({
		locateFile: file => {
			return `https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/${file}`;
		}
	});
	facemesh.setOptions({
		maxNumFaces: 1,
		refineLandmarks: true,
		minDetectionConfidence: 0.5,
		minTrackingConfidence: 0.5
	});
	facemesh.onResults(onResults);

	// 8, Webカメラを開始する
	startCamera();
})();

const onResults = results => {
	// 9, フェイスメッシュの描画
	drawResults(results.multiFaceLandmarks[0]);
	// 10, Live2Dモデルとランドマークを連動させる
	animateLive2DModel(results.multiFaceLandmarks[0]);
};

// フェイスメッシュの描画
const drawResults = points => {
	if (!guideCanvas || !videoElement || !points) return;
	guideCanvas.width = videoElement.videoWidth;
	guideCanvas.height = videoElement.videoHeight;
	let canvasCtx = guideCanvas.getContext("2d");
	canvasCtx.save();
	canvasCtx.clearRect(0, 0, guideCanvas.width, guideCanvas.height);
	drawConnectors(canvasCtx, points, FACEMESH_TESSELATION, {
		color: "#C0C0C070",
		lineWidth: 1
	});
	if (points && points.length === 478) {
		drawLandmarks(canvasCtx, [points[468], points[468 + 5]], {
			color: "#ffe603",
			lineWidth: 2
		});
	}
};

// Live2Dモデルとランドマークを連動させる
const animateLive2DModel = points => {
	if(!currentModel || !points) return;
	let riggedFace = Face.solve(points, {
		runtime: "mediapipe",
		video: videoElement
	});
	rigFace(riggedFace, 0.5);
};

const rigFace = (result, lerpAmount = 0.7) => {
	if (!currentModel || !result) return;
	const updateFn = currentModel.internalModel.motionManager.update;
	const coreModel = currentModel.internalModel.coreModel;

	currentModel.internalModel.motionManager.update = (...args) => {
		currentModel.internalModel.eyeBlink = undefined;

		coreModel.setParameterValueById(
			"ParamEyeBallX",
			lerp(
				result.pupil.x,
				coreModel.getParameterValueById("ParamEyeBallX"),
				lerpAmount
			)
		);
		coreModel.setParameterValueById(
			"ParamEyeBallY",
			lerp(
				result.pupil.y,
				coreModel.getParameterValueById("ParamEyeBallY"),
				lerpAmount
			)
		);

		coreModel.setParameterValueById(
			"ParamAngleX",
			lerp(
				result.head.degrees.y,
				coreModel.getParameterValueById("ParamAngleX"),
				lerpAmount
			)
		);
		coreModel.setParameterValueById(
			"ParamAngleY",
			lerp(
				result.head.degrees.x,
				coreModel.getParameterValueById("ParamAngleY"),
				lerpAmount
			)
		);
		coreModel.setParameterValueById(
			"ParamAngleZ",
			lerp(
				result.head.degrees.z,
				coreModel.getParameterValueById("ParamAngleZ"),
				lerpAmount
			)
		);

		const dampener = 0.3;
		coreModel.setParameterValueById(
			"ParamBodyAngleX",
			lerp(
				result.head.degrees.y * dampener,
				coreModel.getParameterValueById("ParamBodyAngleX"),
				lerpAmount
			)
		);
		coreModel.setParameterValueById(
			"ParamBodyAngleY",
			lerp(
				result.head.degrees.x * dampener,
				coreModel.getParameterValueById("ParamBodyAngleY"),
				lerpAmount
			)
		);
		coreModel.setParameterValueById(
			"ParamBodyAngleZ",
			lerp(
				result.head.degrees.z * dampener,
				coreModel.getParameterValueById("ParamBodyAngleZ"),
				lerpAmount
			)
		);

		let stabilizedEyes = Kalidokit.Face.stabilizeBlink(
			{
				l: lerp(
					result.eye.l,
					coreModel.getParameterValueById("ParamEyeLOpen"),
					0.7
				),
				r: lerp(
					result.eye.r,
					coreModel.getParameterValueById("ParamEyeROpen"),
					0.7
				)
			},
			result.head.y
		);

		coreModel.setParameterValueById("ParamEyeLOpen", stabilizedEyes.l);
		coreModel.setParameterValueById("ParamEyeROpen", stabilizedEyes.r);
		coreModel.setParameterValueById(
			"ParamMouthOpenY", 
			lerp(result.mouth.y, coreModel.getParameterValueById("ParamMouthOpenY"), 0.3)
		);
		coreModel.setParameterValueById(
			"ParamMouthForm",
			0.3 + lerp(result.mouth.x, coreModel.getParameterValueById("ParamMouthForm"), 0.3)
		);
	};
};

// Webカメラ
const startCamera = ()=>{
	const camera = new Camera(videoElement, {
		onFrame: async ()=>{
			await facemesh.send({ image: videoElement });
		},
		width: 640, height: 480
	});
	camera.start();
};
```

これだけでLive2Dアバターが完成してしまいます。(Webカメラ部分は非表示にしてあります!!)

![](https://storage.googleapis.com/zenn-user-upload/bcd382f86a39-20220115.png)

今回は、KalidoKitを使ってサンプルを動作させるまでの手順を駆け足でご紹介致しました。
Webブラウザで気軽に動かせるのはとても使い勝手が良さそうですね。
ここまで読んでいただき有難う御座いました。