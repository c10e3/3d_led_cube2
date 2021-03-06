from led_object import LedObject
from ..led_cube import *
from led_bitmap_obj import LedBitmapObject

START_Y = -16

STATUS_BLINK = 0
STATUS_DROP = 1

class LedDropMushroomObject(LedObject):


    def __init__(self, z, lifetime = 0 ):
        super(LedDropMushroomObject, self).__init__(lifetime)
        self.mushroom = LedBitmapObject('asset/image/mushroom.png', 0, START_Y, z, 1, lifetime)
        self.status = STATUS_BLINK
        self.show = True
        self.set_timer(0.05)
        self.drop_start = 0

    def is_expired(self, offset = 0):
        return self.mushroom.y >= 0

    def on_timer(self):
        self.show = not self.show

    def draw(self, canvas):

        if self.status == STATUS_BLINK and self.elapsed() > 1.0:
            self.status = STATUS_DROP
            self.drop_start = self.elapsed()

        if self.status == STATUS_BLINK:
            if self.show:
                self.mushroom.draw(canvas)

        elif self.status == STATUS_DROP:
            self.mushroom.y = START_Y + (self.elapsed()-self.drop_start) **2  * 150
            self.mushroom.draw(canvas)
        else:
            raise ValueError
