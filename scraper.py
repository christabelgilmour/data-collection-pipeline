import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

url = "https://soundcloud.com/discover/"
driver = webdriver.Safari()
driver.get(url)



def load_and_accept_cookies():
    time.sleep(2)
    accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
    accept_cookies_button.click()
    time.sleep(2)


def get_links_of_Top_50_charts():
    li_tag = driver.find_element(by=By.XPATH, value='//li[@data-test-id="selection"]')
    next_button = li_tag.find_element(by=By.XPATH, value='//button[@class="tileGallery__sliderButton tileGallery__slideForwardButton sc-button sc-button-small sc-button-icon"]')
    # Click the next button until it is disabled
    try: 
        while True:
            next_button.click()
            time.sleep(1)
    except ElementNotInteractableException:
        print("Done")
    genres = li_tag.find_elements(by=By.XPATH, value='.//div[@class="tileGallery__sliderPanelSlide"]')
    all_links = []
    for genre in genres:
        link = genre.find_element(by=By.XPATH, value='.//a[@class="playableTile__artworkLink"]').get_attribute('href')
        all_links.append(link)

    for link in all_links:
          driver.get(link)
          get_data()
          driver.get(url)
    time.sleep(2)

def get_data():
        titles = []
        artists = []
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
            titles.append(song_title)
            artists.append(song_artist)
           
        time.sleep(2)
        print(titles)
        print(artists)
    
driver.get(url)

load_and_accept_cookies()
get_links_of_Top_50_charts()

driver.quit()



