import requests
import json
import yelpAPI

business_id = '4AErMBEoNzbk7Q8g45kKaQ'
API_HOST = 'https://api.yelp.com'

# Define API key, endpoint, and header
API_KEY = yelpAPI.api_key
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

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

for biz in business_data['businesses']:
    print(biz['name'])