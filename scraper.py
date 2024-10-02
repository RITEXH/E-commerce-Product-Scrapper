import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_product_data(url):
    """Fetch product data from the provided URL and return it as a list of dictionaries."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = []

    # Extract product details
    for product in soup.select('.product_pod'):
        try:
            name = product.select_one('h3 a').get('title')
            price = product.select_one('.price_color').get_text(strip=True)
            rating = product.select_one('.star-rating')['class'][1]  # Extract rating from class name

            products.append({
                'Name': name,
                'Price': price,
                'Rating': rating
            })
        except AttributeError as e:
            print(f"Error extracting product data: {e}")

    return products

def save_to_csv(products, filename):
    """Save the list of products to a CSV file."""
    if products:
        df = pd.DataFrame(products)
        df.to_csv(filename, index=False)
        print(f"Product information has been saved to '{filename}'.")
    else:
        print("No data to save.")

def main():
    url = 'https://books.toscrape.com/'
    products = fetch_product_data(url)
    save_to_csv(products, 'products.csv')

if __name__ == '__main__':
    main()
