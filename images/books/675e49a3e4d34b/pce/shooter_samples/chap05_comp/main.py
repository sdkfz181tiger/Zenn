import pyxel
import math
import random

W, H = 160, 120

class BaseSprite:

    def __init__(self, x, y, w=8, h=8):
        """ コンストラクタ """
        self.x = x # x座標
        self.y = y # y座標
        self.w = w # 画像の幅
        self.h = h # 画像の高さ
        self.vx = 0 # 移動速度(x方向)
        self.vy = 0 # 移動速度(y方向)

    def update(self):
        """ 更新処理 """
        self.x += self.vx # x方向に移動
        self.y += self.vy # y方向に移動

    def draw(self):
        """ 描画処理(派生クラスで実装) """
        pass

class ShipSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)

    def draw(self):
        """ 描画処理 """
        pyxel.blt(self.x, self.y, 0, 
            0, 0, 
            self.w, self.h, 0) # Ship

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # プレイヤーを初期化
        self.ship = ShipSprite(W/2, H - 40)

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # プレイヤーを更新
        self.ship.update()

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

        # プレイヤーを描画
        self.ship.draw()

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()