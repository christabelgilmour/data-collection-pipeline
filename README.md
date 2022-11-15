# Data Collection Pipeline

## Milestone 1

After setting up a github repository and choosing the website Soundcloud for my project, I created a Scraper class and used Selenium to create methods to navigate the website and use the relevant XPATH to extract data. The first function is used to accept cookies by finding the relevant button and using `click()`.

<img width="694" alt="Screenshot 2022-10-31 at 11 29 50" src="https://user-images.githubusercontent.com/113252944/198998014-f0ef9987-e983-4102-b3ec-cc738ef5ec8a.png">

## Milestone 2

Methods are implemented to extract data from Soundcloud. A method to get links of each page of Top 50 charts for the specific genres is used by iterating through the panel slide on the homepage and scraping the links and titles of each genre. 

<img width="1054" alt="Screenshot 2022-11-15 at 12 22 45" src="https://user-images.githubusercontent.com/113252944/201918807-6966e6a4-35ed-4469-9397-dc8d80172c06.png">

## Milestone 3

I then created a dictionary for this data of genres and url links.

<img width="615" alt="Screenshot 2022-11-15 at 12 06 41" src="https://user-images.githubusercontent.com/113252944/201915954-c23cbe2b-c82e-4655-b813-eb509662d87e.png">

## Milestone 4

A new method is created to iterate through each of these url links and call on two functions to extract the intended data. The first function to scroll down the webpage is implemented to ensure all the relevant song data is extracted from each webpage.

<img width="943" alt="Screenshot 2022-11-15 at 12 26 10" src="https://user-images.githubusercontent.com/113252944/201919403-4d7cd037-84aa-41af-ba89-a1907483f49b.png">

The second function iterates through all the songs on the webpage and dictionaries of the top 50 artist and song titles for each genre are created.

<img width="966" alt="Screenshot 2022-11-15 at 12 15 13" src="https://user-images.githubusercontent.com/113252944/201917502-26251694-55e7-4d63-9cb3-1f0a4cc8c8b0.png">

Code is written to convert these dictionaries into json files and store them locally in a folder called raw_data.

<img width="522" alt="Screenshot 2022-11-15 at 12 33 59" src="https://user-images.githubusercontent.com/113252944/201920804-e8cd2363-c37c-454b-ba7c-b2005c147463.png">

