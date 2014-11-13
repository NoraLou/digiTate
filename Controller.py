from flask import Flask, render_template, redirect, request, flash, session
import model


app = Flask(__name__)
app.secret_key = 'some_secret'

# def size_artwork():
# 	blah blah blah resize the url here!!!

@app.route("/")
def index():

    print("Hello!")

    movements = model.session.query(model.Movement).all()




    # materials = model.session.query(model.Artwork).all()
    # print materials
    # for material in materials:
    #     print material.medium

    #movements[0].artist_movements[0].artist.artworks [0].thumbnailURL

    moves = []
    for movement in movements:
        artistThumbnail = None
        for am in range(len(movement.artist_movements)):
            if len(movement.artist_movements[am].artist.artworks) >= 1:
                #print movement.name + " has at least 1 artist movement"
                for artwork in range(len(movement.artist_movements[am].artist.artworks)):
                    if movement.artist_movements[am].artist.artworks[artwork].thumbnailURL:
                        #print movement.name + " has at least 1 artist movement"
                        artistThumbnail = movement.artist_movements[am].artist.artworks[artwork].thumbnailURL
        moves.append({"name": movement.name, "thumbnailURL": artistThumbnail})
    
    return render_template("index.html", movements = moves)
    


# @app.route("/artists")
# def artists():

#     artistAll = model.session.query(model.Artist).all()

#     return render_template("artists.html", artistAll = artistAll)


# @app.route("/movements")
# def show_movements():
#     # throw out movements with less than 4... order list decsending by the number of artists in the group
#     movements = model.session.query(model.Movement).all()
   
#     return render_template("movements.html", movements = movements)


# @app.route("/eras")
# def eras():
#     eras = model.session.query(model.Era).all()

#     return render_template("eras.html", eras = eras)


# @app.route("/materials")
# def materials():


#     return










if __name__ == "__main__":
    app.run(debug = True)