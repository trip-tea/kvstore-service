import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import app


class KeyValueStoreAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_existing_key(self):
        # Set the key-value pair before retrieving the value
        response = self.app.post('/set', json={'key': 'key1', 'value': 'value1'})
        self.assertEqual(response.status_code, 200)

        # Retrieve the value
        response = self.app.get('/get/key1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'key1': 'value1'})

    def test_get_non_existing_key(self):
        response = self.app.get('/get/nonexistingkey')
        self.assertEqual(response.status_code, 404)
        # Add your assertions or further test logic here

    def test_set_key_value(self):
        response = self.app.post('/set', json={'key': 'key2', 'value': 'value2'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        # Add your assertions or further test logic here

    def test_search_with_prefix(self):
        response = self.app.get('/search?prefix=abc')
        self.assertEqual(response.status_code, 200)
        # Add your assertions or further test logic here

    def test_search_with_suffix(self):
        response = self.app.get('/search?suffix=-1')
        self.assertEqual(response.status_code, 200)
        # Add your assertions or further test logic here

    def test_invalid_route(self):
        response = self.app.get('/invalid-route')
        self.assertEqual(response.status_code, 404)
        # Add your assertions or further test logic here


if __name__ == '__main__':
    unittest.main()
