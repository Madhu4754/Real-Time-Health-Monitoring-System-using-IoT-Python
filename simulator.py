import requests
import time
import random

url = "http://127.0.0.1:5000/submit_data"

while True:
    data = {
        "temperature": round(random.uniform(36.0, 39.0), 2),
        "pulse": random.randint(60, 100)
    }
    try:
        response = requests.post(url, json=data)
        print(f"Sent data: {data}, Response: {response.status_code}")
    except:
        print("Failed to send data.")
    time.sleep(5)
