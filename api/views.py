from flask import Flask, jsonify, request, Response, json
from api import app

user_requests = []


@app.route('/api/v1/users/requests', methods=['GET'])
def get_all_user_requests():
    response = jsonify({'user_requests':user_requests})
    return response

@app.route('/api/v1/users/requests/<int:requestId>', methods=['GET'])
def get_specific_user_request(requestId):
    ur = {}
    for u_request in user_requests:
        if u_request['id'] == requestId :
            ur = u_request
            break
    if len(ur) == 0 :
        response = jsonify({'':''})
        response.status_code = 404
    else: 
        response = jsonify({'user_request': ur})
    
    return response

@app.route('/api/v1/users/requests', methods=['POST'])
def create_user_request():
    ur =  request.get_json(force=True)
    input_dictionary = {
        'userid' : ur['userid'],
        'id' : len(user_requests) + 1,
        'title' : ur['title'],
        'description' : ur['description'],
        'date_created' : ur['date_created'],
        'date_modified' : ur['date_modified'],
        'status' : ur['status']}

    user_requests.append(input_dictionary)
    
    response = jsonify(input_dictionary)
    response.status_code = 201
    return response

@app.route('/api/v1/users/requests/<int:requestId>', methods=['PUT'])
def modify_request(requestId):
    data_posted =  request.get_json(force=True)
    ur = {}
    for u_request in user_requests:
        if u_request['id'] == requestId :
            ur = u_request
            break
    ur['title'] = data_posted['title'] 
    response = jsonify(ur)
    return response

@app.route('/api/v1/users/requests', methods=['DELETE'])
def delete_all_requests():
    user_requests.clear()
    response = jsonify({'user_requests':user_requests})
    response.status_code = 204
    return response
   
    

if __name__ == '__main__':
         app.run()
