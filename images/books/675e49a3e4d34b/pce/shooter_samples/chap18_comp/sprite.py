# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

TILE_NONE     = 0
TILE_OBSTACLE = 1
TILE_ITEM     = 2

TILE_TYPES = {
    (0, 7): TILE_OBSTACLE, # Grounds
    (1, 7): TILE_OBSTACLE,
    (2, 7): TILE_OBSTACLE,
    (3, 7): TILE_OBSTACLE,
    (4, 7): TILE_OBSTACLE,
    (0, 8): TILE_OBSTACLE,
    (1, 8): TILE_OBSTACLE,
    (2, 8): TILE_OBSTACLE,
    (3, 8): TILE_OBSTACLE,
    (4, 8): TILE_OBSTACLE,
    (4, 2): TILE_OBSTACLE, # Blocks
    (5, 2): TILE_OBSTACLE,
    (2, 2): TILE_OBSTACLE, # Tunnels
    (3, 2): TILE_OBSTACLE,
    (2, 3): TILE_OBSTACLE,
    (3, 3): TILE_OBSTACLE,
    (2, 4): TILE_OBSTACLE,
    (3, 4): TILE_OBSTACLE,
    (0, 2): TILE_ITEM,     # Coin
    (1, 2): TILE_ITEM      # Onigiri
}

class BaseSprite:

    def __init__(self, x, y, u, v, w=8, h=8):
        """ Constructor """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0
        self.hw = w / 2
        self.hh = h / 2

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pass

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def move(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

    def stop(self):
        self.vx = 0
        self.vy = 0

    def intersects(self, other):
        if other.x + other.w < self.x: return False
        if self.x + self.w < other.x: return False
        if other.y + other.h < self.y: return False
        if self.y + self.h < other.y: return False
        return True

    def get_left(self):
        return (self.x, self.y + self.hh)

    def get_right(self):
        return (self.x + self.w, self.y + self.hh)

    def get_top(self):
        return (self.x + self.hw, self.y)

    def get_bottom(self):
        return (self.x + self.hw, self.y + self.h)

    def is_tile_type(self, x, y, type):
        tilemap = pyxel.tilemaps[0]
        u, v = x // 8, y // 8
        tile = tilemap.pget(u, v)
        if not(tile in TILE_TYPES):
            return TILE_NONE, u, v
        return TILE_TYPES[tile] == type, u, v

    def collide_obstacles(self):
        t_obs = TILE_OBSTACLE
        x, y = self.get_bottom()# x Bottom
        flg, u, v = self.is_tile_type(x, y, t_obs)
        if flg:
            self.y = (v-1) * 8
            self.vy = 0
            self.land() # Land
        x, y = self.get_top() # x Top
        flg, u, v = self.is_tile_type(x, y, t_obs)
        if flg:
            self.y = (v+1) * 8
            self.vy = 0
            return
        # x Left
        if self.vx < 0:
            x, y = self.get_left() # Left
            flg, u, v = self.is_tile_type(x, y, t_obs)
            if flg:
                self.x = (u+1) * 8
                self.vx = 0
                return
        # x Right
        if 0 < self.vx:
            x, y = self.get_right() # Right
            flg, u, v = self.is_tile_type(x, y, t_obs)
            if flg:
                self.x = (u-1) * 8
                self.vx = 0
                return

    def collide_items(self):
        tilemap = pyxel.tilemaps[0]
        t_item = TILE_ITEM
        x, y = self.get_bottom()# x Bottom
        flg, u, v = self.is_tile_type(x, y, t_item)
        if flg:
            tilemap.pset(u, v, (0, 0))
            return
        x, y = self.get_top() # x Top
        flg, u, v = self.is_tile_type(x, y, t_item)
        if flg:
            tilemap.pset(u, v, (0, 0))
            return
        x, y = self.get_left() # Left
        flg, u, v = self.is_tile_type(x, y, t_item)
        if flg:
            tilemap.pset(u, v, (0, 0))
            return
        x, y = self.get_right() # Right
        flg, u, v = self.is_tile_type(x, y, t_item)
        if flg:
            tilemap.pset(u, v, (0, 0))
            return
                
class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ Constructor """
        super().__init__(x, y, u, v)
        self.gravity = 0.4 # Gravity
        self.jump_x  = 0.8
        self.jump_y  = -2.4
        self.off_u   = 0
        self.off_v   = 0

    def update(self):
        super().update()
        self.vy += self.gravity # Gravity

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 
            self.u + self.off_u, 
            self.v + self.off_v, 
            self.w, self.h, 0)

    def jump(self):
        self.off_v = 8
        self.vy = self.jump_y

    def runL(self):
        self.off_u = 8
        self.vx = -self.jump_x

    def runR(self):
        self.off_u = 0
        self.vx = self.jump_x

    def stopLR(self):
        self.off_v = 0
        self.vx = 0

    def land(self):
        self.off_v = 0
