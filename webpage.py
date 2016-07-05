"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
"""
import requests
from bs4 import BeautifulSoup

# the URL of the NY Times website we want to parse
base_url = 'http://www.nytimes.com'

# http://docs.python-requests.org/en/master/
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

# Use Chrome inspect to find out which HTML tags contain all the titles 
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
for story_heading in soup.find_all(class_="story-heading"):   # this is class_ not class
    # if story_heading.contents is a tag
    if story_heading.a: 
        # print a tag's text strip white space and '\n'
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        # try to print story_heading.contents first to understand
        print(story_heading.contents[0].strip())
view raw

