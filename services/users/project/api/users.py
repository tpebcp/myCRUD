# services/users/project/api/users.py


from flask import Blueprint, request
from flask_restful import Resource, Api

from project import db
from project.api.models import pocketMoney


users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'GOOD!'
    }

class EventList(Resource):
    def post(self):
        post_data = request.get_json()
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(str(post_data))
        errorFile.close()
        #print(post_data)
        # setup a warning reponse if input is not good
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data: 
            print("from not post_data")
            return response_object, 400

        username = post_data.get('username')
        activities = post_data.get('activities')
        money = post_data.get('money')

        if not username or not activities:
            print("from not username or not activities")
            return response_object, 400

        db.session.add(pocketMoney(username=username, activities=activities, money=money))
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': f'activity {activities} was added!'
        }
        return response_object, 201

    def get(self):
        """Get all events"""
        response_object = {
            'status': 'success',
            'data': {
                'events': [ record.to_json() for record in pocketMoney.query.all()]
            }
        }
        return response_object, 200

api.add_resource(UsersPing, '/users/ping')
api.add_resource(EventList, '/events')
