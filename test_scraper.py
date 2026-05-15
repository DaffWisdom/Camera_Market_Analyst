import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# 1. Initialize an empty list to store the scraped data
scraped_data = []

# Headers to mimic a real web browser and bypass basic anti-bot systems
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Create a session for better performance and connection reuse
session = requests.Session()
session.headers.update(headers)

# 2. Loop through the first 5 pages (Pagination)
for current_page in range(1, 6):
    print(f"\n---> Scraping Page {current_page}...")
    
    # Dynamic URL with f-string for pagination
    url = f"https://www.chotot.com/mua-ban-may-anh-may-quay-may-anh-canon-sdct1eb1?q=canon%20r50&page={current_page}"
    
    try:
        # Send HTTP GET request using the session
        response = session.get(url, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Locate product names and prices (UPDATE THESE CLASSES BASED ON YOUR INSPECT ELEMENT)
            product_names = soup.find_all('h2', class_='ag5pmh3') 
            product_prices = soup.find_all('span', class_='bfe6oav tqqmhlc') 
            
            # Break the loop if the page is empty (reached the end of search results)
            if len(product_names) == 0:
                print("No more products found. Terminating the scraping process.")
                break
                
            print(f"Successfully extracted {len(product_names)} products on Page {current_page}.")
            
            # Zip names and prices together, append to the main list
            for name_tag, price_tag in zip(product_names, product_prices):
                scraped_data.append({
                    'Product_Name': name_tag.text.strip(),
                    'Price': price_tag.text.strip()
                })
                
        else:
            print(f"Connection error on Page {current_page} (Status Code: {response.status_code})")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred on Page {current_page}: {e}")
        
    # ANTI-BAN MECHANISM: Random delay between 2 to 4 seconds
    sleep_time = random.uniform(2, 4)
    print(f"Pausing for {sleep_time:.2f} seconds to avoid rate limiting...")
    time.sleep(sleep_time)

# 3. Export the collected data to a CSV file
if len(scraped_data) > 0:
    df = pd.DataFrame(scraped_data)
    # Using utf-8-sig to prevent font encoding issues with Vietnamese characters in Excel
    df.to_csv('used_camera_canon_r50_raw.csv', index=False, encoding='utf-8-sig')
    print(f"\n SUCCESS! Scraped a total of {len(scraped_data)} products and saved to 'used_camera_canon_r50_raw.csv'.")
else:
    print("\n Failed to scrape data. The list is empty.")