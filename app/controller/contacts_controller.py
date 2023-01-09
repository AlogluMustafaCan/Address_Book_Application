""" """
from flask import Blueprint, request
from app.repository.contact_repository import ContactRepository
from app.service import contact_service

contact = Blueprint('contact', __name__)
db = ContactRepository()


@contact.post('/')
def add_contact():
    """ """
    # res = request.get_json()
    # print(f"res before db : {res}")
    # db.create(request.get_json())
    # print(f"res after db : {res}")
    # return res
    return contact_service.manage_create_contact(request.get_json())


@contact.get('/get/<name>')
def get_contact_by_name(name):
    """"""
    return contact_service.manage_get_contact(name)


@contact.delete('/delete/<name>')
def delete_contact_by_name(name):
    """ """
    contact_service.manage_delete_contact(name)
    return "OK"


@contact.put('/update/<name>')
def update_contact_by_name(name):
    """ """
    contact_service.manage_update_contact(name, request.json)
    return "Works"
