
# Customer Email Confirmation Automation

## Description

A Python automation tool that reads customer information from a CSV file and sends personalized confirmation emails.

The project demonstrates secure credential management using environment variables instead of hardcoding passwords in the Python source code.

## Tech Stack

- Python
- smtplib
- email.mime
- python-dotenv
- CSV

## Features

- Reads customer information from CSV
- Sends personalized emails
- Uses Gmail SMTP
- Uses TLS encryption
- Uses environment variables for credentials
- Prevents credentials from being committed to GitHub
- Displays email delivery status in the terminal

## Project Structure

```text
Task3_Email_Automation/
│
├── email_sender.py
├── customers.csv
├── .env
├── .gitignore
└── README.md
