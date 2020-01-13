from sqlalchemy import Column, Integer, Text, String
from app import db


class MessageBody(db.model):
    __tablename__ = 'messages_body'

    id = Column(Integer, primary_key=True)
    body_plaintext = Column(Text, nullable=False)
    body_html = Column(Text, nullable=True)
    title = Column(String(250), nullable=True)

    def __init__(self, body_plaintext, body_html=None, title=None):
        self.body_plaintext = body_plaintext
        self.body_html = body_html
        self.title = title