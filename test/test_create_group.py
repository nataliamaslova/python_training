# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)

        # alternative: 8 combinations
        # Group(name=name, header=header, footer=footer)
        # for name in ["", random_string("name", 10)]
        # for header in ["", random_string("header", 20)]
        # for footer in ["", random_string("footer", 20)]
    ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_create_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count() # count used as a hash function for preliminary check

    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
