from sqlalchemy import Column, Integer, String, Date, Float
from models.base import Base
import datetime

#### Review class to create Review table
class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    resturant_id = Column(String)
    review_id = Column(String)
    author = Column(String)
    rating = Column(String)
    insert_date = Column(Date(), default=datetime.datetime.now().date())

    def __repr__(self):
        return "<Title (resturant_id='%s', review_id='%s', author='%s', rating='%s', inserted_date='%s' )" % (self.resturant_id, self.review_id, self.author, self.rating, self.inserted_date)
