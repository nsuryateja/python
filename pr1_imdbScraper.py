#This following code scrapes the IMDB website for top 250 indian movies and dictionary of movie name,rating and year of release
from bs4 import BeautifulSoup
import requests
source = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?sort=rk,asc&mode=simple&page=1").text
soup =  BeautifulSoup(source,'lxml')
#Movies List: Consists of top 250 movies
movies = []
for title in soup.find_all("td",class_="titleColumn"):
    movies.append(title.text.strip())
#As the name says, ratings contains ratings of each movie
ratings = []
for rating in soup.find_all("td",class_="imdbRating"):
    ratings.append(rating.strong.text)
#year of release of each movie
years = []
for year in soup.find_all("span",class_ = "secondaryInfo"):
    years.append(year.text[1:5])
movies = ','.join(movies).split("\n")
# This list has nicely formatted movie names
movie = []
for i in range(len(movies)):
    if not i%2==0:
        movie.append(movies[i].strip())
# To print in "250 Nannaku Prematho 7.2 2012" format
imdbDict = {}
for x,y in enumerate(movie):
    #print(str(x+1) + ' ' + y + ' ' + str(ratings[x-1]) +  ' ' + str(years[x-1]))
    imdbDict[y] = [ratings[x-1],years[x-1]]
print(imdbDict)


