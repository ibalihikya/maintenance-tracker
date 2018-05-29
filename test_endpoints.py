from app import*
import unittest

expected_response = {
  "user_requests": [
    {
      "userid": 1,
      "description": "small leakage reducing engine pressure",
      "id": 1,
      "title": "leaking pipe"
    },
    {
      "userid": 1,
      "description": "The handle of the front door is broken",
      "id": 2,
      "title": "broken handle"
    },
    {
      "userid" : 1,
      "description": "My car tyre is flat",
      "id": 3,
      "title": "flat tyre"
    }
  ]
}


class RestTests(unittest.TestCase):
    def test_get_all_user_requests(self):
        testobj = app.test_client(self)
        response = testobj.get('/api/v1/users/requests', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), expected_response)

if __name__ == '__main__':
    unittest.main()