from flask import Blueprint, render_template, request, jsonify
import datetime
from .models import insert_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit_data', methods=['POST'])
def submit_data():
    data = request.get_json()
    insert_data(data)
    return jsonify({"status": "success"}), 200
