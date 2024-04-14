import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import random
import json
from unidecode import unidecode

# 🌟 Exercise 1 : Parsing HTML With BeautifulSoup
#
# Objective: Use urlopen() to fetch the HTML content of a webpage and then parse it using BeautifulSoup.

url = 'https://www.bocajuniors.com.ar/futbol/noticias-futbol'
response = urlopen(url)

html= response.read()
soup = BeautifulSoup(html, 'html.parser')

type(soup)
print(soup.prettify())
print(soup.title)
print(soup.find_all("p"))


# Find all <a> tags which contain links
links = soup.find_all('a')

# Iterate through the links and print their URLs
for link in links:
    href = link.get('href')
    if href:
        print(href)

# 🌟 Exercise 2 : Scraping Robots.Txt From Wikipedia
#
# Write a Python program to download and display the content of robot.txt for en.wikipedia.org

url = 'https://en.wikipedia.org/wiki/Robots.txt'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)

# 🌟 Exercise 3 : Extracting Headers From Wikipedia’s Main Page
#
# Write a Python program to extract and display all the header tags from en.wikipedia.org/wiki/Main_Page.

url = 'https://en.wikipedia.org/wiki/Main_Page'
request = requests.get(url)

soup = BeautifulSoup(request.text, 'lxml')
# creating a list of all common heading tags
heading_tags = ["h1", "h2", "h3"]
for tags in soup.find_all(heading_tags):
    print(tags.name + '->' + tags.text.strip())

# 🌟 Exercise 4 : Checking For Page Title
#
# Write a Python program to check whether a page contains a title or not.

url = 'https://en.wikipedia.org/wiki/Main_Page'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
# displaying the title
for title in soup.find_all('title'):
    if title == None:
        print('The website does not have a title')
    else:
        print('The title of the website is:', title.get_text())

# 🌟 Exercise 6 : Scraping Movie Details
#
# Write a Python program to get movie name, year and a brief summary of the top 10 random movies.

# Downloading imdb top 250 movie's data
import requests
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/chart/top'

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    source = requests.get(url, headers=headers)
    source.raise_for_status()  # In case the website doesn't exist

    soup = BeautifulSoup(source.text, "html.parser")
    movies = soup.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI "
                                   "compact-list-view ipc-metadata-list--base").find_all('li', class_="ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")

    for index, movie in enumerate(movies[:5], start=1):
        name = movie.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon "
                                        "ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title").a.text

        year = movie.find('div', class_="sc-b189961a-7 feoqjK cli-title-metadata").find("span").text

        rating = movie.find('div', class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container").find("span").text

        print('Ranking and name of the movie: ',name,
              '\nYear when it was released: ', year,
              '\nIMDb rating and number of votes: ', rating,'\n')


except Exception as e:
    print(e)
