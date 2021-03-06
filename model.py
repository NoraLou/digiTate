import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker 

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref, scoped_session

# DATABASE_URL = "postgres://mmlwhgyehyapbb:ZvhbR-8OOh3rOUFSFXGOjRmNNd@ec2-54-204-42-119.compute-1.amazonaws.com:5432/dbvie29n4j53hl"
DATABASE_URL = os.environ.get("DATABASE_URL", 'postgresql://localhost/tatedb')
engine = create_engine(DATABASE_URL, echo=False)

# engine = create_engine("sqlite:///tate.db", echo=False)

session = scoped_session(sessionmaker(bind=engine,autocommit = False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()


class Artist(Base):
    __tablename__ = 'artist' 

    id = Column(Integer, primary_key = True)
    name = Column(String(128))
    gender = Column(String(128), nullable = True)
    dates = Column(String(128), nullable=True) 
    yearOfBirth = Column(String(128), nullable = True)
    yearOfDeath = Column(String(128), nullable = True)
    placeOfBirth = Column(String(128), nullable = True)
    info_url = Column(String(128), nullable = True)
    numArtwork = Column(Integer, nullable = True)
    thumbnailURL = Column(String(128), nullable = True)
    numImgs = Column(Integer, nullable = True)

    artworks = relationship("Artwork", backref=backref("artist"))

    #backref to artist_movements table


class Artwork(Base):
    __tablename__ = 'artwork'

    id = Column(Integer, primary_key = True)
    accession_number = Column(String(128), nullable = True)
    artistId = Column(Integer, ForeignKey("artist.id")) 
    artistRole = Column(String(128), nullable = True)
    title = Column(String(1024), nullable = True)
    dateText = Column(String(128), nullable = True)
    medium = Column(String(128), nullable = True)
    creditLine = Column(String(128), nullable = True)
    year = Column(Integer, nullable = True)
    acquisitionYear = Column(Integer, nullable = True)
    dimensions = Column(String(1024), nullable = True)
    width = Column(Integer, nullable = True)
    height = Column(Integer, nullable = True)
    depth = Column(Integer, nullable = True)
    units = Column(String(128), nullable = True)
    thumbnailURL = Column(String(128), nullable = True)
    url = Column(String(1024), nullable = True)


    def thumbnail_format(self):
        base_url = self.thumbnailURL.split("_8.jpg")[0]
        return base_url+"_"+"9"+".jpg"



    def convert_to_JSON(self): 
        d = {"id": self.id, 
            "thumbnailURL": self.thumbnail_format(),
            "artist": self.artist.name,
            "title" : self.title,
            "year" : self.year,
            "medium" : self.medium,
            "dimensions" : self.dimensions,
             }
       
        return d 


  

class Artist_movement(Base):
    __tablename__ = 'artist_movements'

    id = Column(Integer, primary_key = True)
    artistId = Column(Integer, ForeignKey("artist.id"))  
    movementId = Column(Integer, ForeignKey("movements.id"))
    

    artist = relationship("Artist", backref=backref("artist_movements"))
    movement = relationship("Movement", backref=backref("artist_movements"))
    
    def convert_to_JSON(self): 
        d = {}
        d = {"id": self.id, "thumbnailURL": self.thumbnailURL}
        return d 
    


class Movement(Base):
    __tablename__ = 'movements'

    id = Column(Integer, primary_key = True)
    era_id = Column(Integer, ForeignKey("eras.id"))
    name = Column(String(128), nullable = True)
    thumbnailURL = Column(String(128), nullable = True)
    numArtist = Column(Integer, nullable = True)
    numArtwork = Column(Integer, nullable = True)

    # era = relationship("Era", backref=backref("movements"))
    #backref to artist_movements table

    def convert_to_JSON(self): 
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
    name = Column(String(128), nullable = True)
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