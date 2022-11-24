import requests
from bs4 import BeautifulSoup
response = requests.get("https://soundcloud.com/discover")
html = print(response.content)
html = BeautifulSoup(html, 'html.parser')
print(html.prettify)

