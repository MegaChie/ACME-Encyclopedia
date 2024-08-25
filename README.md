# ACME-Encyclopedia
  The encyclopedia by developers to developers.<br>

## Install packages needed
  The web app runs on flask for its backend, MongoDB for the database,
  and LibreTranslate as a translation provider for the articles.<br>

  While on the time of deployment evrey component of was hosted on a
  separate machine (plus one for the frontend), you could host all of it
  on one machine as long as you remember to edit the port number of each part.
  This will make so there in no warning about used ports.<br>

  Please note that it is assumed that Python3 with pip3 are already installed
  on your machine. Make updates if necessarly.<br>

  To install MongoDB and LibreTranslate, simpily run the file
  named "dependencies" available at the root of the repo. After which it will
  start to install all the libraries needed to run the the backend.<br>
  Running the file will start to by installing MongoDB, Docker, and lastly
  LibreTranslate. After which LibreTranslate will start and uses port 5000,
  MongoDB will start running on port 27017.<br>

## Running the backend
  After the installation, start the backend by executing
  `cd Back-end; python3 -m api.v1.app.app; cd ..`.<br>

## Running the frontend
  Built in NodeJS's react and HTML, the frontend is a dynamic webpage that
  utilises the backend to pull data from the database and render the page.<br>

### Installing neccesties
  This project utilies Node, so the machine needs to install it
  before you are able to preceed. If your machine does not have Node installed,
  running the "dependencies" would have already installed it for you.<br>

  After that, run `cd Front-end; npm install; cd..` command to install
  any library that is needed to start the frontend component.<br>

  After which, you need to direct your web-server service
  (eg. Nginx, Gunicorn... etc.) to serve the page to your
  desired location of the domain.
