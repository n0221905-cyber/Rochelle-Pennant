import firecrawl

class FirecrawlScraper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = firecrawl.Client(api_key)

    def scrape(self, url):
        try:
            # Perform a web scraping operation using the Firecrawl API.
            data = self.client.scrape(url)
            return data
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

if __name__ == '__main__':
    # Example usage
    api_key = 'YOUR_API_KEY'
    url = 'http://example.com'
    scraper = FirecrawlScraper(api_key)
    scraped_data = scraper.scrape(url)
    print(scraped_data)