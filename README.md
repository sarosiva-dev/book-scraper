#  Book Scraper

A Python web scraping project built with **Scrapy** to extract book information from a website and store the collected data in structured formats.

##  Features

- Extracts book names
- Extracts book prices
- Extracts availability status
- Extracts star ratings
- Cleans unnecessary whitespace and newlines
- Converts star ratings from words into numbers
- Exports scraped data to JSON and CSV

##  Technologies Used

- Python
- Scrapy
- CSS Selectors
- JSON
- CSV

##  Data Collected

The scraper collects:

| Field | Description |
|---|---|
| Book Name | Name of the book |
| Price | Current listed price |
| Availability | Whether the book is in stock |
| Star Rating | Rating converted into a number |
