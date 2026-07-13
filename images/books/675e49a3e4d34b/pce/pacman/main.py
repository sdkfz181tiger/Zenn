import pyxel
import math
import random
import sprite

W, H = 160, 120

MODE_GAME_READY = "mode_game_ready"
MODE_GAME_PLAY = "mode_game_play"
MODE_GAME_OVER = "mode_game_over"

TOTAL_DOTS = 12
SCORE_DOT = 10
SCORE_IJIKE = 40

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # Player
        self.player = sprite.PlayerSprite(
            0, 0, 0, 8, 1.8)

        # Enemy
        self.enemy = sprite.EnemySprite(
            0, 0, 0, 40, 0.8, self.player)

        # Dots
        self.dots = []
        # ステップ2: ドットを配置
        pad_x = W / TOTAL_DOTS
        for i in range(TOTAL_DOTS):
            x = i * pad_x + pad_x / 2
            self.create_dot(x, H/2, i==0)

        # Ready
        self.game_ready()

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw) # Pyxel実行

    def update(self):
        """ 更新処理 """

        self.control() # Control
        if self.mode != MODE_GAME_PLAY: return

        # Player
        self.player.update()
        self.overlap_area(self.player) # Overlap

        # Enemy
        self.enemy.update()
        self.overlap_area(self.enemy) # Overlap

        # Dots
        for dot in self.dots:
            dot.update()
            # Contains and Sleep
            if dot.is_sleep(): continue
            if self.player.contains_center(dot):
                self.score += SCORE_DOT # Score
                dot.sleep()
                if dot.is_power():
                    self.enemy.ijike_on() # Ijike(On)

        # Awake all dots
        if self.is_sleep_dots():
            self.awake_dots()
            self.level_up() # Level Up!!

        # Collision
        if self.player.contains_center(self.enemy):
            if self.enemy.is_ijike():
                self.score += SCORE_IJIKE # Score
                self.enemy.set_center(0, H/2) # Reset
                self.enemy.ijike_off() # Ijike(Off)
            else:
                # ステップ4: ゲームオーバー判定
                self.game_over() # Game Over
            
    def draw(self):
        """ 描画処理 """
        pyxel.cls(1)

        # Road
        pyxel.rect(0, H/2-8, W, 16, 0)
        pyxel.rect(0, H/2-9, W, 1, 5)
        pyxel.rect(0, H/2+8, W, 1, 5)

        # Dots
        for dot in self.dots:
            dot.draw()
        # Player
        self.player.draw()
        # ステップ3: 敵を描画
        # Enemy
        self.enemy.draw()
        # Stats
        self.draw_stats()

    def create_dot(self, x, y, power_flg):
        dot = sprite.DotSprite(0, 0, 0, 16, power_flg)
        dot.set_center(x, y)
        self.dots.append(dot)

    def overlap_area(self, spr):
        # ステップ1: オーバーラップ処理
        if spr.x < 0: spr.x = W
        if W < spr.x: spr.x = 0

    def draw_stats(self):
        # Level
        str_level = "LV:{}".format(self.level)
        x = W - (len(str_level) * 4) - 10
        pyxel.text(x, 10, str_level, 7)
        # Score
        str_score = "SCORE:{:03}".format(self.score)
        x = 10
        pyxel.text(x, 10, str_score, 7)
        # Message
        str_msg = "{}".format(self.msg)
        x = W / 2 - (len(str_msg) * 4) / 2
        pyxel.text(x, H/2 - 24, str_msg, 7)

    def control(self):
        """ コントロール """
        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): return

        # Ready to Play
        if self.mode == MODE_GAME_READY:
            self.game_play() # Play
            return

        # Play
        if self.mode == MODE_GAME_PLAY:
            self.player.turn() # Turn
            return

        # Over to Ready
        if self.mode == MODE_GAME_OVER:
            self.game_ready() # Ready
            return

    def game_ready(self):
        self.mode = MODE_GAME_READY
        self.msg = "GAME READY!?"
        self.level = 1 # Level
        self.score = 0 # Score
        self.player.set_center(W/2, H/2) # Player
        self.enemy.set_center(0, H/2) # Enemy
        self.awake_dots() # Awake

    def game_play(self):
        self.mode = MODE_GAME_PLAY
        self.msg = "GAME PLAY!!"
        self.player.go_random() # Player
        self.enemy.go_random() # Enemy

    def game_over(self):
        self.mode = MODE_GAME_OVER
        self.msg = "GAME OVER!!"
        self.player.stop() # Player
        self.enemy.stop() # Enemy

    def is_sleep_dots(self):
        if not self.dots: return False
        for dot in self.dots:
            if not dot.is_sleep(): return False
        return True

    def awake_dots(self):
        # Awake
        for dot in self.dots:
            dot.awake()
        # Swap
        if 0 < len(self.dots):
            other = random.choice(self.dots)
            self.dots[0].swap_position(other)

    def level_up(self):
        self.level += 1 # Level Up!!
        self.enemy.speed_up(0.14) # Speed Up!!

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()