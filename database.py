from pymongo import MongoClient

def init_db(app):
    client = MongoClient("mongodb://localhost:27017/")
    db = client['health_monitoring']
    app.config['DB'] = db
