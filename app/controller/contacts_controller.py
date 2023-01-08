""" """
from flask import Blueprint, request, jsonify
from app.repository.contact_repository import ContactRepository

contact = Blueprint('contact', __name__)
db = ContactRepository()


@contact.post('/')
def add_contact():
    """ """

    db.create(request.get_json())
    # TODO: return will be fixed
    return "OK"


@contact.get('/get')
def get_contact_by_name():
    """"""
    return "Works"


@contact.delete('/delete')
def delete_contact_by_name():
    """ """
    return "Works"


@contact.put('/update')
def update_contact_by_name():
    """"""
    return "Works"
