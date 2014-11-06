from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

ENGINE = None
Session = None

# artist has one id.
# one artist_id has many artworks.

# each artwork has one id and one artist_id

# each artist has one gender
# one gender has many artists.


Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artist' 

    id = Column(Integer, primary_key = True)
    name = Column(String(64), primary_key = True)
    gender = Column(String(64), nullable = True)
    dates = Column(String(64), nullable=True) 
    yearOfBirth = Column(String(15), nullable = True)
    yearOfDeath = Column(String(64), nullable = True)
    placeOfBirth = Column(String(64), nullable = True)
    info_url = Column(String(64), nullable = True)
    #artwork = relationship("Artwork", backref = backref("artist", order_by = "Artwork.artistId"))

 # created an attribute called artistpy that backref to artwork table

class Artwork(Base):
    __tablename__ = 'artwork'

    id = Column(Integer, primary_key = True)
    artworkId = Column(Integer, nullable = True)
    accession_number = Column(Integer, nullable = True)
    artistId = Column(Integer, ForeignKey("artist.id"))
    artistRole = Column(String(64), nullable = True)
    title = Column(String(64), nullable = True)
    dateText = Column(String(64), nullable = True)
    medium = Column(String(64), nullable = True)
    creditLine = Column(String(64), nullable = True)
    year = Column(Integer, nullable = True)
    acquisitionYear = Column(Integer, nullable = True)
    dimensions = Column(String(64), nullable = True)
    width = Column(Integer, nullable = True)
    height = Column(Integer, nullable = True)
    depth = Column(Integer, nullable = True)
    units = Column(String(64), nullable = True)
    inscription = Column(String(64), nullable = True)
    thumbnailCopyright = Column(String(64), nullable = True)
    thumbnailURL = Column(String(64), nullable = True)
    url = Column(String(64), nullable = True)




    
    
    
def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///tate.db", echo=True)
    Base.metadata.create_all(ENGINE)
    Session = sessionmaker(bind=ENGINE)

    return Session()


def main():
    """In case we need this for something"""
   

if __name__ == "__main__":
    main()