# # app.py
# import os

# from flask import Flask
# from micawber import bootstrap_basic
# # from peewee import SqliteDatabase

# from flask import render_template, request, redirect, jsonify, url_for, flash
# from sqlalchemy import create_engine, asc
# from sqlalchemy.orm import sessionmaker

# from flask import session as login_session
# import random
# import string

# from oauth2client.client import flow_from_clientsecrets
# from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# @app.route('/index')
# 	# return render_template('index.html')

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5004)