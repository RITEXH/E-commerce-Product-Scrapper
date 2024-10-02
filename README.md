# Ecommerce Product Scraper

## Description

This repository contains a Python script that scrapes product information from an e-commerce website. The script extracts product names, prices, and ratings from a specified URL and saves this data into a CSV file named `products.csv`. It uses `requests` to fetch the webpage content, `BeautifulSoup` to parse the HTML, and `pandas` to handle the data and save it in CSV format.

## Features

- Fetches product details (name, price, rating) from a provided e-commerce webpage.
- Handles network errors and missing data gracefully.
- Saves extracted data in a structured CSV file.

## Requirements

- `requests`
- `beautifulsoup4`
- `pandas`

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
