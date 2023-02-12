import unittest
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')

class FlaskMicroserviceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_current_time(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(response.data.decode('utf-8'), current_time)

if __name__ == '__main__':
    unittest.main()

