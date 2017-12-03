from model.contact import Contact

def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Peter", lastname="Pyatochkin", company="System Group", address="Ukraine, Kiev, Vatslava Gavela blvd., 4",
                       mobile="+38 050 777 88 99", email="p.pyatochkin@gmail.com", year="1980"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Peter2", lastname="Pyatochkin2", company="System Group2", address="2Ukraine, Kiev, Vatslava Gavela blvd., 4",
                                             mobile="+38 050 777 88 00", email="p2.pyatochkin@gmail.com", year="1981")
    contact.id = old_contacts[0].id
    app.contact.update_first_contact(contact)
    assert len(old_contacts) == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)