import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON, Text
from app import db


class MessageBody(db.Model):
    __tablename__ = 'messages_body'

    id = Column(Integer, primary_key=True)
    body_plaintext = Column(Text, nullable=False)
    body_html = Column(Text, nullable=True)
    subject = Column(String(250), nullable=True)

    def __init__(self, body_plaintext, body_html=None, subject=None):
        self.body_plaintext = body_plaintext
        self.body_html = body_html
        self.subject = subject

    @property
    def serialize(self):
        return {
            'id': self.id,
            'body_plaintext': self.body_plaintext,
            'body_html': self.body_html,
            'subject': self.subject
        }


class Message(db.Model):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    body = Column(Integer, ForeignKey('messages_body.id'))
    create_date = Column(DateTime, nullable=False)
    send_date = Column(DateTime, nullable=True)
    sender = Column(String, nullable=False)
    destination = Column(JSON, nullable=False)
    customer_id = Column(Integer, nullable=True)
    parameters = Column(JSON, nullable=False, default=[])
    status = Column(Integer)
    status_smtp = Column(Integer)

    def __init__(self, body, sender, destination, customer_id=0, parameters=None, create_date=None,
                 send_date=None, status=0, status_smtp=0):
        self.body = body
        self.sender = sender
        self.destination = destination
        self.customer_id = customer_id
        self.status = status
        self.status_smtp = status_smtp
        self.parameters = parameters,

        if send_date is None:
            self.send_date = datetime.datetime.now()
        elif type(send_date) is str:
            self.send_date = datetime.datetime.strptime(send_date, "%Y-%m-%d")
        else:
            self.send_date = datetime.datetime(send_date)

        if create_date is None:
            self.create_date = datetime.datetime.now()
        else:
            self.create_date = create_date

    def serialize(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'status': self.status,
            'status_smtp': self.status_smtp
        }
