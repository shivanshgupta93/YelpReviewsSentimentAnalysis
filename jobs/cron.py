from sqlalchemy import func
from models.keyword import Keyword
from models.review import Review
from models.resturant import Resturant
from db import DB
from middlewares.serializer import serialize

db_obj = DB() ### creating a object of DB function in db.py file
db_session = db_obj.get_db() ### getting a session of database

def insert_resturant_data(resturant_data):
    resturant_id = db_session.query(Resturant).filter(Resturant.resturant_id == resturant_data['id']).first()

    if resturant_id is None:

        db_session.add_all([Resturant(resturant_id=resturant_data['id'], name=resturant_data['name'], alias=resturant_data['alias'], 
                                  url=resturant_data['url'], image_url=resturant_data['image_url'], latitude=resturant_data['latitude'], 
                                  longitude=resturant_data['longitude'], address= resturant_data['address'])])

        db_session.commit()

def insert_review_data(review_data):

    db_session.add_all([Review(resturant_id=review_data['resturant_id'], review_id=review_data['review_id'], 
                               author=review_data['author'], rating=review_data['rating'])])

    db_session.commit()


def insert_keyword_data(keyword_data):

    for keyword_row in keyword_data['data']:
        db_session.add_all([Keyword(review_id=keyword_row['review_id'], keyword=keyword_row['keyword'], 
                                    keyword_count=int(keyword_row['keyword_count']), 
                                    keyword_sentiment=keyword_row['keyword_sentiment'])])
        
        db_session.commit()

def get_resturant_data():
    resturant_colums = Resturant.__table__.columns.keys()
    resturant = db_session.query(Resturant).all()
    return resturant_colums, serialize(resturant)


def get_review_data():
    review_colums = Review.__table__.columns.keys()
    review = db_session.query(Review).all()
    return review_colums, serialize(review)

def get_keyword_data():
    keyword_colums = Keyword.__table__.columns.keys()
    keyword = db_session.query(Keyword).all()
    return keyword_colums, serialize(keyword)