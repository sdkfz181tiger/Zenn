import pyxel
import pytweening as tween
import random
import utility

ROWS = 8
COLS = 12
TILE_A = (0, 8)
TILE_B = (8, 8)
TILE_C = (16, 8)
TILE_D = (24, 8)
TILE_TYPES = [
    TILE_A, TILE_B, TILE_C, TILE_D
]

# Gameクラス
class Game:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        self.w = pyxel.width
        self.h = pyxel.height

        # Tiles
        self.tiles = []
        s_x, s_y, pad = 7, 10, 9
        for r in range(ROWS):
            for c in range(COLS):
                x = s_x + c * pad
                y = s_y + r * pad
                type = random.choice(TILE_TYPES)
                tile = utility.Tile(x, y, type, r, c)
                self.tiles.append(tile)
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        # Update
        for tile in self.tiles:
            tile.update()

        # Click
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            for tile in self.tiles:
                if tile.is_tweening():
                    return
            m_x = pyxel.mouse_x
            m_y = pyxel.mouse_y
            for tile in self.tiles:
                if tile.is_inside(m_x, m_y):
                    type = tile.get_type()
                    print(f"r:{tile.r}, c:{tile.c}, type:{type}")
                    chains = self.count_chains(tile.r, tile.c, type, [])
                    count = len(chains)
                    if count < 2:
                       return
                    print(f"count:{count}")
                    # Set off
                    for r, c in chains:
                        print(f"chain: {r}, {c}")
                        tile = self.tiles[r * COLS + c]
                        tile.set_off() # Off
                    # Brow
                    self.brow()


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # Tiles
        for tile in self.tiles:
            tile.draw()

        # マウス座標
        m_x = pyxel.mouse_x
        m_y = pyxel.mouse_y
        pyxel.circ(m_x, m_y, 1, 7)


    def count_chains(self, r, c, type, chains):
        #print(f"count_chains: {r}, {c}, type{type}")
        if r < 0: return chains
        if c < 0: return chains
        if ROWS - 1 < r: return chains
        if COLS - 1 < c: return chains
        if (r, c) in chains:
            return chains
        tile = self.tiles[r * COLS + c]
        if tile.is_off():
            return chains
        if tile.type != type:
            return chains
        chains.append((r, c))
        self.count_chains(r-1, c, type, chains)
        self.count_chains(r+1, c, type, chains)
        self.count_chains(r, c-1, type, chains)
        self.count_chains(r, c+1, type, chains)
        return chains


    def brow(self):
        #print(f"brow")
        for c in range(COLS):
            for r in range(ROWS-1, 0, -1):
                tile = self.tiles[r * COLS + c]
                if not tile.is_off():
                    continue
                self.brow_r(r, c)


    def brow_r(self, r, c):
        #print(f"Let's blow_r: {r}, {c}")
        to_t = r * COLS + c
        to_tile = self.tiles[to_t]
        for t in range(r, -1, -1):
            from_t = t * COLS + c
            from_tile = self.tiles[from_t]
            if self.tiles[from_t].is_off():
                continue
            # Swap
            from_tile.move_to(to_tile.x, to_tile.y, 0.4, tween.iterEaseInQuart)
            to_tile.x, to_tile.y = from_tile.x, from_tile.y
            from_tile.r, to_tile.r = to_tile.r, from_tile.r
            from_tile.c, to_tile.c = to_tile.c, from_tile.c
            self.tiles[from_t], self.tiles[to_t] = self.tiles[to_t], self.tiles[from_t]
            return


# Gameクラスを初期化
Game()

