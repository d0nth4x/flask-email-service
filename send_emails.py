#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import create_app
from lib.send_messages import send_messages
from time import sleep

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        while True:
            send_messages()
            sleep(app.config.get('MAIL_SEND_DELAY') if not None else 300)
