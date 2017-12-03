from model.group import Group

def test_update_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(name="group 44", header="header 44", footer="footer 44"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)