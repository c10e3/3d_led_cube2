from led_canvs_filter import LedCanvasFilter
from ..led_cube import *
from ..util.cube_util import *
from ..util.hw_controller_util import get_data_as_json
import time

class LedRollingCtrlCanvasFilter(LedCanvasFilter):

    def __init__(self, canvas):
        super(LedRollingCtrlCanvasFilter, self).__init__(canvas)
        self.offset = 0
        self.last_update = time.time()

    def pre_draw(self):
        super(LedRollingCtrlCanvasFilter, self).pre_draw()
        param = get_data_as_json(defaults={'a0':0.5, 'a1':0.5})
        direction = (param['a0'] - 0.5) * 2
        speed = param['a1'] * 200

        now = time.time()
        add = now - self.last_update
        self.last_update = now
        self.offset += add * direction * speed
        
    def set_led(self, x, y, z, color):
        if not is_in_cube(x, y, z):
            return
        new_y = (y + self.offset) % LED_HEIGHT

        self.canvas.set_led(x, new_y, z, color)
