from model.contact import Contact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(Contact(firstname="Peter2", lastname="Pyatochkin2", company="System Group2", address="2Ukraine, Kiev, Vatslava Gavela blvd., 4",
                                             mobile="+38 050 777 88 00", email="p2.pyatochkin@gmail.com", year="1981"))
    app.session.logout()