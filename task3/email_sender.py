import csv
import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


# --------------------------------------------------
# Check environment variables
# --------------------------------------------------

if not EMAIL_ADDRESS or not EMAIL_APP_PASSWORD:
    print("ERROR: Email credentials are missing.")
    print("Please check your .env file.")
    exit()


# --------------------------------------------------
# Email sending function
# --------------------------------------------------

def send_confirmation_email(
    customer_name,
    customer_email,
    destination
):

    subject = "Tour Booking Confirmation"

    body = f"""
Dear {customer_name},

Thank you for choosing our tour service!

Your tour enquiry has been successfully confirmed.

Destination: {destination}

We will contact you shortly with additional information
regarding your tour.

Thank you for choosing us.

Best Regards,
Tour Management Team
"""


    # Create email
    message = MIMEMultipart()

    message["From"] = EMAIL_ADDRESS
    message["To"] = customer_email
    message["Subject"] = subject

    message.attach(
        MIMEText(body, "plain")
    )


    # Connect to Gmail SMTP server
    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            EMAIL_ADDRESS,
            EMAIL_APP_PASSWORD
        )

        server.send_message(message)


# --------------------------------------------------
# Read customers from CSV
# --------------------------------------------------

def process_customers(filename):

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            total = 0

            for customer in reader:

                name = customer["name"].strip()
                email = customer["email"].strip()
                destination = customer["destination"].strip()

                print("\n-----------------------------------")
                print("Sending email to:", email)
                print("Customer:", name)
                print("Destination:", destination)

                try:

                    send_confirmation_email(
                        name,
                        email,
                        destination
                    )

                    print("Status: Email sent successfully!")

                    total += 1

                except Exception as error:

                    print("Status: Failed")
                    print("Error:", error)

            print("\n===================================")
            print("Total emails sent:", total)
            print("===================================")


    except FileNotFoundError:

        print("ERROR: customers.csv file not found.")

    except Exception as error:

        print("ERROR:", error)


# --------------------------------------------------
# Main program
# --------------------------------------------------

if __name__ == "__main__":

    print("======================================")
    print("   CUSTOMER EMAIL CONFIRMATION TOOL")
    print("======================================")

    process_customers("customers.csv")
