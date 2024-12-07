import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

countries = []
rows = soup.find_all('div', class_='col-md-4 country')  

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

df = pd.DataFrame(countries)
df.to_csv('countries_data.csv', index=False)

print("Data collection complete. Saved to 'countries_data.csv'.")
