import math
import unittest

def calCircumfrence(r):
    return int(r*2*math.pi)

class TestMyCode(unittest.TestCase):
    def test_circumfrence(self):
        actual = calCircumfrence(5)
        self.assertEqual(actual,31)
    
    def test_circumfrenceZero(self):
        actual = calCircumfrence(0)
        self.assertEqual(actual,0)
    
    def test_circumfrenceInvalid(self):
        self.assertRaises(calCircumfrence("Frank"))

unittest.main()