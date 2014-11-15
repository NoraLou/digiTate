from flask import Flask, render_template, redirect, request, flash, session
import model
from operator import itemgetter
from sqlalchemy import distinct


app = Flask(__name__)
app.secret_key = 'some_secret'

# def size_artwork():
# 	blah blah blah resize the url here!!!

@app.route("/")
def index():

    print("Hello!")

    eras = model.session.query(model.Era).all()

    # movements_eras = eras.artist_movements(distinct(artist_movements.movementId)).all()

    # movements_eras = model.session.query(model.Er)


    #print eras
    
    for era in eras:
        #movements_in_era = model.session.query(distinct(model.Artist_movement))
        #print movements_in_era
        print era.id
        movements_in_era = model.session.query(model.Artist_movement).filter(model.Artist_movement.era_id==era.id).group_by(model.Artist_movement.movementId).all()
        for mie in movements_in_era:
            print mie.movement.name

    # for era in eras:
    #       artistThumbnail = None
    #       numArtwork = 0
    #       for movement in era.artist_movements:
    #         print dir(era.artist_movements)



    return render_template("index.html")


@app.route("/eras")
def show_eras():

    print("Hello!")

    # get a list of eras and display an image for each one. 
    # each image links to all the distinct movements.
    # each movement links to all artists

    eras = model.session.query(model.Era).limit(5)


    return render_template("eras.html", eras = eras)

    
@app.route("/all_movements")
def show_movements():

    movements = model.session.query(model.Movement).all()

    # moves = []
    # for movement in movements: 
    #     artistThumbnail = None
    #     numArtwork = 0
    #     for am in movement.artist_movements:
    #         if len(am.artist.artworks)>0:
    #         # if this movement has an artist with an artwork
    #             for artwork in range(len(am.artist.artworks)):
    #                 # for all the artworks assoc w/ movement
    #                 if am.artist.artworks[artwork].thumbnailURL: 
    #                     artistThumbnail = am.artist.artworks[artwork].thumbnailURL
    #                     numArtwork += len(am.artist.artworks)


    #     moves.append({"name": movement.name, "thumbnailURL": artistThumbnail, 
    #                   "numArtist": len(movement.artist_movements), "numArtwork":numArtwork,
    #                   "movementId": movement.id})

    # moves_sorted = sorted(moves, key= itemgetter("numArtwork"))

    return render_template("all_movements.html", moves = movements)


@app.route("/show/<int:movement>")
def artists(movement):
    display_artwork = model.session.query(model.Movement).filter_by(id = 419).one()

    print display_artwork
    print display_artwork

    #get 10 images from the db based on "movement"
    # pass data retrieved from DB to a template
    #return render_template(html file, data from database)
    return render_template("show_M.html")

if __name__ == "__main__":
    app.run(debug = True)