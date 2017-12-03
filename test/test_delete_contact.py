from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Peter", lastname="Pyatochkin", company="System Group", address="Ukraine, Kiev, Vatslava Gavela blvd., 4",
                       mobile="+38 050 777 88 99", email="p.pyatochkin@gmail.com", year="1980"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()

    assert len(old_contacts) - 1 == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts