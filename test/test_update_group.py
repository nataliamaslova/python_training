from model.group import Group

def test_update_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first_group(Group(name="group 44", header="header 44", footer="footer 44"))

def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first_group(Group(name="New group"))

def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first_group(Group(header="New header"))