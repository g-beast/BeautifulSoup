import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import re

#  Set the URL of the website you want to scrape.
url = "https://sflix.to/home"

# Get the HTML of the website.
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# Get the whole HTML of the home page
html = soup.prettify()
# THE WHOLE SFLIX PAGE
# print(html)

# Find the movies on the website.
movies = soup.find_all("div", {"class": "film-poster"})
# print(movies)

# Print out the movies.
poster_elements = soup.find_all("img", {"class": "film-poster-img"})
# movie_name = soup.find("img", {"class": "film-poster-img"})["src"] #to find the title of the first movie in the website
movie_titles = []
unique_fix = "Title :"
for i in range(len(poster_elements)):
    poster_element = poster_elements[i]
    movie_title = poster_element["title"]
    movie_titles.append(movie_title)

# print("Movie Title : ", movie_titles)

# Print out the movie posters.
poster_elements = soup.find_all("img", {"class": "film-poster-img"})
poster_links = []
for poster_element in poster_elements:
    if "src" in poster_element.attrs:
        poster_link = poster_element["src"]
        poster_links.append(poster_link)


#print(poster_links)

# class of the slider movies
a_slide_elements = soup.find_all("a", {"class": "slide-mask"})
# class of the body movies
a_elements = soup.find_all("a", {"class": "btn btn-sm btn-play btn-secondary"})

# Print out the movie title.
poster_elements = soup.find_all("img", {"class": "film-poster-img"})

# slide_href_links = []
# href_links = []
strT0list = []

url_fix = "https://sflix.to"
slide_fix = "InSlide"

number_of_strings = 0

# to get the movies in the slider element
for a_slide_element in a_slide_elements:
    if "href" in a_slide_element.attrs:
        slide_href_link = a_slide_element["href"]
        movie_title = poster_element["title"]
        if isinstance(slide_href_link, str):
            number_of_strings += 1
            slide_href_links = f"{url_fix}{slide_href_link}"
            # slide_href_links = f"{number_of_strings}??{url_fix}{slide_href_link}"
            strT0list.append(slide_href_links)

# print(strT0list)

for a_element in a_elements:
    if "href" in a_element.attrs:
        href_link = a_element["href"]
        movie_title = poster_element["title"]
        if isinstance(href_link, str):
            number_of_strings += 1
            href_links = f"{url_fix}{href_link}"
            # href_links = f"{number_of_strings}??{url_fix}{href_link}"
            strT0list.append(href_links)

# print(strT0list)

# calling function
# moviesLinks(strT0list)

def moviesLinks(new_urls):
    number_of_strings = 0
    new_url_fix = "https://sflix.to"
    for new_url in new_urls:
        new_response = requests.get(new_url)
        new_soup = BeautifulSoup(new_response.content, "html.parser")
        secondary_repos = new_soup.find_all("a", {"class": "film-poster-ahref"})
        # Print out the movie title.
        poster_elements = soup.find_all("img", {"class": "film-poster-img"})
        movie_title = poster_element["title"]
        for secondary_repo in secondary_repos:
            if "href" in secondary_repo.attrs:
                new_href_link = secondary_repo["href"]

        if isinstance(new_href_link, str):
            number_of_strings += 1
            new_href_link = f"{new_url_fix}{new_href_link}"
            strT0list_numb = len(strT0list)
            fully = f"{strT0list_numb}:{new_href_link}"
            strT0list.append(new_href_link)
        print(fully)
        # print(strT0list_numb)
        if strT0list_numb == 6000:
            print(strT0list)
            break


moviesLinks(strT0list)


def list_to_string(list_of_characters):
    number_of_links = 0
    seen = set()
    new_characters_list = []
    for character in list_of_characters:
        if character not in seen:
            new_characters_list.append(character)
            seen.add(character)
    for new_link in new_characters_list:
        number_of_links += 1
        fully = f"{number_of_links}:{new_link}"
        print(fully)


list_to_string(strT0list)

def write_to_notepad(list_of_strings):
    with open("sflix_movie_links.txt", "w") as f:
        for string in list_of_strings:
            f.write(string + "\n")

write_to_notepad(strT0list)


def remove_duplicate_strings(file_name):
    seen = set()
    new_list = []

    with open(file_name, "r") as f:
        text = f.read()

    links = re.findall(r"https?://\S+", text)

    for link in links:
        if link not in seen:
            new_list.append(link)
            seen.add(link)

    with open("filtered_movie_links.txt", "w") as f:
        for new_links in new_list:
            f.write(new_links + "\n")


remove_duplicate_strings("sflix_movie_links.txt")


