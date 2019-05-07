#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import urllib.request, json 
with urllib.request.urlopen("http://192.168.2.111/dump1090-fa/data/aircraft.json") as url:
    data = json.loads(url.read().decode())
    print(data)
