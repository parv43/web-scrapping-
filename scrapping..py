import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
url = "https://books.toscrape.com/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the book containers
    book_containers = soup.find_all('article', class_='product_pod')

    # Initialize lists to store data
    titles = []
    prices = []
    urls = []

    # Loop through each book container
    for book in book_containers:
        # Extract the book title
        titles.append(book.h3.a['title'])

        # Extract the book price
        prices.append(book.find('p', class_='price_color').text)

        # Extract the book URL
        urls.append(url + book.h3.a['href'])

    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Title': titles,
        'Price': prices,
        'URL': urls
    })

    # Save the DataFrame to an Excel file
    df.to_excel('book_data.xlsx', index=False)

    print("Data saved to book_data.xlsx successfully.")
else:
    print("Failed to retrieve the webpage")
