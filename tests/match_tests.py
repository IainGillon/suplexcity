import unittest
from models.match import Match
from tests.wrestler_tests import TestWrestler


class TestMatch(unittest.TestCase):

    def setUp(self):
        self.match1 = Match('singles', 'Stone Cold Steve Austin', 'Sting', 'Sting' )
    def test_match_has_type(self):
        self.assertEqual('singles', self.match1.match_type)

    def test_match_has_wrestler1(self):
        self.assertEqual('Stone Cold Steve Austin', self.match1.wreslter1)
    def test_match_has_wrestler2(self):
        self.assertEqual('Sting', self.match1.wrestler2)