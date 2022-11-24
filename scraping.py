import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup



url = "https://soundcloud.com/discover/"
track_url = "https://soundcloud.com/search/sounds?q="
artist_url = "https://soundcloud.com/search/people?q="

driver = webdriver.Safari()
driver.get("https://soundcloud.com/discover")
time.sleep(50000000)

##accept cookies - <button id="onetrust-accept-btn-handler">I Accept</button>

## //*[@id="onetrust-accept-btn-handler"]
<div id="onetrust-button-group"><button id="onetrust-accept-btn-handler">I Accept</button>  <button id="onetrust-pc-btn-handler">Manage Preferences</button></div>