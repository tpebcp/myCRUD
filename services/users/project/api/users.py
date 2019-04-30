# services/users/project/api/users.py


from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db
from project.api.models import pocketMoney
import logging

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

logging.basicConfig(
        level=logging.DEBUG, 
        filename="service.users.log",
        format=' %(asctime)s - %(levelname)s - %(message)s'
)

class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'GOOD!'
    }

class EventList(Resource):
    def post(self):
        post_data = request.get_json()
        logging.debug(str(post_data))
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
        disabled = post_data.get('disabled')

        if not username or not activities:
            print("from not username or not activities")
            return response_object, 400

        db.session.add(pocketMoney(username=username, activities=activities, money=money,
                                   disabled=disabled))
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


class Event(Resource):

    def delete(self, event_id):
        """Delete a specified event"""
        response_object = {
            'status': 'fail',
            'message': 'Event does not exist'
        }
        try:
            queryResult= pocketMoney.query.filter_by(id=int(event_id)).first()
            logging.debug(str(queryResult))
            if not queryResult:
                logging.debug("the event user specified was not found, aborting record deletion.")
                return response_object, 404
            else:
                db.session.delete(queryResult)
                db.session.commit()
                response_object = {
                    'status': 'success',
                    'message': f'event {event_id} was deleted!'
                }
                return response_object, 201
        except exc.IntegrityError:
            db.session.rollback()
            logging.debug("database rollback after a event deletion abortion")
            return response_object, 400


    def get(self, event_id):
        """Get one event details"""
        response_object = {
            'status': 'fail',
            'message': 'Event does not exist'
        }
        try:
            queryResult= pocketMoney.query.filter_by(id=int(event_id)).first()
            if not queryResult:
                return response_object, 404
            else:
                 response_object = {
                     'status': 'success',
                     'data': {
                        'id': queryResult.id,
                        'username': queryResult.username,
                        'activities': queryResult.activities,
                        'money': queryResult.money
                     }
                 }
                 return response_object, 200
        except ValueError:
            return response_object, 404

api.add_resource(UsersPing, '/users/ping')
api.add_resource(EventList, '/events') # 注意，EventList and Event二個resources不同
api.add_resource(Event, '/events/<event_id>') # event_id是傳入變數名不能亂取要配合API
