""" """


class Contact:
    """ """

    def __init__(
            self,
            name=None,
            address=None,
            phone=None,
            mobile_phone=None,
            email=None
    ):
        self.name = name
        self.address = address
        self.phone = phone
        self.mobile_phone = mobile_phone
        self.email = email


    def get_json(self):
        """ """
        return self.__dict__

    @staticmethod
    def get_contact_object(json_data):
        """ """
        if json_data is not None:
            try:
                return Contact(
                    json_data["name"],
                    json_data["address"],
                    json_data["phone"],
                    json_data["mobile_phone"],
                    json_data["email"]
                )
            except KeyError as error:
                raise Exception("Key not found : {}".format(error))
        else:
            raise Exception("No data to create")
