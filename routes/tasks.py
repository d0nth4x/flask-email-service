from flask import Blueprint, jsonify, current_app
tasks = Blueprint('tasks', __name__)


@tasks.route('/tasks', methods=['GET'])
def get():

    return jsonify()


@tasks.route('/tasks/add', methods=['POST'])
def insert():

    return jsonify()
