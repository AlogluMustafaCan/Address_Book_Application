""" """
import re


def email_validation(data):
    """ """
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat, data):
        return True
    return False
