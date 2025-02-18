
import pandas as pd   
import requests      
from bs4 import BeautifulSoup 
import numpy as np  # to count the values (in our case)

#assigning the URL with variable name url
url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
#request allow you to send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#creating an empty list, so that we can append the values
movie_name = []
year = []
time = []
rating = []
metascore = []
votes = []
gross = []
#Note: These three list are added recently, Not explained in the video
description = []
Director = []
Stars = []

#storing the meaningful required data in the variable
movie_data = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
print(f"Total movies found:250")

#calling one by one using for loop
for idx, store in enumerate(movie_data):
    print(f"Processing movie {idx + 1} of {len(movie_data)}")
    
    name = store.h3.a.text
    movie_name.append(name)
    
    year_of_release = store.h3.find('span', class_='lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
    year.append(year_of_release)
    
    runtime = store.p.find('span', class_='runtime').text.replace(' min', '')
    time.append(runtime)
    
    rate = store.find('div', class_='inline-block ratings-imdb-rating').text.replace('\n', '')
    rating.append(rate)
    
    meta = store.find('span', class_='metascore').text.replace(' ', '') if store.find('span', class_='metascore') else 'N/A'
    metascore.append(meta)
    
    # since, gross and votes have same attributes, that's why we had created a common variable and then used indexing
    value = store.find_all('span', attrs={'name': 'nv'})
    
    vote = value[0].text
    votes.append(vote)
    
    grosses = value[1].text if len(value) > 1 else 'N/A'
    gross.append(grosses)
    
    # Description of the Movies -- Not explained in the Video, But you will figure it out. 
    describe = store.find_all('p', class_='text-muted')
    description_ = describe[1].text.replace('\n', '') if len(describe) > 1 else 'N/A'
    description.append(description_)
    
    # Cast Details -- Scraping Director name and Stars -- Not explained in Video
    cast = store.find("p", class_='')
    cast = cast.text.replace('\n', '').split('|')
    cast = [x.strip() for x in cast]
    cast = [cast[i].replace(j, "") for i, j in enumerate(["Director:", "Stars:"])]
    Director.append(cast[0])
    Stars.append([x.strip() for x in cast[1].split(",")])

# Creating a dataframe using pandas library
movie_DF = pd.DataFrame({
    'Name of movie': movie_name,
    'Year of release': year,
    'Watchtime': time,
    'Movie Rating': rating,
    'Metascore': metascore,
    'Votes': votes,
    'Gross collection': gross,
    'Description': description,
    'Director': Director,
    'Star': Stars
})


movie_DF.to_csv("Top_250_IMDB_Movies.csv", index=False)
print("Data saved to Top_250_IMDB_Movies.csv")


if not movie_DF.empty:
    print(movie_DF.head(7))
