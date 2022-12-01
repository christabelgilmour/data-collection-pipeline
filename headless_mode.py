import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotInteractableException


class Scraper():
    def __init__(self, url: str = 'https://soundcloud.com/discover'):     
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)
        self.driver.get(url)




    def load_and_accept_cookies(self, xpath: str = '//*[@id="onetrust-accept-btn-handler"]'):
        time.sleep(2)
        accept_cookies_button = self.driver.find_element(By.XPATH, xpath)
        accept_cookies_button.click()
        time.sleep(2)


    def get_links_of_Top_50_charts(self):
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
        self.all_links = []
        genre_titles = []
        for genre in genres:
            genre_title = genre.find_element(By.XPATH, './/a[@class="playableTile__heading playableTile__mainHeading sc-truncate sc-type-light sc-text-secondary sc-font-light sc-link-dark sc-link-primary sc-text-h4"]').text
            link = genre.find_element(By.XPATH, './/a[@class="playableTile__artworkLink"]').get_attribute('href')
            self.all_links.append(link)
            genre_titles.append(genre_title)
            
        genre_dict = {"Genre" : genre_titles , "URL link" : self.all_links}

        df_links = pd.DataFrame(genre_dict)

        print(df_links)
        return self.all_links
        
    
    def get_data(self, all_links):
        for link in all_links:
          self.driver.get(link)
          self.scroll_down_page()
          self.get_top_50()
          self.driver.get('https://soundcloud.com/discover')
        time.sleep(2)

  
    def scroll_down_page(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        self.songs = self.driver.find_elements(By.XPATH, '//li[@class="systemPlaylistTrackList__item sc-border-light-bottom sc-px-2x"]')
    
    def get_top_50(self):
        artists = []
        titles = []
        for song in self.songs:
            song_artist = song.find_element(By.XPATH, './/a[@class="trackItem__username sc-link-light sc-link-secondary sc-mr-0.5x"]').text
            song_title = song.find_element(By.XPATH, './/a[@class="trackItem__trackTitle sc-link-dark sc-link-primary sc-font-light"]').text
            artists.append(song_artist)
            titles.append(song_title)
        time.sleep(2)
        
        song_dict = {"Artist" : artists , "Title" : titles}

        df_songs = pd.DataFrame(song_dict)
        print(df_songs)
    
    def run(self):
        self.load_and_accept_cookies()
        self.get_links_of_Top_50_charts()
        all_links = self.get_links_of_Top_50_charts()
        self.get_data(all_links)


if __name__ == "__main__":
    bot = Scraper()
    bot.run()
