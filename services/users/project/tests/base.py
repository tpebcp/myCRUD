# services/users/project/tests/base.py


from flask_testing import TestCase

from project import create_app, db

app = create_app()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        print("*******setup database - create all")
        db.create_all()
        db.session.commit()

    def tearDown(self):
        print("********drop tables - clear all")
        db.session.remove()
        db.drop_all()
