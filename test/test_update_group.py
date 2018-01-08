from model.group import Group
import random

# def test_update_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.update_first_group(Group(name="group 44", header="header 44", footer="footer 44"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

def test_update_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
        db.connection.commit()
    old_groups = db.get_group_list()
    modified_group = random.choice(old_groups)

    group = Group(name="New group")
    app.group.update_group_by_id(modified_group.id, group)
    db.connection.commit()
    assert len(old_groups) == len(db.get_group_list())

    new_groups = db.get_group_list()

    old_groups_modified = []
    for old_group in old_groups:
        if (old_group.id == modified_group.id):
            old_group.name = group.name
        old_groups_modified.append(old_group)

    assert sorted(old_groups_modified, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)