from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="group 44", header="header 44", footer="footer 44"))
    app.session.logout()

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="New group"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(header="New header"))
    app.session.logout()