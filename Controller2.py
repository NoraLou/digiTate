
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

    # get all artists in a movement

    # artists = model.session.query(model.Artist_movement).filter_by(movementId = 436).limit(5).all()

    # move_artists = []
    # for artist in artists: 
    #     name = artist.artist.name
    #     dates = artist.artist.dates
    #     numArtwork = artist.artist.numArtwork
    #     thumbnailURL = artist.artist.thumbnailURL
    #     print "****************************************************************"
    #     print name, dates, numArtwork, thumbnailURL
    #     id = artist.artist.id
    #     move_artists.append({"name":name, 
    #         "id":id, 
    #         "dates":dates, 
    #         "numArtwork": numArtwork, 
    #         "thumbnailURL": thumbnailURL})

    artists = model.session.query(model.Artist).all()
    for artist in artists:
        numImgs = 0
        numArtwork = len(artist.artworks)
        if numArtwork > 0 :
            for art in range(len(artist.artworks)):
                if artist.artworks[art].thumbnailURL:
                    numImgs += 1
                thumbnailURL = artist.artworks[0].thumbnailURL
        print artist.name
        print numArtwork
        print thumbnailURL
        print numImgs
        print "**********************************************************"   


    page = render_template("index.html")
    return page




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





