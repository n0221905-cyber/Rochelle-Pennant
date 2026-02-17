# Configuration Settings

# Scraping Targets
SCRAPING_TARGETS = [
    'http://example.com',
    'http://another-example.com',
]

# Cloud Connections
CLOUD_CONNECTIONS = {
    'provider': 'AWS',
    'access_key': 'your_access_key',
    'secret_key': 'your_secret_key',
}

# Lead Extraction Settings
LEAD_EXTRACTION_SETTINGS = {
    'name_selector': '.name',
    'email_selector': '.email',
    'phone_selector': '.phone',
}