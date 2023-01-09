from app.repository.contact_repository import ContactRepository

db = ContactRepository()


def manage_create_contact(data):
    """ """
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
