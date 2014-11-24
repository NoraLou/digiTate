
from flask import Flask, render_template, redirect, request, flash, session, Response
import model
from sqlalchemy.orm import subqueryload
import json

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
app.secret_key = 'some_secret'

    
@app.context_processor
def utility_processor():
    def thumbnail_format(url, format= 8):
        base_url = url.split("_8.jpg")[0]
        return base_url+"_"+str(format)+".jpg"

    return dict(thumbnail_format=thumbnail_format)

@app.route("/")
def index():

    movements_artists = model.session.query(model.Artist_movement).filter_by(movementId = 436).limit(10).all()

    move_artists = []
    for artist in movements_artists: 
        name = artist.artist.name
        dates = artist.artist.dates
        numArtwork = len(artist.artist.artworks)
        artistId = artist.artist.id
        artworks  = artist.artist.artworks
        print "**********************************************************************"
        print name
        print artworks[0]
        for art in range(len(artworks)):
            # found =  False
            # while thumbnailURL = 0 :
               if artist.artist.artworks[art].thumbnailURL:
                   thumbnailURL = artist.artist.artworks[art].thumbnailURL
                   move_artists.append({"name":name, "id":artistId, "dates":dates, "numArtwork": numArtwork, "thumbnailURL": thumbnailURL})
                   break
        print "**********************************************************************"

    print move_artists


    page = render_template("index.html")
    return page

   




# def add_details():
#     movements = model.session.query(model.Movement).all()

#     for movement in movements: 
#         artistThumbnail = None
#         numArtwork = 0
#         for am in movement.artist_movements:
#             numArtwork += len(am.artist.artworks)
#             if len(am.artist.artworks)>0:
#       # if this movement has an artist with an artwork
#                 for artwork in range(len(am.artist.artworks)):
#                     # for all the artworks assoc w/ movement
#                     if am.artist.artworks[artwork].thumbnailURL: 
#                         artistThumbnail = am.artist.artworks[artwork].thumbnailURL


    # move_artists.append({"name":name, "id":artistId, "dates":dates, "numArtwork": numArtwork, "thumbnailURL": thumbnailURL})


@app.route("/api/movements", methods=['GET','POST'])
def load_movments():

    era = request.args.get('data')
    eras_movements = model.session.query(model.Movement).filter_by(era_id = era).all()
    json_movement_objs = [movement.convert_to_JSON()for movement in eras_movements]

    # [movement.convert_to_JSON().thumbnailURL for movement in eras_movements]
        # ls[]
        # for i in ls ; do something
        # ls.append( i w/ something done)
    
    return Response(json.dumps(json_movement_objs), mimetype="text/json")


@app.route("/api/artwork",methods=['GET','POST'])
# get artwork for a given movement
def load_artwork():
    movement = request.args.get('data')
    print movement

    movements_artwork = model.session.query(model.Artist_movement).filter_by(movementId = movement).all()
    artwork_ls = []
    for am in movements_artwork:
        current_artist = am.artistId
        artwork = model.session.query(model.Artwork).filter(model.Artwork.artistId == current_artist)
        for piece in artwork:

            artwork_ls.append({"thumbnailURL":piece.thumbnailURL, "id":piece.id, "name":piece.title, "artistId":piece.artistId})

    return Response(json.dumps(artwork_ls), mimetype="text/json")


# @app.route("/api/artists", methods= ['GET','POST'])
# # get artists for a given movement
# def load_artists():

#     movement = request.args.get('data')

#     movements_artists = model.session.query(model.Artist_movement).filter_by(movementId = movement).limit(5).all()

#     move_artists = []
#     for artist in movements_artists: 
#         name = artist.artist.name
#         dates = artist.artist.dates
#         numArtwork = len(artist.artist.artworks)
#         artistId = artist.artist.id





#         move_artists.append({"name":name, "id":artistId, "dates":dates, "numArtwork": numArtwork, "thumbnailURL": thumbnailURL})

#     return Response(json.dumps(move_artists), mimetype="text/json")


# @app.route("/api/artwork", methods = ['GET','POST'])
# # get artwork for a given artist
# def load artwork():


if __name__ == "__main__":
    app.run(debug = True)





