import pyxel
import math
import random

W, H = 160, 120

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # 宇宙船1のテスト
        pyxel.blt(20, 20, 0, 0, 0, 8, 8, 0) # 宇宙船1
        pyxel.blt(20, 28, 0, 0, 8, 8, 8, 0) # ブースター1
        
        # 宇宙船2のテスト
        pyxel.blt(30, 30, 0, 8, 0, 8, 8, 0) # 宇宙船2
        pyxel.blt(30, 38, 0, 8, 8, 8, 8, 0) # ブースター2

        # 隕石のテスト
        pyxel.blt(40, 40, 0, 16, 0, 8, 8, 0) # 隕石1
        pyxel.blt(50, 50, 0, 24, 0, 8, 8, 0) # 隕石2
        pyxel.blt(60, 60, 0, 32, 0, 8, 8, 0) # 隕石3
        pyxel.blt(70, 70, 0, 40, 0, 8, 8, 0) # 隕石4
        pyxel.blt(80, 80, 0, 48, 0, 8, 8, 0) # 隕石5
        pyxel.blt(90, 90, 0, 56, 0, 8, 8, 0) # 隕石5

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()