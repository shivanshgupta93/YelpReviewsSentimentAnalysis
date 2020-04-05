from sqlalchemy import Column, Integer, String, Date, Float
from models.base import Base
import datetime

#### Keyword class to create Keyword table
class Keyword(Base):
    __tablename__ = 'keyword'

    id = Column(Integer, primary_key=True)
    review_id = Column(String)
    keyword = Column(String)
    keyword_count = Column(Integer)
    keyword_sentiment = Column(String)
    insert_date = Column(Date(), default=datetime.datetime.now().date())

    def __repr__(self):
        return "<Title (review_id='%s', keyword='%s', keyword_count='%d', keyword_sentiment='%s', inserted_date='%s' )" % (self.review_id, self.keyword, self.keyword_count, self.keyword_sentiment, self.inserted_date)
