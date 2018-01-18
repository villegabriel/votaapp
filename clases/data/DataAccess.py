from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import sessionmaker




class DataAccess():
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root@localhost:3306/votaapp')
        base = declarative_base()
        base.metadata.bind = self.engine
        session = sessionmaker()
        session.bind = self.engine
        self.session = session()

    def get_session(self):
        return self.session

    def get_engine(self):
        return self.engine

def get_data_access_instance():
    return data_access

data_access = DataAccess()