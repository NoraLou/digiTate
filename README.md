digiTate
========
###Project Overview

digiTate is  Art History exploration app based on open source data from London’s Tate museum.  As an avid museum goer and technologist, I was excited to discover that the Tate had publicly released meta-data for 70,000 artworks and wanted to make a contribution. Previous treatments of this meta-data were primarily analytic and pre-supposed prior knowlegde of art history. I wanted to make this information accessible and engaging for all users. DigiTate is a responsive one-page app, that offers users from around the globe a playful, visually intuitive way to explore London’s cultural treasures from the 16th to 20th centuries.

###Front-end
digiTate features a custom-built “fan” navigation system that allows users to visually browse the massive image set quickly.  Layers of information are initially nested on top of each other like a closed fan.  As a user drills-down into a selected time period, layers of the fan animate open and dynamically display data based on the user’s selections.  The responsive front-end structure is based on CSS3’s z-index and flexbox properties.  Ajax allows users to seamlessly switch image sets or rapidly drill-back across fan layers.  Javascript DOM manipulation is thoughtfully employed in the primary navigation functions to optimize browser memory as the fan layers re-stack.

###Back-end
In order to achieve digiTate's specific drill-down structure, I had to create a custom data model.  I built out the many relationships between historical periods, cultural movements, individual artists, and artworks by creating a seed script to loop through the files of json meta-data and extract the specific information I needed.  I further optimized this data by creating custom class attributes and methods to enhance the quick availability of data on the front-end.

###Stack
    
Python, Flask, Javascript, Jquery/Ajax, SQLAlchemy, PostgreSQL, CSS3, HTML5

###

###Screenshots: 
<p align="center">
  <img align="center" src="/screenshots/Github.jpg" alt="Overview layer">
  <br/>
  <br/>
  <img align="center" src="/screenshots/gif/Best_Screencast.gif" alt="Artist's page">
</p>
  



###Installation 

1. Clone this repo on your local machine.

  ```
  https://github.com/NoraLou/digiTate.git
  ```
2. Create a python virtual environment:

  ```
  virtualenv env
  ```
3. Activate the virtual environment:

  ```
  source env/bin/activate
  ```
4. Install the requirements:

  ```
  pip install -r requirements.txt
  ```

6. Start the program by typing:
  ```
  python Controller.py
  ```
  into your terminal. 

7.  After Controller.py runs successfully, point your browser to http://localhost:5000/ and get started!
 


  
