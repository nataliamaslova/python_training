from model.contact import Contact
from random import randrange

def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Peter", lastname="Pyatochkin", company="System Group", address="Ukraine, Kiev, Vatslava Gavela blvd., 4",
                                   mobilephone="+38 050 777 88 99", email="p.pyatochkin@gmail.com", year="1980"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Peter2", lastname="Pyatochkin555", company="System Group2", address="2Ukraine, Kiev, Vatslava Gavela blvd., 4",
                      mobilephone="+38 050 777 88 00", email="p2.pyatochkin@gmail.com", year="1981")
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)