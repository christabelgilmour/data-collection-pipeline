import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

url = "https://soundcloud.com/discover/sets/charts-top:hiphoprap:gb"
driver = webdriver.Safari()
driver.get(url)

def load_and_accept_cookies():
        time.sleep(2)
        accept_cookies_button = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies_button.click()
        time.sleep(2)

def get_data():
        artists = []
        titles = []
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        songs = driver.find_elements(By.XPATH, '//li[@class="systemPlaylistTrackList__item sc-border-light-bottom sc-px-2x"]')
        for song in songs:
            song_artist = song.find_element(By.XPATH, './/a[@class="trackItem__username sc-link-light sc-link-secondary sc-mr-0.5x"]').text
            song_title = song.find_element(By.XPATH, './/a[@class="trackItem__trackTitle sc-link-dark sc-link-primary sc-font-light"]').text
            artists.append(song_artist)
            titles.append(song_title)
        time.sleep(2)
        
        song_dict = {"Artist" : artists , "Title" : titles}

        df_songs = pd.DataFrame(song_dict)
        print(df_songs)

        
    



def Top_50():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    li_tag_50 = driver.find_elements(by=By.XPATH, value='//li[@class="systemPlaylistTrackList__item sc-border-light-bottom sc-px-2x"]')
    artist_links = []
    song_links = []
    for artist in li_tag_50:
        a_link = artist.find_element(by=By.XPATH, value='.//a[@class="trackItem__username sc-link-light sc-link-secondary sc-mr-0.5x"]').get_attribute('href')
        artist_links.append(a_link)
    for song in li_tag_50:
        s_link = song.find_element(by=By.XPATH, value='.//a[@class="trackItem__trackTitle sc-link-dark sc-link-primary sc-font-light"]').get_attribute('href')
        song_links.append(s_link)
    print(artist_links)
    print(song_links)
    
        
    




load_and_accept_cookies()
get_data()