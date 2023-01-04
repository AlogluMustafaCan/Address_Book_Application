""" """
from flask import Blueprint, request

contact = Blueprint('contact', __name__)


@contact.route('/', methods=["POST"])
def add_contact():
    json_contact = request.get_json()
    return json_contact
