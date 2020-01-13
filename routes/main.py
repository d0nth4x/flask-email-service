from flask import Blueprint, jsonify, current_app

main = Blueprint('main', __name__)


@main.route('/')
def get():
    return jsonify()
