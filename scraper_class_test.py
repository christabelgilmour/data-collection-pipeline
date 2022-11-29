import unittest
from scraper_class import Scraper
from selenium import webdriver


class ScraperTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.scraper = Scraper()

        
    def test_get_links_top_50(self):
        #This method tests that the url links produced is a list
        self.scraper.load_and_accept_cookies()
        result_links = self.scraper.get_links_top_50()
        self.assertIsInstance(result_links, list)

    def test_get_song_data(self):
        #This method tests that the length of the final dictionary produced is 50
        self.scraper.load_and_accept_cookies()
        all_links = self.scraper.get_links_top_50()
        result = self.scraper.get_song_data(all_links)
        self.assertEqual(len(result), 50)

if __name__ == "__main__":
    unittest.main()





