# -*- coding: utf-8 -*-
from model.group import Group
    
def test_create_group(app):
    app.group.create(Group(name="group 4", header="header 4", footer="footer 4"))

def test_create_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))