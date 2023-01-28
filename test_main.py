import unittest
import requests
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_classify(self):
        test_data = {'pixels': [255, 255, 255, 128, 128, 128, 0, 0, 0]}
        url = "http://localhost:5000/classify"
        response = requests.post(url, json=test_data)
        
        try:
            result = response.json()
            expected_value = 'class_1'
            self.assertEqual(result, expected_value)
            
        except ValueError:
            print("Response content is not valid JSON")

if __name__ == '__main__':
    unittest.main()