import unittest
import json
from app import create_app

class HealthMonitoringTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_submit_data(self):
        data = json.dumps({"temperature": 37.5, "pulse": 75})
        response = self.app.post('/submit_data', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
