import unittest
from scraper_class import Scraper
from selenium import webdriver

class ScraperTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.scraper = Scraper()
    
    # def test_get_links_top_50(self):
    #     links = self.scraper.get_links_top_50()
    #     self.assertIsInstance(links, list)

    def test_get_song_data(self, all_links):
        result = self.scraper.get_song_data(self, all_links)
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()





