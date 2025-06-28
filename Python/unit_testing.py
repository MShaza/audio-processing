import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../build")))
import audio_processing
class TestLowPassFilter(unittest.TestCase):
    def test_basic_case(self):
        data = [1.0, 2.0, 4.0, 5.0, 6.0]
        window = 3
        expected = [1.0, 1.5, 2.3333333333333335, 3.6666666666666665, 5.0]
        result = audio_processing.low_pass_filter(data, window)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places = 5)
    
    def test_sigle_element(self):
        data = [10.0]
        window = 3
        expected = [10.0]
        result = audio_processing.low_pass_filter(data, window)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places = 5)
    def test_empty_input(self):
        data = []
        window = 3
        result = audio_processing.low_pass_filter(data, window)
        self.assertAlmostEqual(result, [])

if __name__ == '__main__':
    unittest.main()