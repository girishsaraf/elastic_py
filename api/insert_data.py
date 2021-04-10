from flask_app import app
from api.elastic_test import connect_elasticsearch
from flask import request
from flask import jsonify

es = connect_elasticsearch()

@app.route('/add_user', methods=['POST'])
def add_user():
    user_id = request.form['id']
    first_name = request.form['fname']
    last_name = request.form['lname']
    job = request.form['job']

    user_obj = {
        'id': user_id,
        'name': '{} {}'.format(first_name, last_name),
        'occupation': '{}'.format(job)
    }

    result = es.index(index='user', id=user_id, body=user_obj, request_timeout=30)
    return jsonify(result)

@app.route('/update_user', methods=['POST'])
def update_user():
    user_id = request.form['id']
    param = request.form['param']
    new_val = request.form['new_value']

    update_dict = {
        'doc':{
            param: new_val
        }
    }

    response = es.update(index='user', id=user_id, body=update_dict)
    return jsonify(response)