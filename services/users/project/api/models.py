# services/users/project/api/models.py


from sqlalchemy.sql import func

from project import db


class pocketMoney(db.Model):
    __tablename__ = 'pocketMoney'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    activities = db.Column(db.String(128), nullable=False)
    money = db.Column(db.Integer(), nullable=True)
    disabled = db.Column(db.Boolean(), default=False, nullable=False)

    def __init__(self, username, activities, money,disabled):
        self.username = username
        self.activities = activities
        self.money = money
        self.disabled = disabled

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'activities': self.activities,
            'money': self.money,
            'disabled': self.disabled
        }
