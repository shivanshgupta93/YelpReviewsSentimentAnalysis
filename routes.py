import requests
import json
from consts import YELP_API_KEY, URL
from scrapper import reviews
from jobs.cron import insert_resturant_data

def resturants():

    payload={
        "term": "tim hortons",
        "location": "toronto",
        "categories": "coffee",
        "limit": "50"
    }

    resturant_raw_data = requests.get(URL, params=payload, headers={"Authorization": "Bearer %s" % YELP_API_KEY}).json()

    for resturant in resturant_raw_data['businesses']:
        resturant_data = {}

        resturant_data['id'] = resturant['id']
        resturant_data['alias'] = resturant['alias']
        resturant_data['name'] = resturant['name']
        resturant_data['url'] = resturant['url']
        resturant_data['image_url'] = resturant['image_url']
        resturant_data['latitude'] = resturant['coordinates']['latitude']
        resturant_data['longitude'] = resturant['coordinates']['longitude']
        resturant_data['address'] = resturant['location']['display_address'][0] + ", " + resturant['location']['display_address'][1]

        insert_resturant_data(resturant_data)
        reviews(resturant_data)