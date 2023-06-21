import unittest
import json
from flask import Flask
from app import app

class KeyValueStoreAPITestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_existing_key(self):
        app.store = {'key1': 'value1'}
        response = self.client.get('/get/key1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'key1': 'value1'})

    def test_get_non_existing_key(self):
        response = self.client.get('/get/nonexistingkey')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data, {'error': 'Key not found'})

    def test_set_key_value(self):
        response = self.client.post('/set', json={'key': 'key2', 'value': 'value2'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'message': 'Key-value pair set successfully'})

    def test_search_with_prefix(self):
        app.store = {'abc-1': 'value1', 'abc-2': 'value2', 'xyz-1': 'value3', 'xyz-2': 'value4'}
        response = self.client.get('/search?prefix=abc')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'keys': ['abc-1', 'abc-2']})

    def test_search_with_suffix(self):
        app.store = {'abc-1': 'value1', 'abc-2': 'value2', 'xyz-1': 'value3', 'xyz-2': 'value4'}
        response = self.client.get('/search?suffix=-1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'keys': ['abc-1', 'xyz-1']})

if __name__ == '__main__':
    unittest.main()
