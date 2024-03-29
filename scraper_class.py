import json
import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
class Scraper():
    '''
    A webscraping tool to navigate through Soundcloud and retrieve data. 
    
    Parameters:
    ----------
    url: str
        The website we choose to scrape data from

    '''
    def __init__(self, url: str = 'https://soundcloud.com/discover'):
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(url)

    def _load_and_accept_cookies(self):
        '''
        This method is to accept the cookies button
        '''
        time.sleep(2)
        accept_cookies_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies_button.click()
        time.sleep(2)


    def _get_links_top_50(self):
        '''
        This method gets the urls of the top 50 charts for each genre

        Returns:
        --------
        all_links: list
            List of all the links retrieved
        '''
        li_tag = self.driver.find_element(By.XPATH, '//li[@data-test-id="selection"]')
        next_button = li_tag.find_element(By.XPATH, '//button[@class="tileGallery__sliderButton tileGallery__slideForwardButton sc-button sc-button-small sc-button-icon"]')
        # Click the next button until it is disabled
        try: 
            while True:
                next_button.click()
                time.sleep(1)
        except ElementNotInteractableException:
            print("Done")
        genres = li_tag.find_elements(By.XPATH, './/div[@class="tileGallery__sliderPanelSlide"]')
        all_links = []
        genre_titles = []
        #Iterate over the genres to extract the titles and urls
        for genre in genres:
            genre_title = genre.find_element(By.XPATH, './/a[@class="playableTile__heading playableTile__mainHeading sc-truncate sc-type-light sc-text-secondary sc-font-light sc-link-dark sc-link-primary sc-text-h4"]').text
            link = genre.find_element(By.XPATH, './/a[@class="playableTile__artworkLink"]').get_attribute('href')
            all_links.append(link)
            genre_titles.append(genre_title)
        #Create a dictionary of the genres and their url links
        for i in range(len(genre_titles)):
            genre_dict = {genre_titles[i] : all_links[i]}

        self.make_folder("raw_data")
        self.write_to_json(genre_dict, "genre_dictionary.json")
        return all_links
        
    
    def get_song_data(self, all_links):
        '''
        This method iterates through each link to extract data

        Parameters:
        -----------
        all_links: list
            the url links found in the get_links_top_50

        Returns:
        --------
        list_of_dictionaries: list
            list of the song dictionaries generated from _top_50()
        '''
        list_of_dictionaries = []
        for link in all_links:
          self.driver.get(link)
          time.sleep(2)
          self._scroll_down_page()
          self._top_50()
          list_of_dictionaries.append(self.song_dict)
        time.sleep(2)
        return list_of_dictionaries
      
  
    def _scroll_down_page(self):
        '''
        This method scrolls down the webpage
        
        Returns:
        --------
        songs: list
            List of songs found in each webpage
        '''
        #Scroll down the page to ensure we retrieve all the relevant data
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        self.songs = self.driver.find_elements(By.XPATH, '//li[@class="systemPlaylistTrackList__item sc-border-light-bottom sc-px-2x"]')
    
    def _top_50(self):
        '''
        This method iterates through the songs in each link and creates a dictionary of the top 50 artists and song titles for each genre
        
        Returns:
        --------
        song_dict
            dictionary containing artist names and song titles for each genre
        '''
        self.artists = []
        self.titles = []
        genre = self.driver.find_element(By.XPATH, './/span[@class="fullHero__titleTextTitle"]/span').text
        #Iterate through the songs to extract the data
        for song in self.songs:
            song_artist = song.find_element(By.XPATH, './/a[@class="trackItem__username sc-link-light sc-link-secondary sc-mr-0.5x"]').text
            song_title = song.find_element(By.XPATH, './/a[@class="trackItem__trackTitle sc-link-dark sc-link-primary sc-font-light"]').text
            self.artists.append(song_artist)
            self.titles.append(song_title)
            for i in range(len(self.artists)):
                self.song_dict = {self.artists[i]: self.titles[i]}
    
        self.write_to_json(self.song_dict, f"{genre}.json")
        time.sleep(2)
        
    def make_folder(self, foldername):
        '''
        This method is used to create a folder to store the raw data

        Parameters:
        -----------
        foldername: str
            Name of the folder that is being created 
        '''
        if not os.path.exists(foldername):
            os.makedirs(foldername)

    def write_to_json(self, object_to_dump, filepath):
        '''    
        This method converts the dictionaries to json files and stores them in the raw data folder

        Parameters:
        -----------
        object_to_dump:
            The dictionary to convert into a json file
        filepath: str
            The location of the json file that is dumped
        '''
        with open(f"raw_data/{filepath}", "w") as outfile:
            json.dump(object_to_dump, outfile, indent=4)
    
    def run(self):
        self._load_and_accept_cookies()
        all_links = self._get_links_top_50()
        self.get_song_data(all_links)


if __name__ == "__main__":
    bot = Scraper()
    bot.run()

