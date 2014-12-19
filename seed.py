import json
import model 
import csv
from model import session
import os
import random

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]


def load_artists(session):
    f1 = unicode_csv_reader(open("artist_data.csv"), delimiter=",")
    f1.next()

    for row in f1:
        artist = model.Artist() 
        artist.id = int(row[0])
        artist.name = row[1]
        artist.gender = row[2]
        artist.dates = row[3]
        artist.yearOfBirth = row[4]
        artist.yearOfDeath = row[5]
        artist.placeOfBirth = row[6]
        artist.info_url= row[7]

        session.add(artist)

    session.commit()



def load_artwork(session):
    f2 = unicode_csv_reader(open("artwork_data.csv"), delimiter = ",")
    f2.next()

    for row in f2:
        artwork = model.Artwork()
        artwork.artworkId = int(row[0])
        artwork.artistRole = row[3]
        if int(row[4])!= 19232:
            if int(row[4])!= 5265:
                if int(row[4])!= 3462:
                    if int(row[4])!= 12951:
                        artwork.artistId = int(row[4])
        artwork.title = row[5]
        artwork.dateText = row[6]
        artwork.medium = row[7]
        if row[9].isdigit():
            artwork.year = row[9]
        artwork.dimensions = row[11] 
        if row[12].isdigit():
            artwork.width = row[12]
        if row[13].isdigit():
            artwork.height = row[13]
        if row[15].isdigit():
            artwork.units = row[15]    
        artwork.inscription = row[16]
        artwork.thumbnailCopyright = row[17]
        artwork.thumbnailURL = row[18]
        artwork.url = row[19]

        session.add(artwork)
    session.commit()


def loop_directories (file_path):
    for directr in os.listdir(file_path):

        print directr
        new_dir = file_path + "/" + directr
        print new_dir
        print os.listdir(new_dir)
        file_names = os.listdir(new_dir)
        for i in file_names:
            print i
            load_json(new_dir + "/" + i)


def load_json(file_name):
    file = open(file_name)
    json_text = file.read()
    file.close()

    data = json.loads(json_text)

    artist_id = data.get("id")
    artist = model.session.query(model.Artist).filter_by(id = artist_id).first()


    if data.get("movements",[]):
        for movement in data["movements"]:
            if movement.get("era"):
              
                era_id = movement["era"].get("id")
                era_name = movement["era"].get("name")
                
                if era_id:
                    e = session.query(model.Era).get(era_id)
                    if not e:
                        e = model.Era()
                        e.id = era_id
                        e.name = era_name

                        session.add(e)


            movement_id = movement.get("id")
            movement_name = movement.get("name")

            if movement_id == 22012:
                    continue;
            if movement_id == 22014:
                    continue;
            if movement_id == 425:
                    continue;
            if movement_id == 343:
                    continue;
            if movement_id == 22043:
                    continue;
            if movement_id == 367:
                    continue;
            if movement_id == 293:
                    continue;
 

            if movement_id:          
                m = session.query(model.Movement).get(movement_id)
                if not m:
                    m = model.Movement()
                    m.id = movement_id
                    m.name = movement_name
                    m.era_id = era_id
                
                    session.add(m)

                else:
                    if m.name != movement_name:
                        print "ERROR!  movement name doesn't match!"
                        print movement_id, movement_name
                        print "database has: ", m.name

                am = model.Artist_movement()
                am.movementId = movement_id
                am.artistId = artist_id

                session.add(am)

    session.commit()


def add_artist_details():

     artists = model.session.query(model.Artist).all()
     for artist in artists:
        numImgs = 0
        numArtwork = len(artist.artworks)
        if numArtwork > 0 :
            for art in range(len(artist.artworks)):
                if artist.artworks[art].thumbnailURL:
                    numImgs += 1
                thumbnailURL = artist.artworks[0].thumbnailURL      

        artist.numImgs = numImgs
        artist.numArtwork = numArtwork
        artist.thumbnailURL = thumbnailURL

        session.add(artist)

        session.commit()







def add_details():

    movements = model.session.query(model.Movement).all()

    for movement in movements:
        numArtwork = 0
        numArtist = 0
        for am in movement.artist_movements:
            if am.artist.numImgs > 0:
                numArtist += 1
            numArtwork += am.artist.numImgs
        movement.numArtwork = numArtwork 
        movement.numArtist = numArtist
        session.add(movement)
    session.commit()

    movements = model.session.query(model.Movement).all()


    used = set()
    for movement in movements:
        all_works_in_movement = set()
        for a_m in movement.artist_movements:
            all_works_in_movement.update([ artwork.thumbnailURL for artwork in a_m.artist.artworks if artwork.thumbnailURL != "" ])
            # for artwork in a_m.artist.artworks:
            #     if artwork.thumbnailURL != "":
            #         possible_list.append(artwork.thumbnailURL)

        possible_unused = all_works_in_movement - used
        if possible_unused:
            url = random.choice(list(possible_unused))
            movement.thumbnailURL = url
            used.add(url)
            print movement.name, " will use", url
        else:
            movement.thumbnailURL = ""
            print movement.name, " has no possible art"


        session.add(movement)
    session.commit()

    eras = model.session.query(model.Era).all()

    for era in eras:
        numArtwork=0
        numArtist=0 
        
        movements_in_era = model.session.query(model.Movement).filter(model.Movement.era_id == era.id).all()
        for movement in movements_in_era:
            numArtist += movement.numArtist
            numArtwork += movement.numArtwork

        era.numArtist = numArtist
        era.numArtwork = numArtwork

        session.add(era)

    session.commit()




def main():
    model.create_tables()
    load_artists(session)
    load_artwork(session)

    loop_directories("./artists")
    add_artist_details()
    add_details()


if __name__ == "__main__":
    main()