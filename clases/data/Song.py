from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from DataAccess import *

Base = declarative_base()
Base.metadata.bind = get_data_access_instance().get_engine()
class Song(Base):

    __tablename__ = 'songs'

    idSong = Column(String, primary_key=True)
    name = Column(String)
    artist_name = Column(String)