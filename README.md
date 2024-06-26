# 📧 Email Scraper

A Python script that scrapes email addresses from a specified URL and saves them to a CSV file. This script utilizes the `requests` library to fetch the web page, `BeautifulSoup` to parse the HTML, and a regular expression to find email addresses.

## 🛠 Prerequisites

Before running the script, ensure you have Python installed on your system. You also need the following libraries:
- `requests`
- `beautifulsoup4`

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4




📜 Code Explanation
get_emails_from_url(url)
Sends an HTTP GET request to the URL.
Parses the HTML content using BeautifulSoup.
Finds all email addresses using a regular expression.
Returns the email addresses as a list.
save_emails_to_csv(emails, filename)
Takes a list of email addresses and a filename.
Writes the email addresses to a CSV file.
Main Script
Sets the url variable to the target website.
Calls get_emails_from_url(url) to retrieve email addresses.
Calls save_emails_to_csv(emails, 'emails.csv') to save them to a CSV file.

📋 Example
To scrape emails from https://www.example.com and save them to emails.csv:



📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

Feel free to reach out if you have any questions or suggestions! Happy scraping! 🎉
