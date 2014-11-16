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

    for era in eras:
        moves_in_era = []
        numArtwork=0
        numArtist=0 
        print "*****************"
        print era.id
        print era.name
        movements_in_era = model.session.query(model.Artist_movement).filter(model.Artist_movement.era_id==era.id).group_by(model.Artist_movement.movementId).all()
        for artist_move in movements_in_era:
            moves_in_era.append([artist_move.movement.name])
            numArtist += artist_move.movement.numArtist
            numArtwork += artist_move.movement.numArtwork
        print moves_in_era
        print "numArtwork", numArtwork
        print "numArtist", numArtist

       
         

    return render_template("index.html")


@app.route("/eras")
def show_eras():

    print("Hello!")

    eras_w_moves = []
    eras = model.session.query(model.Era).all()
    for era in eras:
        print era.name
        movements_in_era = model.session.query(model.Artist_movement).filter(model.Artist_movement.era_id==era.id).group_by(model.Artist_movement.movementId).all()
        for m in movements_in_era:
            print m.movementId
            print m.movement.name
        
        # eras_w_moves.append({"era": era.name, "movements_in_era":[movements_in_era]})
        # print"*************"
        # print"*************"
        # print eras_w_moves
        


    # get a list of eras and display an image for each one. 
    # each image links to all the distinct movements.
    # each movement links to all artis
    return render_template("eras.html", eras_w_moves = eras_w_moves)
    

@app.route("/show/eras_movements")
def eras_movements(era_id):
    movements_in_era = model.session.query(model.Artist_movement).filter(model.Artist_movement.era_id==era.id).group_by(model.Artist_movement.movementId).all()
    return render_template("eras_movements", movements_in_era = movements_in_era
   
# @app.route("/movements")
# def show_movements():


#     movements = model.session.query(model.Movement).all()
#     return render_template("movements.html", moves = movements)


@app.route("/show/movement")
def artists(movement_id):
    display_artwork = model.session.query(model.Movement).filter_by(id = 419).one()

    print display_artwork
    print display_artwork

    #get 10 images from the db based on "movement"
    #pass data retrieved from DB to a template
    #return render_template(html file, data from database)
    return render_template("show_M.html")

if __name__ == "__main__":
    app.run(debug = True)