# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, current_app, abort
from sqlalchemy import desc
from models.messages import MessageBody
from app import db

body = Blueprint('message_body', __name__)


@body.route('/message/body/all', methods=['GET'])
def get_all():
    b = db.session.query(MessageBody).filter().order_by(
        desc(MessageBody.id)
    ).limit(1000)

    return jsonify(template_list=[i.serialize for i in b.all()])


@body.route('/message/body/<body_id>', methods=['GET'])
def get_one(body_id):
    b = db.session.query(MessageBody).filter(MessageBody.id == body_id).first()

    return jsonify(b.serialize)


@body.route('/message/body', methods=['POST'])
def create():
    try:
        message_body = MessageBody(
            body_plaintext=request.json['body_plaintext'],
            body_html=request.json['body_html'],
            subject=request.json['subject']
        )

        db.session.add(message_body)
        db.session.commit()

        return jsonify(message_body.serialize)
    except KeyError as e:
        abort(400)
