
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
    numArtwork = Column(Integer, nullable = True)
    thumbnailURL = Column(String(64), nullable = True)
    numImgs = Column(Integer, nullable = True)

    artworks = relationship("Artwork", backref=backref("artist"))

    #backref to artist_movements table
    # !!!! ADD CONVERT TO JSON METHOD


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

    def convert_to_JSON(self): 
        # whenever you have an artwork object, you call example.covert_to_JSON
        d = {}
        d = {"id": self.id, "thumbnailURL": self.thumbnailURL}
        # d["artist"]= self.artist.convert_to_JSON()
        return d 

    # backref to artist table



class Artist_movement(Base):
    __tablename__ = 'artist_movements'

    id = Column(Integer, primary_key = True)
    artistId = Column(Integer, ForeignKey("artist.id"))  
    movementId = Column(Integer, ForeignKey("movements.id"))
    

    artist = relationship("Artist", backref=backref("artist_movements"))
    movement = relationship("Movement", backref=backref("artist_movements"))
    
    def convert_to_JSON(self): 
        # whenever you have an artwork object, you call example.covert_to_JSON
        d = {}
        d = {"id": self.id, "thumbnailURL": self.thumbnailURL}
        # d["artist"]= self.artist.convert_to_JSON()
        return d 
    


class Movement(Base):
    __tablename__ = 'movements'

    id = Column(Integer, primary_key = True)
    era_id = Column(Integer, ForeignKey("eras.id"))
    name = Column(String(64), nullable = True)
    thumbnailURL = Column(String(64), nullable = True)
    numArtist = Column(Integer, nullable = True)
    numArtwork = Column(Integer, nullable = True)

    # era = relationship("Era", backref=backref("movements"))
    #backref to artist_movements table

    def convert_to_JSON(self): 
        # whenever you have an object, you call example.covert_to_JSON
        d = {
            "id": self.id, 
            "thumbnailURL": self.thumbnailURL, 
            "era_id": self.era_id, 
            "name": self.name, 
            "numArtist": self.numArtist, 
            "numArtwork": self.numArtwork
        }
       
        return d 

class Era(Base):
    __tablename__ ='eras'
    id = Column(Integer,primary_key = True)
    name = Column(String(64), nullable = True)
    numArtist = Column(Integer, nullable = True)
    numArtwork = Column(Integer, nullable = True)
    
    movements = relationship("Movement", backref=backref("era"))

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