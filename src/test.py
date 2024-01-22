"""
test.py

Part of the "Unit Converter for Historical Studies" project by OperaVaria.

Unit testing script.
"""

# Built-in module imports:
import unittest
import time
import random
from decimal import Decimal, getcontext

# Import functions for testing:
from functionality.functions import set_act_objs


class Test(unittest.TestCase):
    """Unittests."""
    def test_calculation(self):
        """Test calculation accuracy and rounding."""
        # Values to input.
        value = 1
        input_inter = 0.3048  # Imperial foot
        output_inter = 0.0254  # Imperial inch
        # Extracted copy of the calculation function.
        solution = Decimal(value) * Decimal(input_inter) / Decimal(output_inter)
        getcontext().prec = 10
        solution = solution.normalize()
        # Assertion.
        self.assertEqual(solution, 12)

    def test_obj_setup_speed(self):
        """Test the speed of the active object creation process."""
        # Preparations.
        category_list = ["Hosszúság", "Terület", "Súly",
                         "Darabmérték", "Szárazmérték", "Folyadékmérték"]
        self.act_cat = random.choice(category_list)
        self.sys_name_list = []
        # Function execution and timing.
        start_time = time.time()
        set_act_objs(self)
        end_time = time.time()
        elapsed_time = end_time - start_time
        # Assertion.
        self.assertLess(elapsed_time, 0.01, "Too slow!")


if __name__ == '__main__':
    unittest.main()
