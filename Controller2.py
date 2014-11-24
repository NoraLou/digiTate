
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

# def login():
# def signout():
# def lightbox():

@app.route("/")
def index():

    # get number of artists, artworks, per movement
    # movements = model.session.query(model.Movement).all()
    # for move in movements:
    #     print "************************************"
    #     print move.name
    #     print move.era.
    #     print move.numArtist
    #     print move.numArtwork

    page = render_template("index.html",)
    return page

@app.route("/api/movements", methods=['GET','POST'])
def load_movments():

    era = request.args.get('data')
    eras_movements = model.session.query(model.Movement).filter_by(era_id = era).all()
    json_movement_objs = [movement.convert_to_JSON()for movement in eras_movements]

                          # [movement.convert_to_JSON().thumbnailURL for movement in eras_movements]
    print json_movement_objs

        # ls[]
        # for i in ls ; do something
        # ls.append( i w/ something done)
    
    return Response(json.dumps(json_movement_objs), mimetype="text/json")


# get artwork for a given movement
@app.route("/api/artwork",methods=['GET','POST'])
def load_artwork():
    movement = request.args.get('data')
    print movement

    movements_artwork = model.session.query(model.Artist_movement).filter_by(movementId = movement).all()
    artwork_ls = []
    for am in movements_artwork:
        current_artist = am.artistId
        artwork = model.session.query(model.Artwork).filter(model.Artwork.artistId == current_artist)
        for piece in artwork:

            artwork_ls.append({"thumbnailURL":piece.thumbnailURL, "id":piece.id, "name":piece.title, "artistId":piece.artistId} )
    print artwork_ls 

    return Response(json.dumps(artwork_ls), mimetype="text/json")

#get artists for a given movment
@app.route("/api/artists", methods= ['GET','POST'])
def load_artists():
    movement = request.args.get('data')
    print movement

    movements_artists = model.session.query(model.Artist_movement).filter_by(movementId = movement).limit(5).all()
    print movements_artists

    # eras = model.session.query(model.Era).all()r

    # for era in eras:
    #     print "*****************"
    #     print era.id
    #     print era.name
    #     movements_in_era_easy = model.session.query(model.Movement).filter(model.Movement.era_id == era.id).all()
    #     print movements_in_era_easy

    #     for movement in movements_in_era_easy:
    #         print movement.name

    # current_era = model.session.query(model.Era).filter_by(id = 19376).all()
    
    # moves_in_current_era = model.session.query(model.Movement).filter(model.Movement.era_id == 19376).all()
    # print moves_in_current_era

    # for i in moves_in_current_era: 
    #     print i.name
    #     print i.numArtist
    #     print i.numArtwork
    # print i.artist_movements.artistId



    # Find era artwork 
    # eras = model.session.query(model.Era).all()

    # for era in eras:
    #     print "*****************"
    #     print era.id
    #     print era.name
    #     print 

    #     movements_in_era_easy = model.session.query(model.Movement).filter(model.Movement.era_id == era.id).all()
    #     print movements_in_era_easy

    #     sixteenthcentury = model.session.query(model.Era).filter_by(id =289 ).all()

    # find artwork in a given era, movement, artist#

    # sixteenthcentury = model.session.query(model.Movement).filter(model.Movement.era_id == 350
    #     ).all()
    #     # print  sixteenthcentury

    # for move in sixteenthcentury:
    #     print "************************************************************"
    #     print move.name,  "numArtwork:", move.numArtwork, "numArtist:", move.numArtist
    #     mam = move.artist_movements
        # for am in mam:
        #     print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        #     print am.artist.name
        #     print am.artistId
        #     current_artist = am.artistId
        #     artwork = model.session.query(model.Artwork).filter(model.Artwork.artistId == current_artist)
        #     for piece in artwork:
        #         print piece.thumbnailURL


    # def imgs_from_movement(movement_object)
       
        


# @app.route("/")
# def show_eras():

#     print("Hello!")

#     eras = model.session.query(model.Era).options(subqueryload('movements')).all()

#     return render_template("eras.html", eras = eras)

# @app.route("/show/eras_movements")
# def eras_movements(era):
#     movements_in_era = model.session.query(model.Artist_movement).filter(model.Artist_movement.era_id == era.id).group_by(model.Artist_movement.movementId).all()
#     return render_template("eras_movements.html", movements_in_era = movements_in_era)



# @app.route("/show/<int:movement>")
# def movement(movement):
#     display_artwork = model.session.query(model.Movement).filter_by(id = 419).one()

#     print display_artwork
#     print display_artwork

#     #get 10 images from the db based on "movement"
#     # pass data retrieved from DB to a template
#     #return render_template(html file, data from database)
#     return render_template("show_M.html")

# @app.route("/show/movements_artists")
# def movements_artists(movement):

#     pass

# @app.route("/show/artist")
# def artist(artist):


#     pass

if __name__ == "__main__":
    app.run(debug = True)





