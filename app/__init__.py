""" """
from flask import Flask
from app.controller.contacts_controller import contact


def create_app():
    """ """
    app = Flask(__name__)
    app.register_blueprint(contact)
    return app
