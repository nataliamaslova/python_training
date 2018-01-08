# -*- coding: utf-8 -*-
from model.group import Group

def test_create_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)

    # without this commit next assert is failure: data from db is old
    db.connection.commit()

#    redundant check
#    assert len(old_groups) + 1 == len(db.get_group_list()) # count used as a hash function for preliminary check

    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)