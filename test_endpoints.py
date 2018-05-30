from app import app
import unittest
import json



u_requests ={
        "user_requests":[
		          {'userid': 1,
                  'id': 1,
                  'title': 'leaking pipe',
                  'description': 'small leakage reducing engine pressure',
                  'date_created': 'Wed, 30 May 2018 14:00:00 GMT',
                  'date_modified': 'Wed, 30 May 2018 15:00:00 GMT',
                  'status': 'pending'},
                 {'userid': 1,
                  'id': 2,
                  'title': 'broken handle',
                  'description': 'The handle of the front door is broken',
                  'date_created': 'Wed, 30 May 2018 14:00:00 GMT',
                  'date_modified': 'Wed, 30 May 2018 15:00:00 GMT',
                  'status': 'pending'},
                 {'userid': 1,
                  'id': 3,
                  'title': 'flat tyre',
                  'description': 'My car tyre is flat',
                  'date_created': 'Wed, 30 May 2018 14:00:00 GMT',
                  'date_modified': 'Wed, 30 May 2018 15:00:00 GMT',
                  'status': 'pending'}
				  ]
				  }

# this should not be a json array
u_request = {
    "user_request":
		          {'userid': 1,
                              'id': 1,
                              'title': 'leaking pipe',
                              'description': 'small leakage reducing engine pressure',
                              'date_created': 'Wed, 30 May 2018 14:00:00 GMT',
                              'date_modified': 'Wed, 30 May 2018 15:00:00 GMT',
                              'status': 'pending'}
}

u_entry = {
    'userid': 1,
    'title': 'leaking pipe',
    'description': 'small leakage reducing engine pressure',
    'date_created': 'Wed, 30 May 2018 14:00:00 GMT',
    'date_modified': 'Wed, 30 May 2018 15:00:00 GMT',
    'status': 'pending'
}

u_request2 = {
    "user_request":
		          {'userid': 1,
                              'id': 4,
                              'title': 'leaking pipe',
                              'description': 'small leakage reducing engine pressure',
                              'date_created': 'Wed, 30 May 2018 14:00:00 GMT',
                              'date_modified': 'Wed, 30 May 2018 15:00:00 GMT',
                              'status': 'pending'}
}


class RestTests(unittest.TestCase):
    def test_get_all_user_requests(self):
        testobj = app.test_client(self)
        response = testobj.get('/api/v1/users/requests', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), u_requests)

    def test_get_specific_user_request(self):
            testobj = app.test_client(self)
            response = testobj.get('/api/v1/users/requests/1', content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), u_request)

    def test_get_non_existent_user_request(self):
            testobj = app.test_client(self)
            response = testobj.get('/api/v1/users/requests/15', content_type='application/json')
            self.assertEqual(response.status_code, 404)
            #self.assertEqual(response.get_json(), expected_response)

    def test_create_request(self):
        testobj = app.test_client(self)
        response = testobj.post('/api/v1/users/requests', json=u_entry)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), u_request2)



if __name__ == '__main__':
    unittest.main()
