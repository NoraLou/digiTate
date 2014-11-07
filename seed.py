import json
from pprint import pprint
import model 
import csv
from model import session


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]


def load_artists(session):
    f1 = unicode_csv_reader(open("artist_data.csv"), delimiter=",")
    # print dir(f1)
    f1.next()

    for row in f1:
        # print dir(row)
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
        artwork.accession_number = row[1]
        artwork.artistRole = row[3]
        artwork.artistId = int(row[4])
        artwork.title = row[5]
        artwork.dateText = row[6]
        artwork.medium = row[7]
        artwork.creditLine = row[8]
        artwork.year = row[9]
        artwork.acquisitionYear = row[10]
        artwork.dimensions = row[11]
        artwork.width = row[12]
        artwork.height = row[13]
        artwork.depth = row[14]
        artwork.units = row[15]
        artwork.inscription = row[16]
        artwork.thumbnailCopyright = row[17]
        artwork.thumbnailURL = row[18]
        artwork.url = row[19]

        session.add(artwork)
    session.commit()


def load_json(file_name):
    file = open(file_name)
    json_text = file.read()
    file.close()

    data = json.loads(json_text)
    pprint(data)

    m = model.Movements()
    am = model.Artist_movements()

    movements_list = data["movements"]
    am.artistId = data["id"] # Artist_movements.artistId # assign unique artId to artist_movements table

    print "****************************"
    print am.artistId

    for i in movements_list:
        # if i["id"] not in m:
        if model.session.query(model.Movements.id).filter(i["id"]).count()<= 0:

            if model.session.query(model.Movements.id).filter(i["id"]).get() != null:

#How to check if something is already in a file.
            m.id = i["id"]
            print i["id"]
        else:
            print "im here already" 

        m.name = i["name"]
        print i["name"]

        session.add(m)
        session.add(am)

    session.commit()


# check movements table to see if movement already exists, get id if yes, add


def main():
    """In case we need this for something"""
    # model.create_tables()

    load_json("ackling-roger-624.json")
    # load_artists(session)
    # load_artwork(session)


if __name__ == "__main__":
    main()