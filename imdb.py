import requests
from bs4 import BeautifulSoup

# Replace this with the URL of the IMDb Top 250 Movies page
url = ''

# Send a GET request to the IMDb Top 250 Movies page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the top 250 movies
    table = soup.find('tbody', class_='lister-list')
    
    # Initialize lists to hold movie titles and links
    link_list = []
    
    # Extract movie titles and links
    for row in table.find_all('tr'):
        title_column = row.find('td', class_='titleColumn')
        title = title_column.a.text
        link = 'https://www.imdb.com' + title_column.a['href']
        link_list.append(link)

    # Print the number of movies found
    print("Number of movies found:", len(link_list))

    # Example variable n; replace it with your logic for selecting movies
    n = int(input("Enter a number (1 to {}): ".format(len(link_list))))

    # Check if n is within the valid range
    if n < 1 or n > len(link_list):
        print(f"Error: n={n} is out of range. Valid range is 1 to {len(link_list)}.")
    else:
        # Fetch the selected movie page
        page_text = requests.get(link_list[n-1]).text  # Adjusted index to n-1 for zero-based indexing
        print(f"Successfully fetched page for {n}-th movie: {link_list[n-1]}")
        
        # You can continue processing the page_text as needed

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
