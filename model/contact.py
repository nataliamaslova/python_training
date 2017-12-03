from sys import maxsize

class Contact:

    def __init__(self, firstname = None, lastname = None, company = None, address = None, mobile = None,
                 email = None, year = None, id = None):
         self.firstname = firstname
         self.lastname = lastname
         self.company = company
         self.address = address
         self.mobile = mobile
         self.email = email
         self.year = year
         self.id = id

    def __repr__(self):
         return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
         return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname ==other.lastname

    def id_or_max(contact):
        if contact.id:
            return int(contact.id)
        else:
            return maxsize
