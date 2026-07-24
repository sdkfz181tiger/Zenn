import pyxel # Pyxelゲームエンジン
import math # 数学用モジュール
import random # 乱数用モジュール

W, H = 160, 120 # ゲーム画面の幅、高さ

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()