digiTate
========
You can visit digitTATE online  <a href = http://nora-digitate.herokuapp.com/>HERE</a>. <br>It is currently deployed in beta for WebKit browers (Chrome, Safari).

Project Overview

digiTate is an Art History exploration app based on open source data from London’s Tate museum.  As an avid museum goer and technologist, I was excited to discover that the Tate had publicly released meta-data for 70,000 artworks and wanted to make a contribution. Previous treatments of this meta-data were primarily analytic and pre-supposed prior knowlegde of art history. 
I wanted to make this information engaging for all users, and create a visually intuative User Experience that would let the artwork speak for itself. 

DigiTate is a flexible one-page app, that offers users from around the globe a playful, visually intuitive way to explore London’s cultural treasures from the 16th to 20th centuries.

<p align="center">
  <br/>
  <img align="center" src="/screenshots/gif/Best_Screencast.gif" alt="Artist's page">
</p>


Stack
Python, Flask, Javascript, Jquery/Ajax, SQLAlchemy, PostgreSQL, CSS3, HTML5


Building digiTate
digiTate was built in 4 weeks. Roughly, the breakdown of the project, week-by-week was:
-  <b>Week 1</b>
  - Scoping the Project
  - Creating UI Wireframes
  - Exploring APIs, finding data sources
  - Code a working UI prototype
-  <b>Week 2</b>
  - Working with open-source data from Tate
  - Data-munging
  - Using <a href = "http://stedolan.github.io/jq/">JQ</a> to write test queries and understand data.
  - Develop data model
  - Write a seed script to loop through files and build out data model.
-  <b>Week 3</b>
  - Finish building the database
  - Set-up Flask 
  - Build out Ajax requests in Controller
  - Re-seed database with custom data methods to speed availability of data on front-end
-  <b>Week 4</b>
  - Polish out UI functionality, event handler functions
  - Add CSS styling and graphics
  - Add nav-bar with updating breadcrumb display
  - Add comments and clean code to make it more maintainable.
  
Key Features

Front-end
digiTate features a custom-built “fan” navigation system that allows users to visually browse the massive image set quickly.  Layers of information are initially nested on top of each other like a closed fan.  As a user drills-down into a selected time period, layers of the fan animate open and dynamically display data based on the user’s selections.  The responsive front-end structure is based on CSS3’s z-index and flexbox properties.  Ajax allows users to seamlessly switch image sets or rapidly drill-back across fan layers.  Javascript DOM manipulation is thoughtfully employed in the primary navigation functions to optimize browser memory as the fan layers re-stack.

Code snippet of function to drill-back across fan layers.
```
function closePane(pane){

		var paneToExpand = pane.prev();
		var paneToExpand2 = pane;

		$('#breadcrumbs span:last-child')[0].remove();

		pane.find(".fan").empty();
		switch (paneToExpand.attr("id"))
		{
			case ("eraColumn"):
				transitionToEras(pane);
				break;
			default:
				transitionToPrev(paneToExpand2);
				transitionToPrev(paneToExpand);
		}
}
````



###Back-end
In order to achieve digiTate's specific drill-down structure, I had to create a custom data model.  The data-model is seperated from the presentation layer and acts as an internal API.   I built out some of the relationships between historical periods, cultural movements, individual artists, and artworks by using Python's OS module and creating a seed script to loop through the files of json meta-data and extract the specific information needed.  I further optimized this data by creating custom class attributes and methods to enhance the quick availability of data on the front-end.

Code snippet of function to extract data from json files.
```
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
```
Thank you
Thank you for your interest.  Please feel free to be in touch if you have any questions!


  





  
