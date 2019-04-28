# services/users/project/tests/test_users.py


import json
import unittest

from project.tests.base import BaseTestCase

def add_event(username, event):
    record =pocketMoney(username=username, event=event)
    db.session.add(record)
    db.session.commit()
    return record

class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('GOOD!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_event(self):
        """Ensure a new event can be added to the database."""
        with self.client:
            response = self.client.post(
                '/events',
                data=json.dumps({
                    'username': 'budien',
                    'event': 'joggking 3K'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('added!', data['message'])
            self.assertIn('success', data['status'])


    def test_add_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/events',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """
        Ensure error is thrown if the JSON object does not have a username key.
        """
        with self.client:
            response = self.client.post(
                '/events',
                data=json.dumps({'event': 'jogging for 3k'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

def test_all_events(self):
    """Ensure get all users behaves correctly."""
    add_event('budien', 'petty cash from grandma')
    add_event('claire', 'prize from school')
    with self.client:
        response = self.client.get('/events')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']['users']), 2)
        self.assertIn('budien', data['data']['users'][0]['username'])
        self.assertIn(
            'petty cash from grandma', data['data']['users'][0]['event'])
        self.assertIn('fletcher', data['data']['users'][1]['username'])
        self.assertIn(
            'prize from school', data['data']['users'][1]['event'])
        self.assertIn('success', data['status'])

if __name__ == '__main__':
    unittest.main()
