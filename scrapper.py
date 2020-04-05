import requests
from bs4 import BeautifulSoup
from sentiment import sentiment_calculator
from jobs.cron import insert_review_data, insert_keyword_data
import datetime

cycle_time_id = datetime.datetime.now().strftime('%Y%m%d')

def reviews(resturant_data):

    start_count = 0
    review_count = 1

    reviews_raw_data = BeautifulSoup(requests.get(resturant_data['url']).content, 'html.parser').find_all(itemprop="review")

    for review in reviews_raw_data:

        review_data = {}

        review_data['resturant_id'] = resturant_data['id']
        review_data['review_id'] = resturant_data['id'] + '_' + datetime.datetime.now().strftime('%Y%m%d') + '_' + str(review_count)
        review_data['description'] = review.get_text().strip('\n')
        review_data['rating'] = review.find(itemprop="ratingValue")['content']
        review_data['author'] = review.find(itemprop="author")['content']

        insert_review_data(review_data)
        final_words = sentiment_calculator(review_data)

        insert_keyword_data(final_words)

        review_count = review_count + 1

    print(review_data)
