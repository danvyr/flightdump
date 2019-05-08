#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import urllib.request, json 
import datetime
from flask import Flask, jsonify

app = Flask(__name__)


# aircraft = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web', 
#         'done': False
#     }
# ]

# @app.route('/todo/api/v1.0/aircraft', methods=['GET'])
# def get_aircraft():
    
#     with urllib.request.urlopen("http://192.168.2.111/dump1090-fa/data/aircraft.json") as url:
#         aircraft = json.loads(url.read().decode())
#         print(aircraft['now'])
#         s = float(aircraft['now'])
#         print (datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f'))
#         return jsonify({'aircraft': aircraft})

# if __name__ == '__main__':
#     app.run(debug=True)



tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
