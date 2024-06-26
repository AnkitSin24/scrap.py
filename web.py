import requests
from bs4 import BeautifulSoup
import re
import csv

def get_emails_from_url(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    print("helloworld")

    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser'
                         )
    print(soup)
    
    # Convert the soup to a string
    soup_str = str(soup)
    
    # Find all email addresses using regular expressions
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup_str)
    
    return emails

def save_emails_to_csv(emails, filename):
    # Write the emails to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        email_writer = csv.writer(csvfile)
        # Write the header
        email_writer.writerow(['Email'])
        # Write the emails
        for email in emails:
            email_writer.writerow([email])


url = 'https://www.specrom.com/wsj.com/'
emails = get_emails_from_url(url)

if emails:
    save_emails_to_csv(emails, 'emails.csv')
    print(f"Saved {len(emails)} emails to emails.csv")
else:
    print("No emails found.")
