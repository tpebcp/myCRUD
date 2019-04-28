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
        print(post_data)
        # setup a warning reponse if input is not good
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data: 
            print("from not post_data")
            return response_object, 400

        username = post_data.get('username')
        event = post_data.get('event')

        if not username or not event:
            print("from not username or not event")
            return response_object, 400

        db.session.add(pocketMoney(username=username, event=event))
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': f'event {event} was added!'
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
