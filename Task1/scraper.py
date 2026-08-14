import csv
import re


# Sample scraped data
raw_properties = [
    {
        "title": "2 BHK Apartment",
        "price": "₹45,00,000",
        "location": "Tirupati, Andhra Pradesh"
    },
    {
        "title": "3 BHK Luxury Villa",
        "price": "₹75,00,000",
        "location": "Bangalore, Karnataka"
    },
    {
        "title": "1 BHK Flat",
        "price": "₹32,50,000",
        "location": "Chennai, Tamil Nadu"
    },
    {
        "title": "4 BHK Independent House",
        "price": "₹1,20,00,000",
        "location": "Hyderabad, Telangana"
    },
    {
        "title": "2 BHK Premium Flat",
        "price": "₹58,00,000",
        "location": "Vijayawada, Andhra Pradesh"
    }
]


# Clean text
def clean_text(text):

    text = re.sub(r"\s+", " ", text)
    return text.strip()


# Clean property data
cleaned_properties = []

for property_data in raw_properties:

    title = clean_text(
        property_data["title"]
    )

    price = clean_text(
        property_data["price"]
    )

    location = clean_text(
        property_data["location"]
    )

    cleaned_properties.append({
        "Property Title": title,
        "Price": price,
        "Location": location
    })


# Create CSV file
filename = "properties.csv"

with open(
    filename,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "Property Title",
        "Price",
        "Location"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(cleaned_properties)


# Display results
print("\n========== REAL ESTATE DATA ==========\n")

for i, property_data in enumerate(
    cleaned_properties,
    start=1
):

    print(f"Property {i}")
    print("-" * 35)

    print(
        "Title    :",
        property_data["Property Title"]
    )

    print(
        "Price    :",
        property_data["Price"]
    )

    print(
        "Location :",
        property_data["Location"]
    )

    print()


print("======================================")
print(
    "Total Properties:",
    len(cleaned_properties)
)

print(
    "CSV file created:",
    filename
)
