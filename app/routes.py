from app import app
import urllib.request
import json
from flask import jsonify
import datetime

all = {}
now = datetime.datetime.now()

@app.route('/')
@app.route('/index')
def index():
    with urllib.request.urlopen("http://192.168.1.121/radar/dump1090-fa/data/aircraft.json") as url:
        aircraft = json.loads(url.read().decode())
        print(aircraft['now'])
        s = float(aircraft['now'])
        #print (datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f'))

        all[aircraft['now']] = aircraft
        print (len(all))
        return jsonify(aircraft)


@app.route('/listall')
def listall():
        return jsonify(all)
