from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.base import Base


class DB:
    __session = None

    def __init__(self): ### constructor of DB class
        if not DB.__session:
            DB.__session = self.create_db_session()

    def create_db_session(self):
        ###engine = create_engine(DATABASE_URI) #sql server
        engine = create_engine('mssql+pyodbc://localhost/Georgian_College?driver=SQL+Server+Native+Client+11.0')
        Base.metadata.create_all(engine) ### creating database and tables if it does not exists

        Session = sessionmaker(bind = engine)
        session = Session() ### creating a session of the database

        return session

    def get_db(self):
        return DB.__session

    def close(self):
        DB.__session.close()