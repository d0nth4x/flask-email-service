#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from flask_mail import Mail
from flask_migrate import Migrate

db = SQLAlchemy()
mail = Mail()


def create_app(config_filename='settings', check_db=True):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config_filename)

    # database
    migrate = Migrate(app, db)
    db.init_app(app)

    if check_db and not database_exists(app.config.get('SQLALCHEMY_DATABASE_URI')):
        create_db(True)

    # routes
    from routes import main, message, message_body
    app.register_blueprint(main.main)
    app.register_blueprint(message.message)
    app.register_blueprint(message_body.body)

    # mail
    mail.init_app(app)

    return app


def create_db(force=False):
    """Create fresh DB"""
    _answer = 'n'
    _loop = True

    if force is False:
        while _loop is True:
            print('Drop existing db and create new one? [y/N]')
            _answer = input()
            _loop = False if _answer in ('y', 'n', 'Y', 'N') else True
            if _answer in ('n', 'N', ''):
                return

    db.drop_all(app=create_app(check_db=False))
    db.create_all(app=create_app(check_db=False))


if __name__ == '__main__':
    app = create_app()
    app.run()
