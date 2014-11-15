
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker 

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref, scoped_session

engine = create_engine("sqlite:///tate.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,autocommit = False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()


class Artist(Base):
    __tablename__ = 'artist' 

    id = Column(Integer, primary_key = True)
    name = Column(String(64))
    gender = Column(String(64), nullable = True)
    dates = Column(String(64), nullable=True) 
    yearOfBirth = Column(String(15), nullable = True)
    yearOfDeath = Column(String(64), nullable = True)
    placeOfBirth = Column(String(64), nullable = True)
    info_url = Column(String(64), nullable = True)

    artworks = relationship("Artwork", backref=backref("artist"))

    #backref to artist_movements table

class Artwork(Base):
    __tablename__ = 'artwork'

    id = Column(Integer, primary_key = True)
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
    url = Column(String(1024), nullable = True)

    # backref to artist table

    # def format date Text.. ????


class Artist_movement(Base):
    __tablename__ = 'artist_movements'

    id = Column(Integer, primary_key = True)
    artistId = Column(Integer, ForeignKey("artist.id"))  
    movementId = Column(Integer, ForeignKey("movements.id"))
    era_id = Column(Integer, ForeignKey("eras.id"))

    artist = relationship("Artist", backref=backref("artist_movements"))
    movement = relationship("Movement", backref=backref("artist_movements"))
    era = relationship("Era", backref=backref("artist_movements"))


    

   

class Movement(Base):
    __tablename__ = 'movements'

    id = Column(Integer, primary_key = True)
    name = Column(String(64), nullable = True)
    thumbnailURL = Column(String(64), nullable = True)
    numArtist = Column(Integer, nullable = True)
    numArtwork = Column(Integer, nullable = True)


    #backref to artist_movements table

class Era(Base):
    __tablename__ ='eras'
    id = Column(Integer,primary_key = True)
    name = Column(String(64), nullable = True)
    thumbnailURL = Column(String(64), nullable = True)
    numArtist = Column(Integer, nullable = True)
    numArtwork = Column(Integer, nullable = True)



    # era.artist_movement.movementId
    # get the number of distinct movements per era. 

    # backref to artist_movements table



     
def create_tables():

    # global ENGINE
    # global Session

    # ENGINE = create_engine("sqlite:///tate.db", echo=True)
    Base.metadata.create_all(engine)
    # Session = sessionmaker(bind=ENGINE)


def main():
    """In case we need this for something"""
   

if __name__ == "__main__":
    main()