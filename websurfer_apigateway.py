import requests
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS, ALL_REGIONS

import random

from bs4 import BeautifulSoup
from urllib.parse import unquote
from dotenv import load_dotenv
import os


### SEARCH CONFIG

# We return 10 results by default
n_results = 10

# You can change this list to add or change any search queries you might want to test
keywords = ['joe biden']

# Load .env into envinroment variables
load_dotenv()

# Retrieve our AWS access key
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_ACCESS_KEY_SECRET = os.environ.get('AWS_ACCESS_KEY_SECRET')

### APIGATEWAY CONFIG

# You can choose US or EU only regions for the Gateway IPs if you want in AWS, for example:

US_REGIONS = [region for region in ALL_REGIONS if "us-" in region]
EU_REGIONS = [region for region in ALL_REGIONS if "eu-" in region]

# Create gateway object and initialise in AWS - by default I use US regions
gateway = ApiGateway("https://www.google.com", 
                    regions=US_REGIONS, 
                    access_key_id=AWS_ACCESS_KEY_ID, 
                    access_key_secret=AWS_ACCESS_KEY_SECRET)

### MAIN CODE

# Start the gateway
gateway.start(force=True)

# Start a new request session with this gateway
session = requests.Session()
session.mount("https://www.google.com", gateway)

# Search all keywords
for keyword in keywords:
    responses = []
    
    # Keep going until we get status 200 - in the case the request fails
    while True:
        response = session.get(f'https://www.google.com/search?q', params={'q':f'{keyword}', 'num':n_results+2}) # For some reason, you have to add 2 to return the proper number of results
        
        response = {'status': response.status_code, 'body': response.text}

        responses.append(response)
        
        if response['status'] == 200:
            break
    
    # Collect the HTML of every page    
    html_pages = [response['body'] for response in responses if response['status'] == 200]

    for html in html_pages:
        soup = BeautifulSoup(html)
        # Remove prefix and suffixes so we get the original URL and decode it so we don't have special characters becoming strange strings
        hrefs = [unquote(a['href'].split('/url?q=')[-1].split('&sa')[0]) for a in soup.find_all('a') if a.find('h3')]
        # Print all the URLs we found for a page as a list
        print(hrefs)
        
# Shut down the gateway
gateway.shutdown()