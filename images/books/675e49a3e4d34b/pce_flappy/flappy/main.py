import pyxel
import math
import random
import sprite

W, H = 160, 120

START_X = W / 2 - 48
START_Y = H / 2 - 12

MODE_TITLE = "title"
MODE_PLAY = "play"
MODE_GAME_OVER = "game_over"

TUNNEL_TOTAL = 48

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # ゲームモード
        self.game_mode = MODE_TITLE

        # プレイヤーを初期化
        self.player = sprite.PlayerSprite(START_X, START_Y)

        # ステージを初期化
        self.reset()

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # スコアを更新
        self.score = int(self.player.x - START_X)

        # コントロール
        self.control()

        # プレイ中判定
        if self.game_mode != MODE_PLAY: return

        # プレイヤーを更新
        self.player.update()

        # トンネルを更新
        for tunnel in self.tunnels:
            tunnel.update()
            if(tunnel.intersects(self.player)):
                self.game_mode = MODE_GAME_OVER
                break

        # 落下判定
        if H < self.player.y: 
            self.game_mode = MODE_GAME_OVER

    def draw(self):
        """ 描画処理 """
        pyxel.cls(6)

        # タイルマップ
        pyxel.bltm(0, 0, 0, 0, 0, 192, 128, 0)

        # カメラ(セット)
        pyxel.camera(self.player.x - START_X, 0)

        # プレイヤーを描画
        self.player.draw()

        # トンネルを描画
        for tunnel in self.tunnels:
            tunnel.draw()

        pyxel.camera() # カメラ(リセット)

        # メッセージ
        if self.game_mode == MODE_TITLE:
            msg = "SPACE TO PLAY"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 1)
        elif self.game_mode == MODE_GAME_OVER:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 1)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 1)

    def reset(self):
        """ ステージを初期化 """

        # プレイヤー
        self.player.x = START_X
        self.player.y = START_Y

        # トンネル
        self.tunnels = []
        for i in range(TUNNEL_TOTAL):
            pad_x = 42
            pad_y = random.randint(2, 3) * 8
            x = START_X + pad_x * i + 32
            y = H / 2 + random.randint(-2, 2) * 8
            t_top = sprite.TunnelSprite(x, y-pad_y, 10, True)
            self.tunnels.append(t_top)
            t_bottom = sprite.TunnelSprite(x, y+pad_y, 10)
            self.tunnels.append(t_bottom)

    def control(self):
        """ コントロール """
        if not pyxel.btnp(pyxel.KEY_SPACE): return

        # Title -> Play
        if self.game_mode == MODE_TITLE:
            self.game_mode = MODE_PLAY

        # Game Over -> Title
        if self.game_mode == MODE_GAME_OVER:
            self.game_mode = MODE_TITLE
            # Reset
            self.reset()

        # ジャンプ
        if self.game_mode == MODE_PLAY:
            self.player.jump()

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()