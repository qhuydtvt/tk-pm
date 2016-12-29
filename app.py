from flask import Flask
import mlab
from mongoengine import *
from flask_restful import Resource, Api, reqparse
import json

mlab.connect()

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
