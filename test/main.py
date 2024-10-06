from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/?ref_=nv_home'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

# print(soup)
soup.find('table')
soup.find_all('table')[1]
soup.find('table', class_ = 'wikitable sortable')
table = soup.find_all('table')[1]
print(table)

world_titles = table.find_all('th')

world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)

import pandas as pd

df = pd.DataFrame(columns = world_table_titles)

df

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


df

df.to_csv(r'C:\Users\Harin\Desktop\WebScrapping\Companies.csv', index = False)

