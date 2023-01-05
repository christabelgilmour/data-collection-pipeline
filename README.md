# Data Collection Pipeline

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Milestone 1

After setting up a github repository and choosing the website Soundcloud for my project, I created a Scraper class and used Selenium to create methods to navigate the website and use the relevant XPATH to extract data. The first function is used to accept cookies by finding the relevant button and using `click()`.

<img width="967" alt="Screenshot 2023-01-05 at 15 58 00" src="https://user-images.githubusercontent.com/113252944/210824375-cfb7830a-72b1-4e36-b71f-8afa818f7139.png">

## Milestone 2

Methods are implemented to extract data from Soundcloud. A method to get links of each page of Top 50 charts for the specific genres is used by iterating through the panel slide on the homepage and scraping the links and titles of each genre. 

<img width="986" alt="Screenshot 2023-01-05 at 16 00 13" src="https://user-images.githubusercontent.com/113252944/210824885-36963c9c-3e78-4286-9584-c7c5bb47f5f1.png">

## Milestone 3

I then created a dictionary for this data of genres and url links.

<img width="615" alt="Screenshot 2022-11-15 at 12 06 41" src="https://user-images.githubusercontent.com/113252944/201915954-c23cbe2b-c82e-4655-b813-eb509662d87e.png">

## Milestone 4

A new method is created to iterate through each of these url links and call on two functions to extract the intended data. The first function to scroll down the webpage is implemented to ensure all the relevant song data is extracted from each webpage.

<img width="963" alt="Screenshot 2023-01-05 at 16 01 26" src="https://user-images.githubusercontent.com/113252944/210825251-e6464ba3-1996-4fe7-a4af-4d223e902f22.png">

The second function iterates through all the songs on the webpage and creates dictionaries of the top 50 artist and song titles for each genre are created.

<img width="992" alt="Screenshot 2023-01-05 at 16 05 50" src="https://user-images.githubusercontent.com/113252944/210826012-47fdf974-f62e-420d-bc7d-9c2d6f3d5fe6.png">

Code is written to convert these dictionaries into json files, with the genre of each chart as the filename, and these filea are stored locally in a folder called raw_data.

<img width="845" alt="Screenshot 2023-01-05 at 16 06 19" src="https://user-images.githubusercontent.com/113252944/210826124-e2696dfc-fdff-49af-9001-c66b4cf6a959.png">

## Milestone 5

Once the web scraping tool is built and returns the desired output, the next step is to test all the public methods of the class.
These include the get_song_data(), make_folder() and write_to_json() methods.

<img width="828" alt="Screenshot 2023-01-05 at 16 07 41" src="https://user-images.githubusercontent.com/113252944/210826406-43aef5bf-c5f2-4900-9bf0-7be64800761a.png">

<img width="861" alt="Screenshot 2023-01-05 at 16 08 20" src="https://user-images.githubusercontent.com/113252944/210826560-8faafa67-81ee-456e-a0e9-a5505f478621.png">

## Milestone 6

Using Docker, we can now containerise the scraper by creating a docker image where we choose a base image, install any dependencies and run the python file withing the container. Afterwards, the Dockerfile can be pushed to Docker Hub

<img width="992" alt="Screenshot 2023-01-05 at 16 15 24" src="https://user-images.githubusercontent.com/113252944/210828074-2f49bafd-77c6-426e-bc9b-cecf154c25c2.png">

