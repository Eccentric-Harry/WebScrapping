from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.in/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

div_data = soup.find('div', class_='dcl-container-inner')

if div_data:
    print(div_data.text) 
else:
    print("No data found for the specified div.")
