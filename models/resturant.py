from sqlalchemy import Column, Integer, String, Date, Float
from models.base import Base
import datetime

#### Resturant class to create Title table
class Resturant(Base):
    __tablename__ = 'resturant'

    id = Column(Integer, primary_key=True)
    resturant_id = Column(String)
    name = Column(String)
    alias = Column(String)
    url = Column(String)
    image_url = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    address = Column(String)
    insert_date = Column(Date(), default=datetime.datetime.now().date())

    def __repr__(self):
        return "<Title (resturant_id='%s', name='%s', alias='%s', url='%s', image_url='%s', latitude='%s', longitude='%s', address='%s', inserted_date='%s' )" % (self.resturant_id, self.name, self.alias, self.url, self.image_url, self.latitude, self.longitude, self.address, self.inserted_date)
