from flask import Flask, jsonify, request, Response, json
app= Flask(__name__)


user_requests = [{'userid':1,
                  'id': 1,
                   'title': 'leaking pipe',
                    'description': 'small leakage reducing engine pressure'},
                {'userid':1,
                    'id': 2,
                   'title': 'broken handle',
                    'description': 'The handle of the front door is broken'},
                    {'userid':1,
                        'id': 3,
                   'title': 'flat tyre',
                    'description': 'My car tyre is flat'}]
 

@app.route('/api/v1/users/requests', methods = ['GET'])
def get_all_user_requests():
    resp = jsonify({'user_requests' : user_requests})
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run()