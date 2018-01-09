# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group

def test_remove_contact_from_group(app, dbORM):
    # Preliminary condition: Contact with id = 80 is in Group with id = 329
    contact = Contact(id="80")
    group = Group(id="329")
    old_contacts_in_group = dbORM.get_contacts_in_group(group)
    app.contact.remove_contact_from_group_by_ids(contact.id, group.id)
    assert len(old_contacts_in_group) - 1 == len(dbORM.get_contacts_in_group(group))



