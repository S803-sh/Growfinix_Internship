import requests
from bs4 import BeautifulSoup
import csv

# ----------------------------------------
# Real Estate Web Scraper
# Tech Stack: Python, Requests, BeautifulSoup4, CSV
# ----------------------------------------

url = "https://example.com/"

# Send request to website
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    properties = []

    # Find all property cards
    property_cards = soup.select(".property-card")

    for card in property_cards:

        # Extract title
        title = card.select_one(".property-title")

        # Extract price
        price = card.select_one(".property-price")

        # Extract location
        location = card.select_one(".property-location")

        # Clean data
        title = title.get_text(" ", strip=True) if title else "N/A"
        price = price.get_text(" ", strip=True) if price else "N/A"
        location = location.get_text(" ", strip=True) if location else "N/A"

        properties.append([title, price, location])

    # ----------------------------------------
    # Save data into CSV file
    # ----------------------------------------

    with open("real_estate_data.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # CSV Header
        writer.writerow([
            "Property Title",
            "Price",
            "Location"
        ])

        # Write property data
        writer.writerows(properties)

    # ----------------------------------------
    # Display result
    # ----------------------------------------

    print("\n" + "=" * 60)
    print("       REAL ESTATE SCRAPING RESULTS")
    print("=" * 60)

    if properties:

        for i, property_data in enumerate(properties, start=1):

            print(f"\nProperty {i}")
            print("-" * 40)
            print("Title    :", property_data[0])
            print("Price    :", property_data[1])
            print("Location :", property_data[2])

        print("\n" + "=" * 60)
        print("Scraping completed successfully!")
        print("CSV file created: real_estate_data.csv")
        print("=" * 60)

    else:

        print("\nNo properties found.")
        print("Check the CSS selectors of the website.")

else:

    print("Unable to access the website.")
    print("Status Code:", response.status_code)
