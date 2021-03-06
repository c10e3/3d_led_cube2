import unittest
import block_dictionary as bd
from libled.util.led_order_util import *

class TestBlockDictionary(unittest.TestCase):

    def test_order_in_order_all_is_exist_in_led_order_util(self):
        for order in bd.order_all:
            for _, color in order.iteritems():
                for _, size in color.iteritems():
                    target = create_order({'id': str(size)}, None)
                    self.assertIsNotNone(target)

    def test_all_black_size_is_exist_in_order_all(self):
        for order in bd.order_all:
            for _, color in order.iteritems():
                result = {
                    '2':0,
                    '3':0,
                    '4':0,
                }
                for size, _ in color.iteritems():
                    result[str(size)]+= 1

                # check
                for _, count in result.iteritems():
                    self.assertEqual(1, count)

 
    def test_all_color_is_exist_in_order_all(self):
        for order in bd.order_all:
            result = {
                'red':0,
                'blue':0,
                'yellow':0,
                'yellowgreen':0,
                'brown':0,
                'white':0,
                'orange':0,
                'green':0,
            }
            for color, _ in order.iteritems():
                result[color]+= 1

            # check
            for _, count in result.iteritems():
                self.assertEqual(1, count)


            
