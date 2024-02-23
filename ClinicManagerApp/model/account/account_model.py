import hashlib
from datetime import datetime

from sqlalchemy import Column, Text, String, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from ClinicManagerApp import db
from flask_login import UserMixin


class AccountModel(db.Model, UserMixin):
    __tablename__ = 'account_model'

    # primary keys
    account_id = Column(Integer, primary_key=True, autoincrement=True)

    # attributes
    username = Column(String(20), unique=True, nullable=False, default='')
    password = Column(String(40), nullable=False, default='')
    avatar = Column(Text, default='')
    is_active = Column(Boolean, default=True)
    last_access = Column(DateTime, default=datetime.now())

    # foreign keys
    role_id = Column(Integer, ForeignKey('role_model.role_id'))

    # relationship
    staff = relationship('StaffModel', backref=backref('account', uselist=False, lazy=True),
                         foreign_keys='[StaffModel.account_id]', uselist=False, lazy=True)

    def __str__(self):
        return '{}'.format(self.username)

    def get_id(self):
        return self.account_id

    def set_avatar(self, url):
        self.avatar = url

    def set_password(self, password):
        self.password = hashlib.md5(password.encode('utf8')).hexdigest()
