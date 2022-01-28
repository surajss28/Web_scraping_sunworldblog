from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pandas as pd

url_page1 = 'https://sunworldblog.herokuapp.com/'
url_page2 = 'https://sunworldblog.herokuapp.com/?page=2'
url_page3 = 'https://sunworldblog.herokuapp.com/?page=3'

html_1 = urlopen(url_page1)
html_2 = urlopen(url_page2)
html_3 = urlopen(url_page3)

soup_1 = BeautifulSoup(html_1, features="html.parser")
soup_2 = BeautifulSoup(html_2, features="html.parser")
soup_3 = BeautifulSoup(html_3, features="html.parser")

posts_title = []
posts_author = []
posts_category = []


# getting data from first page 

posts = soup_1.find_all('div', class_='excerpt')
for post in posts:
    posts_title.append(post.h2.text)

author = soup_1.find_all('span', class_='d-inline-block')
for writer in author:
    posts_author.append(writer.a.text)

categories = soup_1.find_all('span', class_='post-category')
for category in categories:
    posts_category.append(category.text)


# getting data from second page     

posts = soup_2.find_all('div', class_='excerpt')
for post in posts:
    posts_title.append(post.h2.text) 

author = soup_2.find_all('span', class_='d-inline-block')
for writer in author:
    posts_author.append(writer.a.text)

categories = soup_2.find_all('span', class_='post-category')
for category in categories:
    posts_category.append(category.text)


# getting data from third page 

posts = soup_3.find_all('div', class_='excerpt')
for post in posts:
    posts_title.append(post.h2.text)

author = soup_3.find_all('span', class_='d-inline-block')
for writer in author:
    posts_author.append(writer.a.text)

categories = soup_3.find_all('span', class_='post-category')
for category in categories:
    posts_category.append(category.text)

 

data = pd.DataFrame(list(zip(posts_category, posts_author, posts_title)), columns=['category','author','post title'])
data.to_csv('sunblog.csv')

