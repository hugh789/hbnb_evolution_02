The files in the docker folder have everything you need to create the containers for Ubuntu and MySQL that will be linked together.

I know that the project actually wants everyone to run the Flask + SQLAlchemy files locally in your computer and access the database that is in a container, but since most if not all of you are using Docker to run Ubuntu right now so it won't be easy to do what the project asks because it's rather troublesome to get a docker container running within a docker container lol.

Instead, we'll be using docker compose to stitch everything together. You'll need to copy everything inside the 'docker' folder to a location on your local computer first. Note that the Dockerfile we're using is a modified version of the one from Part 01 with a few changes inside.

After you've copied the files to a location in your local computer, go to that folder and run the following commands:
- docker-compose build
- docker-compose up -d

The Ubuntu container may fail at first... but it will automatically restart and then things will be ok after that. Things take a while to initialise. Give it a short while.

You can then start testing your APIs using localhost:5000