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

        # テキストを描画
        pyxel.text(10, 10, 
            "HELLO, SHAPES!!", 12)
        
        # 線を描画
        # x1, y1, x2, y2, color
        pyxel.line(0, 0, 50, 50, 1)

        # 四角を描画
        # x, y, w, h, color
        pyxel.rect(90, 10, 10, 20, 2)
        pyxel.rectb(120, 30, 30, 20, 3)

        # 円を描画
        # x, y, r, color
        pyxel.circ(60, 80, 10, 4)
        pyxel.circb(90, 50, 10, 5)

        # 楕円を描画
        # x, y, w, h, color
        pyxel.elli(10, 60, 30, 10, 6)
        pyxel.ellib(20, 80, 10, 30, 7)

        # 三角形を描画
        # x1, y1, x2, y2, x3, y3, color
        pyxel.tri(90, 70, 70, 100, 110, 90, 8)
        pyxel.trib(120, 70, 100, 100, 140, 90, 9)


def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()