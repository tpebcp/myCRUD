# services/users/project/api/models.py


from sqlalchemy.sql import func

from project import db


class pocketMoney(db.Model):
    __tablename__ = 'pocketMoney'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    event = db.Column(db.String(128), nullable=False)
    money = db.Column(db.Integer(), nullable=True)
    #active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, event):
        self.username = username
        self.event = event

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'event': self.event,
            'money': self.money
        }