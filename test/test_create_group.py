# -*- coding: utf-8 -*-
from model.group import Group
    
def test_create_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="group 4", header="header 4", footer="footer 4")
    app.group.create(group)

    assert len(old_groups) + 1 == app.group.count() # count used as hash function fro preliminary check

    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_create_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
