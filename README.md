## Software Development Processes Project - Group 3

Students: Cecilia Machado Alves and Peter Bader

This project is part of the MIO program from FHTW. The aim of this project is to practice the methods of current software development processes.

The project consists of a docker image that runs a python code generating a Flask application where sensor data from the RockPi 4 SE is displayed. 
The links on the web application display CPU temperature (/cpu/temp) and disk usage (/disk/usage). Also, through "/cpu/temp/error" it is possible to check if the temperature is considered fine or too hot.

A Continuous Integration workflow includes linting, testing and generation of docker image before it is pulled to GitHub and DockerHub repository. Also, optimization of pull requests are done by storing previously generater images in cache, to speed up future pull requests.