# Real-Time Health Monitoring System using IoT and Python

This project simulates a real-time health monitoring system that collects patient data (temperature and pulse) from an IoT device and displays it on a web dashboard. Built using **Python, Flask**, and **MongoDB**, it showcases embedded concepts, API development, and IoT simulation.

---

## 🚀 Features

- Real-time health data collection via REST API
- IoT device simulator that sends data every 5 seconds
- Flask-based web dashboard to monitor status
- MongoDB integration to store health records
- Unit testing for API endpoints

---

## 🛠️ Technologies Used

- Python 3.x  
- Flask  
- MongoDB  
- HTML/CSS  
- REST API  
- Requests (IoT simulation)  
- PyMongo  
- Unittest (for testing)

---

## 📁 Project Structure

```
RealTimeHealthMonitoringSystem/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── database.py
│   ├── templates/
│   │   └── index.html
│   └── static/css/
│       └── style.css
│
├── iot_device/
│   └── simulator.py
│
├── tests/
│   └── test_api.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/RealTimeHealthMonitoringSystem.git
cd RealTimeHealthMonitoringSystem
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask server

```bash
python run.py
```

Access the dashboard at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🤖 Simulate IoT Device

Run the simulator in a new terminal:

```bash
python iot_device/simulator.py
```

This will start sending random temperature and pulse data every 5 seconds to your Flask API.

---

## 🧪 Run Tests

```bash
python -m unittest discover tests
```

---

## 📊 Example Data Sent by IoT Simulator

```json
{
  "temperature": 37.4,
  "pulse": 78
}
```

---

## 👨‍⚕️ Use Case

This project demonstrates how IoT devices can be integrated with a lightweight server to monitor patient vitals in real time. It simulates a real-world healthcare application and can be extended with real sensors and front-end graphs.

---

## 📃 License

This project is for educational purposes and personal use only.
