from flask import Blueprint, jsonify, current_app, request, abort
from sqlalchemy import desc
from app import db

from models.messages import Message

message = Blueprint('message', __name__)


@message.route('/message/<message_id>', methods=['GET'])
def get(message_id):
    return jsonify()


@message.route('/message/all', methods=["GET"])
def get_all():
    m = db.session.query(Message).order_by(
        desc(Message.id)
    ).limit(1000)

    return jsonify(messages=[i.serialize() for i in m.all()])


@message.route('/message', methods=['POST'])
def insert():
    try:
        msg = Message(
            body=request.json['body'],
            sender=request.json['sender'],
            destination=request.json['destination'],
            customer_id=request.json['customer_id'],
            parameters=request.json['parameters']
        )
        db.session.add(msg)
        db.session.commit()

        return jsonify(msg.serialize())
    except KeyError:
        return jsonify("key error"), 400
    except TypeError:
        return jsonify("wrong content-type"), 400
