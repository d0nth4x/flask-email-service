# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, current_app
from sqlalchemy import desc
from models.message_body import MessageBody

templates = Blueprint('templates', __name__)


@templates.route('/templates', methods=['GET'])
def get_all():
    template_list = current_app.db.session.query(MessageBody).filter().order_by(
        desc(MessageBody.id)
    ).limit(1000)

    return jsonify(template_list)
