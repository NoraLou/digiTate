
from flask import Flask, render_template, redirect, request, flash, session
import model
from operator import itemgetter
from sqlalchemy.orm import subqueryload

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

    eras = model.session.query(model.Era).all()

    for era in eras:
        print "*****************"
        print era.id
        print era.name
        # movements_in_era_easy = model.session.query(model.Movement).filter(model.Movement.era_id == era.id).all()
        
        

    return render_template("index.html")


@app.route("/eras")
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





