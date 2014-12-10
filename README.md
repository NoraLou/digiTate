digiTate
========
###Project Overview

digiTate is  Art History exploration app based on open source data from London’s Tate museum.  As an avid museum goer and technologist, I was excited to discover that the Tate had publicly released meta-data for 70,000 artworks and wanted to make a contribution.  This responsive one-page app, offers users from around the globe a playful, visually intuitive way to explore London’s cultural treasures from the 16th to 20th centuries.
 
digiTate features a custom-built “fan” navigation system that allows users to visually browse the massive image set quickly.  Layers of information are initially nested on top of each other like closed fan.  As a user drills-down into a selected time period, layers of the fan animate open and dynamically display data based on the user’s selections.  The responsive front-end structure is based on CSS3’s z-index and flexbox properties.  Ajax allows users to seamlessly switch image sets or rapidly drill-back across fan layers.  Javascript DOM manipulation is thoughtfully employed to optimize browser memory and performance.

I choose a relational database for the backend and crafted the data model to reflect the complex relationships between historical periods, cultural movements, individual artists, and artworks.  Using Python’s OS module I created a program to loop through files of meta-data and extract the specific information I needed to build out these relationships and give the app its specific drill-down structure.  Custom class attributes and methods were created to optimize the quick availability of data on the front-end.

###Stack:
    
Python, Flask, Javascript, Jquery/Ajax, SQLAlchemy, SQLite3, CSS3, HTML5

###

###Screenshots: 
<p align="center">
  <img align="center" src="/screenshots/Github.jpg" alt="Overview layer">
  <img align="center" src="/screenshots/Github3.jpg" alt="Artist's page">
</p>
  

<!--<img src = "/screenshots/gif/750px/18sec_1080.gif">-->

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
 


  
