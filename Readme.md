# License Plate Recognition Flask App
## Introduction
This is a website using Flask to provide an interface for License Plate Recognition
## Installation
### Using docker-compose
Run the following commands
```
docker-compose build
docker-compose up
```
If you want to change the code and run the web again
```
docker-compose up --build
```
### Another way to install in case of errors when building image
Run the following commands
```
cd flask
pip install -r requirements.txt
python run.py
```
The web will be in [localhost](http://127.0.0.1:8080/)