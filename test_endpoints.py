from app import app
from file_util import*
import unittest


class RestTests(unittest.TestCase):

    def setUp(self):
        tester = app.test_client(self)
        tester.post('/api/v1/users/requests', json=user_entry_data)
        tester.post('/api/v1/users/requests', json=user_entry2_data)
   

    def tearDown(self):
        tester_b = app.test_client(self)
        tester_b.delete('/api/v1/users/requests')

    def test_get_all_user_requests(self):
        self.maxDiff = None
        testobj = app.test_client(self)
        response = testobj.get('/api/v1/users/requests', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), user_requests_data)

    def test_get_specific_user_request(self):
        testobj = app.test_client(self)
        response = testobj.get('/api/v1/users/requests/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), user_request_data)

    def test_get_non_existent_user_request(self):
        testobj = app.test_client(self)
        response = testobj.get('/api/v1/users/requests/15', content_type='application/json')
        self.assertEqual(response.status_code, 404)
        #self.assertEqual(response.get_json(), expected_response)
  
    
    def test_create_request(self):
        testobj = app.test_client(self)
        response = testobj.post('/api/v1/users/requests', json=user_entry3_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), user_request2_data)

    def test_modify_request(self):
        testobj = app.test_client(self)
        response = testobj.put('/api/v1/users/requests/2', json=user_request_modify_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), user_request_modify_result_data)


if __name__ == '__main__':
    unittest.main()
