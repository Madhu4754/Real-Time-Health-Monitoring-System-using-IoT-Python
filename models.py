from flask import current_app
import pymongo

def insert_data(data):
    db = current_app.config['DB']
    data['timestamp'] = datetime.datetime.now()
    db.health_data.insert_one(data)
