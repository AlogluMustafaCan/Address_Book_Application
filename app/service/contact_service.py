from app.repository.contact_repository import ContactRepository
from app.service import validation

db = ContactRepository()


def manage_create_contact(data):
    """ """
    if not validation.email_validation(data["email"]):
        return {
            "Error": "Invalid Email"
        }
    db.create(data)
    del data["_id"]
    return data


def manage_get_contact(data):
    """ """
    res = db.read(data)
    del res["_id"]
    return res


def manage_delete_contact(data):
    """ """
    db.delete(data)


def manage_update_contact(name, data):
    """ """
    db.update(name, data)
