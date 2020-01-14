#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.messages import *
from models.message_body import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import create_app

app = create_app('settings')
db = SQLAlchemy(app)

migrate = Migrate(app, db)
