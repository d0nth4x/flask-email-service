from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from flask_mail import Mail

from flask_migrate import Migrate

db = SQLAlchemy()
mail = Mail()


def create_app(config_filename='settings', check_db=True):
    app = Flask(__name__, template_folder='templates')

    migrate = Migrate(app, db)
    db.init_app(app)

