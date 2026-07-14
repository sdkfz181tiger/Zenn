"""
Pyxelリファレンス
https://kitao.github.io/pyxel/web/api-reference/
"""

import pyxel
import math
import random

W, H = 160, 120

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!", fps=16)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # スコアを描画
        pyxel.text(10, 10, 
            "HELLO, PYXEL!!", 12)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()