# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group

def test_add_contact_to_group(app, dbORM):
    # Preliminary condition: Contact with id = 80 and Group with id = 329 are exist
    contact = Contact(id="80")
    group = Group(id="329")
    old_contacts_in_group = dbORM.get_contacts_in_group(group)
    app.contact.add_contact_to_group_by_ids(contact.id, group.id)
    assert len(old_contacts_in_group) + 1 == len(dbORM.get_contacts_in_group(group))



