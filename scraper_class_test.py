import unittest
import os
import json
from scraper_class import Scraper
from selenium import webdriver


class ScraperTestCase(unittest.TestCase):
    '''
    Unit tests for the public methods of the webscraping tool
    
    '''
    def setUp(self) -> None:
        self.scraper = Scraper()

    def test_get_song_data(self):
        '''
        This method tests that the length of the final dictionary produced is 50

        '''
        self.scraper._load_and_accept_cookies()
        all_links = self.scraper._get_links_top_50()
        result = self.scraper.get_song_data(all_links)
        self.assertEqual(len(result), 50)

    def test_make_folder(self):
        '''
        This method tests that the folder named raw_data exists after the function make_folder is run

        '''
        folder_path = "/Users/christabelgilmour/Documents/AiCore/Data-Collection-Pipeline/"
        self.scraper.make_folder(folder_path)
        self.assertTrue(os.path.exists(folder_path))

    def test_write_to_json(self):
        '''
        This method tests whether the dictionaries are converted into json files
        
        '''
        test_data = {"BugzyMalone": "Bugzy Malone & TeeDee - Out Of Nowhere",
        "Schak": "Moving All Around (Jumpin') [feat. Kim English]",
        "venbee": "messy in heaven",
        "multunes": "Can I Get Witchaa",
        "Clavish": "Rocket Science (feat. D-Block Europe)"}

        self.scraper.write_to_json(test_data, "test.json")
        with open("raw_data/test.json") as test:
            file = json.load(test)
        
        self.assertEqual(test_data, file)

if __name__ == "__main__":
    unittest.main()










