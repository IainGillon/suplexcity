import unittest
from models.wrestler import Wrestler

class TestWrestler(unittest.TestCase):

    def setUp(self):
        self.wrestler1 = Wrestler("Stone Cold Steve Austin", 3)
        self.wrestler2 = Wrestler("Sting", 3)

    def test_wrestler_has_name(self):
        self.assertEqual("Stone Cold Steve Austin", self.wrestler1.name)

    def test_wrestler_has_points(self):
        self.assertEqual(3, self.wrestler2.points)

