import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the target URL
url = "https://www.scrapethissite.com/pages/simple/"

# Step 2: Send a GET request
response = requests.get(url)

# Step 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract data for each country
countries = []
rows = soup.find_all('div', class_='col-md-4 country')  # Select elements containing country data

for row in rows:
    name = row.find('h3', class_='country-name').text.strip()
    capital = row.find('span', class_='country-capital').text.strip()
    population = row.find('span', class_='country-population').text.strip()
    area = row.find('span', class_='country-area').text.strip()

    countries.append({
        'Name': name,
        'Capital': capital,
        'Population': population,
        'Area': area
    })

# Step 5: Save the data to a CSV file
df = pd.DataFrame(countries)
df.to_csv('countries_data.csv', index=False)

print("Data collection complete. Saved to 'countries_data.csv'.")
