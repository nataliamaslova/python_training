# -*- coding: utf-8 -*-
from model.contact import Contact

def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Peter", lastname="Pyatochkin", company="System Group", address="Ukraine, Kiev, Vatslava Gavela blvd., 4",
                       mobile="+38 050 777 88 99", email="p.pyatochkin@gmail.com", year="1980")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

