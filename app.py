from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)


user_requests = [{'userid': 1,
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
                  'status': 'pending'}]
                  


@app.route('/api/v1/users/requests', methods=['GET'])
def get_all_user_requests():
    resp = jsonify({'user_requests': user_requests})
    #resp.status_code = 200
    return resp

@app.route('/api/v1/users/requests/<int:requestId>', methods=['GET'])
def get_specific_user_request(requestId):
    return jsonify({'':''})

@app.route('/api/v1/users/requests', methods=['POST'])
def create_user_request():
    return jsonify({'':''})
    

if __name__ == '__main__':
         app.run()
