import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
        
    def testi1(self):
        player = self.stats.search("Kurri")
        
        self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")
        
    def testi2(self):
        team = self.stats.team("EDM")
        
        self.assertEqual(len(team), 3)
        
    def testi3(self):
        top2 = self.stats.top(2)
        
        self.assertEqual(top2[0].name, "Gretzky")
        self.assertEqual(top2[1].name, "Lemieux")
        
    def testi4(self):
        nimeton = self.stats.search("Kukkuu")
        
        self.assertEqual(nimeton, None)