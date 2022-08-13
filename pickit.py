# Yelp business search URL - 'https://api.yelp.com/v3/businesses/search'

# Import the modules
import requests
from yelpAPI import get_key

business_id = 'WavvLdfdP6g8aZTtbBQHTw'

# Define API key, andpoint, and header
API_KEY = get_key()
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorisation': "bearer %s" % API_KEY}

# Ask the user for the rype of food
food_type = input("Please pick an option: 1.Restaurant 2.Fast food 3.Dessert 4.Coffee 5.Boba 6.Alcohol ")


# Define the parameters
PARAMETERS = {'term': food_type,
               'limit': 50,
               'radius': 10000,
               'location': 'San Jose, CA'}

# Make a requet to the yelp API
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

# Convert JSON to a dictionary
business_data = response.json()

for bis in business_data['businesses']:
    print(bis['name'])