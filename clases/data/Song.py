from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from DataAccess import *

Base = declarative_base()
Base.metadata.bind = get_data_access_instance().get_engine()
class Song(Base):

    __tablename__ = 'songs'

    id_song = Column(String, primary_key=True)
    name = Column(String)
    artist_name = Column(String)

    def __init__(self, id = None, name = None, artist_name = None):
        self.id_song = id
        self.name = name
        self.artist_name = artist_name