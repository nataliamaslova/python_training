from model.group import Group

def test_modify_group(app):
    app.group.update_first_group(Group(name="group 44", header="header 44", footer="footer 44"))

def test_modify_group_name(app):
    app.group.update_first_group(Group(name="New group"))

def test_modify_group_header(app):
    app.group.update_first_group(Group(header="New header"))