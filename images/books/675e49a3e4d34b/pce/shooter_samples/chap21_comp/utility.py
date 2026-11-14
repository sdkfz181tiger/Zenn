import pyxel
import pytweening as tween
import math

#==========
# BaseSpriteクラス
class BaseSprite:

    def __init__(self, x, y, u=0, v=0, w=8, h=8):
        """ コンストラクタ """
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

        # Animation
        self.anim_flg = False
        self.anim_index = 0
        self.anim_key = ""
        self.anims = {}

        # Tween
        self.t_frame = -1
        self.t_points = []

    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.animate() # Animation
        self.tween() # Tween


    def draw(self):
        pyxel.blt(self.x, self.y, 0,
            self.u, self.v, self.w, self.h, 0)


    def move(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度


    def stop(self):
        self.vx = 0
        self.vy = 0
        if -1 < self.t_frame:
            self.t_frame = -1


    def get_left(self):
        return (self.x, self.y + self.hh)


    def get_right(self):
        return (self.x + self.w, self.y + self.hh)


    def get_top(self):
        return (self.x + self.hw, self.y)


    def get_bottom(self):
        return (self.x + self.hw, self.y + self.h)


    #==========
    # Collision
    def get_min_x(self):
        return self.x


    def get_min_y(self):
        return self.y


    def get_max_x(self):
        return self.x + self.w


    def get_max_y(self):
        return self.y + self.h


    def collide(self, other):
        if other.get_max_x() < self.get_min_x():
            return False
        if other.get_max_y() < self.get_min_y():
            return False
        if self.get_max_x() < other.get_min_x():
            return False
        if self.get_max_y() < other.get_min_y():
            return False
        return True


    def is_inside(self, x, y):
            if x < self.get_min_x():
                return False
            if y < self.get_min_y():
                return False
            if self.get_max_x() < x:
                return False
            if self.get_max_y() < y:
                return False
            return True


    #==========
    # Animation
    def animate(self):
        if not self.anim_flg:
            return
        anims = self.anims[self.anim_key]
        frame = anims[self.anim_index]
        if frame is None:
            self.anim_flg = False
            self.anim_index = 0
            frame = anims[self.anim_index]
            return
        self.u = frame[0]
        self.v = frame[1]
        if pyxel.frame_count % 3 == 0:
            self.anim_index += 1
        if len(anims) <= self.anim_index:
            self.anim_index = 0


    def set_animation(self, key, animations):
        self.anims[key] = animations


    def start_animation(self, key):
        if not key in self.anims:
            return
        self.anim_flg = True
        self.anim_index = 0
        self.anim_key = key


    def stop_animation(self):
        self.anim_flg = False


    def toggle_animation(self):
        self.anim_flg = not self.anim_flg


    #==========
    # Tween
    def tween(self):
        if self.t_frame < 0:
            return
        if len(self.t_points) -1 <= self.t_frame:
            self.t_frame = -1
            return
        self.t_frame += 1
        self.x, self.y = self.t_points[self.t_frame]


    def move_to(self, x, y, sec, func):
        t_interval_size = 1 / (30 * sec)
        self.t_frame = 0
        self.t_points = list(func(
                    self.x, self.y, x, y, 
                    t_interval_size))


    def is_tweening(self):
        return 0 <= self.t_frame


    def get_left(self):
        return (self.x, self.y + self.hh)


    def get_right(self):
        return (self.x + self.w, self.y + self.hh)


    def get_top(self):
        return (self.x + self.hw, self.y)


    def get_bottom(self):
        return (self.x + self.hw, self.y + self.h)


#==========
# Camera
class CameraManager:

    def __init__(self, area_w, area_h, pad_x=16, pad_y=16):
        """ コンストラクタ """
        self.camera_x = 0
        self.camera_y = 0
        self.area_w = area_w
        self.area_h = area_h
        self.pad_x = pad_x
        self.pad_y = pad_y
        self.limit_l = pyxel.width - area_w
        self.limit_r = 0
        self.limit_t = pyxel.height - area_h
        self.limit_b = 0


    def set_center(self, spr):
        x = spr.x
        y = spr.y
        w = min(pyxel.width, self.area_w)
        h = min(pyxel.height, self.area_h)
        self.camera_x = w / 2 - x
        self.camera_y = h / 2 - y
        pyxel.camera(-self.camera_x, -self.camera_y)


    def camera_on(self, spr):
        x = spr.x
        y = spr.y
    
        line_l = 0 - self.camera_x + self.pad_x
        if x < line_l:
            self.camera_x += line_l - x
            if self.limit_r < self.camera_x:
                self.camera_x = self.limit_r

        line_r = pyxel.width - self.camera_x - self.pad_x
        if line_r < x:
            self.camera_x += line_r - x
            if self.camera_x < self.limit_l:
                self.camera_x = self.limit_l

        line_t = 0 - self.camera_y + self.pad_y
        if y < line_t:
            self.camera_y += line_t - y
            if self.limit_b < self.camera_y:
                self.camera_y = self.limit_b

        line_b = pyxel.height - self.camera_y - self.pad_y
        if line_b < y:
            self.camera_y += line_b - y
            if self.camera_y < self.limit_t:
                self.camera_y = self.limit_t

        pyxel.camera(-self.camera_x, -self.camera_y)
    
    
    def camera_off(self):
        pyxel.camera()
    

#==========
# Tilemap

def is_tile_type(x, y, type, types):
    tilemap = pyxel.tilemaps[0]
    u, v = x // 8, y // 8
    tile = tilemap.pget(u, v)
    if not(tile in types):
        return None, u, v
    return types[tile] == type, u, v


def collide_tile(spr, t_type, t_types, replace=None):
    tilemap = pyxel.tilemaps[0]
    x, y = spr.get_bottom()# x Bottom
    flg, u, v = is_tile_type(x, y, t_type, t_types)
    if flg and 0 < spr.vy:
        if replace:
            tilemap.pset(u, v, replace)
        else:
            spr.y = (v-1) * 8
            spr.vy = 0
        return True
    x, y = spr.get_top() # x Top
    flg, u, v = is_tile_type(x, y, t_type, t_types)
    if flg and spr.vy < 0:
        if replace:
            tilemap.pset(u, v, replace)
        else:
            spr.y = (v+1) * 8
            spr.vy = 0
        return True
    x, y = spr.get_left() # x Left
    flg, u, v = is_tile_type(x, y, t_type, t_types)
    if flg and spr.vx < 0:
        if replace:
            tilemap.pset(u, v, replace)
        else:
            spr.x = (u+1) * 8
            spr.vx = 0
        return True
    x, y = spr.get_right() # x Right
    flg, u, v = is_tile_type(x, y, t_type, t_types)
    if flg and 0 < spr.vx:
        if replace:
            tilemap.pset(u, v, replace)
        else:
            spr.x = (u-1) * 8
            spr.vx = 0
        return True
    return False

#==========
# Tile

class Tile(BaseSprite):

    def __init__(self, x, y, type, r, c):
        """ Constructor """
        self.type = type
        u, v = type
        self.r, self.c = r, c
        super().__init__(x, y, u, v, 8, 8)


    def get_type(self):
        return self.type

    
    def get_rc(self):
        return self.r, self.c


    def set_off(self):
        self.u = 0
        self.v = 0


    def is_off(self):
        return self.u == 0 and self.v == 0

