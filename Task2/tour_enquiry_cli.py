import argparse
import re
import sys


# ---------------------------------------------------------
# Regex Patterns
# ---------------------------------------------------------

NAME_PATTERN = re.compile(
    r"(?:Name|Customer|Client|From)\s*[:\-]\s*"
    r"([A-Za-z][A-Za-z .'-]{1,50})",
    re.IGNORECASE
)

EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)

DESTINATION_PATTERN = re.compile(
    r"(?:Destination|Dest|Travel To|Travelling To|Going To|Visit)\s*"
    r"[:\-]\s*([A-Za-z][A-Za-z ,.'-]{1,60})",
    re.IGNORECASE
)


# ---------------------------------------------------------
# Cleaning Functions
# ---------------------------------------------------------

def clean_name(name):
    """Clean and format customer name."""
    name = re.sub(r"\s+", " ", name)
    name = name.strip(" -:,.")
    return name.title()


def clean_destination(destination):
    """Clean and format destination."""
    destination = re.sub(r"\s+", " ", destination)
    destination = destination.strip(" -:,.")
    return destination.title()


# ---------------------------------------------------------
# Extraction Functions
# ---------------------------------------------------------

def extract_name(text):
    """Extract customer name from text."""
    match = NAME_PATTERN.search(text)

    if match:
        return clean_name(match.group(1))

    return "Unknown"


def extract_email(text):
    """Extract email address from text."""
    match = EMAIL_PATTERN.search(text)

    if match:
        return match.group(0).lower()

    return "Unknown"


def extract_destination(text):
    """Extract travel destination from text."""
    match = DESTINATION_PATTERN.search(text)

    if match:
        return clean_destination(match.group(1))

    return "Unknown"


# ---------------------------------------------------------
# Process Enquiries
# ---------------------------------------------------------

def process_enquiry(enquiry):
    """Extract all required information from one enquiry."""

    return {
        "name": extract_name(enquiry),
        "email": extract_email(enquiry),
        "destination": extract_destination(enquiry)
    }


def read_file(filename):
    """Read the enquiry file."""

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print(f"\nError: File '{filename}' not found.")
        sys.exit(1)

    except PermissionError:
        print(f"\nError: Permission denied for '{filename}'.")
        sys.exit(1)


# ---------------------------------------------------------
# Split Raw Enquiries
# ---------------------------------------------------------

def split_enquiries(text):
    """
    Split enquiries using blank lines.

    Each enquiry should be separated by an empty line.
    """

    enquiries = re.split(r"\n\s*\n", text.strip())

    return [item.strip() for item in enquiries if item.strip()]


# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

def display_results(results):
    """Display clean enquiry summary in terminal."""

    print("\n" + "=" * 75)
    print("              TOUR ENQUIRY SUMMARY")
    print("=" * 75)

    print(
        f"{'No.':<5}"
        f"{'Name':<25}"
        f"{'Email':<30}"
        f"{'Destination':<20}"
    )

    print("-" * 75)

    for index, result in enumerate(results, start=1):

        print(
            f"{index:<5}"
            f"{result['name'][:23]:<25}"
            f"{result['email'][:28]:<30}"
            f"{result['destination'][:18]:<20}"
        )

    print("-" * 75)
    print(f"Total enquiries processed: {len(results)}")
    print("=" * 75)


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Tour Enquiry CLI Tool - "
            "Extract names, emails and destinations "
            "from messy enquiry text using Regular Expressions."
        )
    )

    parser.add_argument(
        "file",
        help="Path to the raw tour enquiries text file"
    )

    args = parser.parse_args()

    # Read file
    raw_text = read_file(args.file)

    # Split enquiries
    enquiries = split_enquiries(raw_text)

    if not enquiries:
        print("\nNo enquiries found in the file.")
        sys.exit(0)

    # Process enquiries
    results = []

    for enquiry in enquiries:
        result = process_enquiry(enquiry)
        results.append(result)

    # Display clean summary
    display_results(results)


# ---------------------------------------------------------
# Program Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
