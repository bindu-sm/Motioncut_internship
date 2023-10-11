import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Blood_type_distribution_by_country"

response = requests.get(url)

if response.status_code == 200:
   
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table', {'class': 'wikitable'})
    
    with open('blood_type.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        headers = [header.text.strip() for header in table.find_all('th')]
        csv_writer.writerow(headers)
        
        for row in table.find_all('tr')[1:]:
            cells = row.find_all(['th', 'td'])
            row_data = [cell.text.strip() for cell in cells]
            csv_writer.writerow(row_data)
    
    print("Table data has been successfully scraped and saved to 'blood_type.csv'.")
else:
    print("Failed to retrieve data from the URL.")
