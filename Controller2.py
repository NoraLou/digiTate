
from flask import Flask, render_template, redirect, request, flash, session
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

    print("Hello!")

    page = render_template("index.html",)
    return page

@app.route("/test", methods=['GET','POST'])
def load_images():

    # get the era name that is being being clicked on from ajax json 
    era = request.json['data']

    # get all the movements for the era, get a piece of representative artwork 
    eras_movements = model.session.query(model.Movement).filter_by(era_id = era).limit(5).all()
    # still need to write the getting arwork bit!!!!!!!!!!!!!!!!!!
    print eras_movements
    
    return json.dumps(eras_movements.convert_to_JSON())







    # eras = model.session.query(model.Era).all()

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
    #     for am in mam:
    #         print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    #         print am.artist.name
    #         print am.artistId
    #         current_artist = am.artistId
    #         artwork = model.session.query(model.Artwork).filter(model.Artwork.artistId == current_artist)
    #         for piece in artwork:
    #             print piece.thumbnailURL


    # def imgs_from_movement(movement_object)
       
        

    


@app.route("/")
def show_eras():

    print("Hello!")

    eras = model.session.query(model.Era).options(subqueryload('movements')).all()

    return render_template("eras.html", eras = eras)

@app.route("/show/eras_movements")
def eras_movements(era):
    movements_in_era = model.session.query(model.Artist_movement).filter(model.Artist_movement.era_id == era.id).group_by(model.Artist_movement.movementId).all()
    return render_template("eras_movements.html", movements_in_era = movements_in_era)



@app.route("/show/<int:movement>")
def movement(movement):
    display_artwork = model.session.query(model.Movement).filter_by(id = 419).one()

    print display_artwork
    print display_artwork

    #get 10 images from the db based on "movement"
    # pass data retrieved from DB to a template
    #return render_template(html file, data from database)
    return render_template("show_M.html")

@app.route("/show/movements_artists")
def movements_artists(movement):

    pass

@app.route("/show/artist")
def artist(artist):


    pass

if __name__ == "__main__":
    app.run(debug = True)





