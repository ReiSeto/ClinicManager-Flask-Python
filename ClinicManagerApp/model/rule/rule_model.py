from sqlalchemy import Column, Integer, String

from ClinicManagerApp import db


class RuleModel(db.Model):
    __tablename__ = 'rule_model'

    # primary key
    rule_id = Column(Integer, primary_key=True, autoincrement=True)

    # attribute
    name = Column(String(150), unique=True, nullable=False, default='')
    amount = Column(Integer, default=0)

    def __str__(self):
        return self.name
